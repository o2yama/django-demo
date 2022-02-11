from django.test import TestCase
from django.http import HttpRequest
from snippets import views

# b’Hello World’を投げて正しく返ってくるかのテスト

# class TopPageViewTest(TestCase):
    # def test_top_retursns_200(self):
    #     request = HttpRequest()
    #     responce = views.top(request)
    #     self.assertEqual(responce.status_code, 200)
        
    # def test_top_returns_expect_content(self):
    #     request = HttpRequest()
    #     responce = views.top(request)
    #     self.assertEqual(responce.content, b'Hello World')


class TopPageTest(TestCase): #継承の書き方
    # TestCaseでは事前に、django.test.Clientクラスが提供されているため、
    # self.client で使える
    def test_top_retursns_200(self):
        responce = self.client.get('/')
        self.assertEqual(responce.status_code, 200)
        
    def test_top_returns_expect_content(self):
        responce = self.client.get('/')
        self.assertEqual(responce.content, b'Hello World')

