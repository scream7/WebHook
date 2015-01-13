# -*- coding: utf-8 -*-  
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.db import connection,transaction
from request.models import *
from django.views.decorators.csrf import csrf_exempt
import datetime
import sys
reload(sys)
sys.setdefaultencoding('utf8')

def query_form(request):
	return render_to_response("query_form.html")

#disabled csrf function
@csrf_exempt
def insert(request):  
    if request.POST.has_key('keywords') and request.POST.has_key('url') and request.POST.has_key('email'): 
        keywords = request.POST['keywords']  
        url = request.POST['url']
        if url.find('http://') == -1:
            url = 'http://' + url
        email = request.POST['email']
        message = '您搜索的关键字是: %r\n' % keywords
        message += 'URL: %r\n' % url
        message += 'Email: %r\n' % email

        insert_record(url,keywords,KeywordsCount(url,keywords),email)

        message += '数据插入成功!<br>'
        message += '现有数据:<br>'
        for i in query_db():
            message += str(i.id)
            message += " "
            message += i.url
            message += " "
            message += i.keywords
            message += " "
            message += str(i.keywordscount)
            message += " "
            message += i.email
            message += " "
            message += str(i.datetime)
            message += "<br>"
        message += str(datetime.datetime.utcnow())
        return HttpResponse(message)  
    else:  
        return render_to_response("query_form.html",{'error': True})

def check(request):
    for record in query_db():
        id = record.id
        url = record.url
        keywords = record.keywords
        keywordscount = record.keywordscount
        email = record.email
        datetime = record.datetime
        body = "OK"
        if KeywordsCount(url,keywords) != keywordscount:
            body = u"URL:%s\n关键字:%s,更新了."%(url,keywords)
            sendmail('更新通知',body,email)
            delete_record(id)
    return HttpResponse(body)


def query_db():
    return request.objects.all()

def delete_record(id_):
    request.objects.filter(id = id_).delete()

def insert_record(url_,keywords_,keywordscount_,email_):
    request.objects.create(url = url_,keywords = keywords_,keywordscount = keywordscount_,email = email_)

def sendmail(Subject,Body,To):
    from sae.mail import send_mail
    import settings
    send_mail(To, Subject, Body,
          (settings.EMAIL_HOST, settings.EMAIL_PORT, settings.EMAIL_HOST_USER, settings.EMAIL_HOST_PASSWORD, settings.EMAIL_USE_TLS))

def KeywordsCount(url,keywords):
    import urllib
    str = urllib.urlopen(url).read().decode("gbk")
    return str.count(keywords)