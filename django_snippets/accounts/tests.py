from django.test import TestCase

class LoginPageTest(TestCase):
    def test_should_use_expect_template(self):
        res = self.client.get('/accounts/login')
        self.assertTemplateUsed(res, 'accounts/login.html')
    
    def test_login_page_return_status_code_200(self):
        res = self.client.get('/accounts/login')
        self.assertContains(res, 'ログイン', status_code=200)

class SignupPageTest(TestCase):
    def test_should_use_expected_templates(self):
        res = self.client.get('/accounts/signup')
        self.assertTemplateUsed(res, 'accounts/signup.html')

    def test_page_return_200(self):
        res = self.client.get('/accounts/signup')
        self.assertContains(res, '会員登録', status_code=200)
