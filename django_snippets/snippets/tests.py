from django.urls import resolve
from django.test import TestCase, Client, RequestFactory
from snippets.models import Snippet
from snippets.views import top, snippet_detail, snippet_new, snippet_edit, snippets_list
from django.contrib.auth import get_user_model

UserModel = get_user_model()

class TopPageRenderSnippetsTest(TestCase):
    def setUp(self):
        self.user = UserModel.objects.create(
            username = 'test_user',
            email = 'test@ex.com',
            password = 'abcd1234',
        )
        self.snippet = Snippet.objects.create(
            title = 'title1',
            code = 'I like Chocolate!',
            desc='description!',
            created_by = self.user,
        )

    def test_should_return_snippet_title(self):
        request = RequestFactory().get('/')
        request.user = self.user
        response = top(request)
        self.assertContains(response, self.snippet.title)

    def test_should_return_username(self):
        req = RequestFactory().get('/')
        req.user = self.user
        res = top(req)
        self.assertContains(res, self.user.username)

class SnippetDetailTest(TestCase):
    def setUp(self):
        self.user = UserModel.objects.create(
            username = 'test_user',
            email = 'test@ex.com',
            password = 'abcd1234',
        )
        self.snippet = Snippet.objects.create(
            title = 'タイトル',
            code = 'コード',
            desc='説明',
            created_by = self.user,
        )

    def test_should_use_expect_template(self):
        res = self.client.get('/snippets/{}/'.format(self.snippet.id))
        self.assertTemplateUsed(res, 'snippets/snippet_detail.html')

    def test_top_page_return_200_and_expected_heading(self):
        res = self.client.get('/snippets/{}/'.format(self.snippet.id))
        self.assertContains(res, self.snippet.title, status_code=200)

class CreateSnippetTest(TestCase):
    def setUp(self):
        self.user = UserModel.objects.create(
            username = 'test_user',
            email = 'test@ex.com',
            password = 'abcd1234',
        )
        self.client.force_login(self.user)

    def test_render_creation_form(self):
        res = self.client.get('/snippets/new/')
        self.assertContains(res, 'スニペットの登録', status_code=200)

    def test_create_snippet(self):
        data = {'title': 'タイトル2', 'code': 'super code', 'desc': 'not desk'}
        res = self.client.post('/snippets/new/', data)
        snippet = Snippet.objects.get(title='タイトル2')
        self.assertEqual(snippet.code, 'super code')
        self.assertEqual(snippet.desc, 'not desk')

# class TopPageTest(TestCase): #継承の書き方
#     # TestCaseでは事前に、django.test.Clientクラスが提供されているため、
#     # self.client で使える
#     def test_top_retursns_200_and_exoected_title(self):
#         response = self.client.get('/')
#         self.assertContains(response, 'Djangoスニペット', status_code=200)

#     def test_top_page_uses_expected_template(self):
#         response = self.client.get('/')
#         self.assertTemplateUsed(response, 'snippets/top.html')

# class SnippetsListTest(TestCase):
#     def test_should_resolve_snippets_list(self):
#         found = resolve('/snippets/')
#         self.assertEqual(snippets_list, found.func)

# class CreateSnippetTest(TestCase):
#     def test_should_resolve_snippet_new(self):
#         found = resolve('/snippets/new/')
#         # django.urls.resolve(path) -> 渡したURLパスに対応するビュー関数の結果を返す
#         self.assertEqual(snippet_new, found.func)
#         # found.func -> ビュー関数自信を返す

# class SnippetDetailTest(TestCase):
#     def test_should_resolve_snippets_detail(self):
#         found = resolve('/snippets/1/')
#         self.assertEqual(snippet_detail, found.func)

# class EditSnippetTest(TestCase):
#     def test_should_resolve_snippet_edit(self):
#         found = resolve('/snippets/1/edit/')
#         self.assertEqual(snippet_edit, found.func)
