from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium.webdriver.firefox.webdriver import WebDriver
import selenium.common.exceptions as selexcep

class MySeleniumTests(StaticLiveServerTestCase):
    fixtures = ["user.json"]

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.selenium = WebDriver()
        cls.selenium.implicitly_wait(10)

    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super().tearDownClass()

    def test_login(self):
        self.selenium.get("%s%s" % (self.live_server_url, "/accounts/login/"))
        email_input = self.selenium.find_element_by_name("login")
        email_input.send_keys("test@test.fr")
        password_input = self.selenium.find_element_by_name("password")
        password_input.send_keys("Aa123456789-")
        try:
            self.selenium.find_element_by_xpath(
                '//button[text()="Se connecter"]'
            ).click()
        except selexcep.NoSuchElementException:
            self.selenium.find_element_by_xpath(
                '//button[text()="Connexion"]'
            ).click()
