
from project.utils.test import FunctionalTestCase
from django.contrib.auth import get_user_model

User = get_user_model()


USERNAME = 'probably-not-going-to-match-anything-else'


class FunctionalTestCaseTests(FunctionalTestCase):

    def setUp(self):
        self.user = User.objects.create_user(username=USERNAME, password='password')

    def test_login(self):
        self.assertNotIn(USERNAME, self.driver.page_source)

        self.login(username=USERNAME, password='password')

        self.driver.get(self.url('home'))
        self.assertIn(USERNAME, self.driver.page_source)

    def test_force_login(self):
        self.assertNotIn(USERNAME, self.driver.page_source)

        self.force_login(self.user)

        self.driver.get(self.url('home'))
        self.assertIn(USERNAME, self.driver.page_source)

    def test_url(self):
        self.assertEqual(self.url('login'), '%s/accounts/login' % self.live_server_url)
