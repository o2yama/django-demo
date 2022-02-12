from django.urls import resolve
from django.test import TestCase
from snippets.views import top, snippet_detail, snippet_new, snippet_edit, snippets_list

# b’Hello World’を投げて正しく返ってくるかのテスト

# class TopPageViewTest(TestCase):
    # def test_top_retursns_200(self):
    #     request = HttpRequest()
    #     responce = top(request)
    #     self.assertEqual(responce.status_code, 200)
        
    # def test_top_returns_expect_content(self):
    #     request = HttpRequest()
    #     responce = top(request)
    #     self.assertEqual(responce.content, b'Hello World')


# class TopPageTest(TestCase): #継承の書き方
#     # TestCaseでは事前に、django.test.Clientクラスが提供されているため、
#     # self.client で使える
#     def top_retursns_200(self):
#         responce = self.client.get('/')
#         self.assertEqual(responce.status_code, 200)
        
#     def top_returns_expect_content(self):
#         responce = self.client.get('/')
#         self.assertEqual(responce.content, b'Hello World')
        
class SnippetsListTest(TestCase):
    def test_should_resolve_snippets_list(self):
        found = resolve('/snippets/')
        self.assertEqual(snippets_list, found.func)

class CreateSnippetTest(TestCase):
    def test_should_resolve_snippet_new(self):
        found = resolve('/snippets/new/') 
        # django.urls.resolve(path) -> 渡したURLパスに対応するビュー関数の結果を返す
        self.assertEqual(snippet_new, found.func) 
        # found.func -> ビュー関数自信を返す
        
class SnippetDetailTest(TestCase):
    def test_should_resolve_snippets_detail(self):
        found = resolve('/snippets/1/')
        self.assertEqual(snippet_detail, found.func)
        
class EditSnippetTest(TestCase):
    def test_should_resolve_snippet_edit(self):
        found = resolve('/snippets/1/edit/')
        self.assertEqual(snippet_edit, found.func)