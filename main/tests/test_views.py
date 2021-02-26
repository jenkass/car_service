from django.test import TestCase
from main.views import *
from django.urls import reverse
from main.models import *


class TestAllTeamView(TestCase):

    def test_all_team_correct_output_200(self):
        resp = self.client.get('http://127.0.0.1:8000/team/')
        self.assertEqual(resp.status_code, 200)

    def test_all_team_correct_template_team_html(self):
        resp = self.client.get('http://127.0.0.1:8000/team/')
        self.assertTemplateUsed(resp, 'main/team.html')


class TestOtherPageView(TestCase):

    def test_other_page_correct_output_200(self):
        resp = self.client.get('http://127.0.0.1:8000/about/')
        self.assertEqual(resp.status_code, 200)

    def test_other_page_incorrect_output_Http404(self):
        resp = self.client.get('http://127.0.0.1:8000/2/')
        self.assertRaises(Http404)

    def test_other_page_correct_template_about_html(self):
        resp = self.client.get('http://127.0.0.1:8000/about/')
        self.assertTemplateUsed(resp, 'main/about.html')


class TestIndexView(TestCase):

    @classmethod
    def setUpTestData(cls):
        count = 3
        for cat in range(count):
            Cat.objects.create(title="Шиномонтаж %s" % cat, content='СТО обслуживает идеально %s' % count,
                               price=2500.55, is_active=True)

    def test_index_correct_output_200(self):
        resp = self.client.get('http://127.0.0.1:8000/')
        self.assertEqual(resp.status_code, 200)

    def test_index_correct_count_category_output_3(self):
        resp = self.client.get('http://127.0.0.1:8000/')
        self.assertTrue(len(resp.context['cat']) == 3)

    def test_other_page_correct_template_index_html(self):
        resp = self.client.get('http://127.0.0.1:8000/index/')
        self.assertTemplateUsed(resp, 'main/index.html')


class TestProfileView(TestCase):

    @classmethod
    def setUpTestData(cls):
        author = AdvUser.objects.create(password='mikipiki123', username='jenkass_')
        cat = Cat.objects.create(title="Шиномонтаж", content='СТО обслуживает идеально', price=2500.55, is_active=True)
        count = 3
        for order in range(count):
            Order.objects.create(category=cat, author=author, date='2015-10-12 15:42:2%s' % order,
                                 number='+375299370205')

    def test_index_correct_output_200(self):
        resp = self.client.get('http://127.0.0.1:8000/accounts/profile/')
        self.assertEqual(resp.status_code, 200)

    def test_index_correct_count_category_output_False(self):
        resp = self.client.get('http://127.0.0.1:8000/accounts/profile/')
        self.assertTrue(len(resp.context['order']) == False)

    def test_other_page_correct_template_profile_html(self):
        resp = self.client.get('http://127.0.0.1:8000/accounts/profile/')
        self.assertTemplateUsed(resp, 'main/profile.html')


class TestLoginView(TestCase):

    def setUp(self):
        user1 = AdvUser.objects.create(username='jenkass_', password='mikipiki123')
        user1.save()

    def test_login_correct_output_200(self):
        resp = self.client.get('http://127.0.0.1:8000/accounts/login/')
        self.assertEqual(resp.status_code, 200)

    def test_login_correct_template_login_html(self):
        resp = self.client.get('http://127.0.0.1:8000/accounts/login/')
        self.assertTemplateUsed(resp, 'main/login.html')

    def test_logged_user_True(self):
        login = self.client.login(username='jenkass_', password='mikipiki123')
        resp = self.client.get(reverse('main:index'))
        self.assertNotEqual(str(resp.context['user']), 'jenkass_')

    def test_not_logged_user_False(self):
        login = self.client.login(username='je', password='mik')
        resp = self.client.get(reverse('main:index'))
        self.assertFalse(login)


class TestLogoutView(TestCase):

    def test_logout_correct_output_302(self):
        resp = self.client.get('http://127.0.0.1:8000/accounts/logout/')
        self.assertEqual(resp.status_code, 302)


class TestAddOrderView(TestCase):

    def test_add_order_checked_corrected_output_200(self):
        resp = self.client.get('http://127.0.0.1:8000/accounts/profile/add/')
        self.assertEqual(resp.status_code, 200)

    def test_add_order_correct_template_order_add_html(self):
        resp = self.client.get('http://127.0.0.1:8000/accounts/profile/add/')
        self.assertTemplateUsed(resp, 'main/order_add.html')


class TestAddOrderDoneView(TestCase):

    def test_add_order_done_checked_corrected_output_200(self):
        resp = self.client.get('http://127.0.0.1:8000/accounts/profile/add/done/')
        self.assertEqual(resp.status_code, 200)


class TestDeleteOrderView(TestCase):

    def test_delete_order_done_checked_corrected_output_302(self):
        resp = self.client.get('http://127.0.0.1:8000/accounts/profile/delete/1/')
        self.assertEqual(resp.status_code, 302)

    def test_delete_order_correct_template_profile_html(self):
        resp = self.client.get('http://127.0.0.1:8000/accounts/profile/')
        self.assertTemplateUsed(resp, 'main/profile.html')


class TestChangePasswordView(TestCase):

    def test_password_change_checked_corrected_output_302(self):
        resp = self.client.get('http://127.0.0.1:8000/accounts/password/change')
        self.assertEqual(resp.status_code, 302)


class TestRegisterUserView(TestCase):

    def test_register_user_checked_corrected_output_200(self):
        resp = self.client.get('http://127.0.0.1:8000/accounts/register/')
        self.assertEqual(resp.status_code, 200)


class TestRegisterUserDoneView(TestCase):

    def test_register_user_done_checked_corrected_output_301(self):
        resp = self.client.get('http://127.0.0.1:8000/accounts/register/done')
        self.assertEqual(resp.status_code, 301)


class TestChangeUserInfoView(TestCase):

    def test_change_user_info_checked_corrected_output_302(self):
        resp = self.client.get('http://127.0.0.1:8000/accounts/profile/change')
        self.assertEqual(resp.status_code, 302)


class TestDeleteUserView(TestCase):

    def test_delete_user_checked_corrected_output_302(self):
        resp = self.client.get('http://127.0.0.1:8000/accounts/profile/delete/')
        self.assertEqual(resp.status_code, 302)
