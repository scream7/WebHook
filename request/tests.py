"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from request.models import *

class SimpleTest(TestCase):
    def test_basic_addition(self):
        """
        Tests that 1 + 1 always equals 2.
        """
        self.assertEqual(1 + 1, 2)

class RequestTestCase(TestCase):
	def setUp(self):
		request.objects.create(url = 'url1',keywords = 'keywords1',keywordscount = 1,email = 'email1')
		request.objects.create(url = 'url2',keywords = 'keywords2',keywordscount = 2,email = 'email2')
	def test_insert_succeed(self):
		record1 = request.objects.get(url = 'url1')
		record2 = request.objects.get(url = 'url2')
		self.assertEqual(record1.url,'url1')
		self.assertEqual(record2.url,'url2')


