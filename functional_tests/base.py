import sys

from django.test import LiveServerTestCase
from selenium import webdriver

from store.models import Product
DEFAULT_WAIT = 5


class FunctionalTest(LiveServerTestCase):
    
    @classmethod
    def setUpClass(cls):  
        for arg in sys.argv:  
            if 'liveserver' in arg:  
                cls.server_url = 'http://' + arg.split('=')[1]  
                return  
        super(FunctionalTest, cls).setUpClass()
        cls.server_url = cls.live_server_url

    @classmethod
    def tearDownClass(cls):
        if cls.server_url == cls.live_server_url:
            super(FunctionalTest,cls).tearDownClass() 

    def setUp(self):  
        Product.objects.create(name="Milk", price=2)
        Product.objects.create(name="Sugar", price=2)
        Product.objects.create(name="Salt", price=2)
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(DEFAULT_WAIT)

    def tearDown(self):
        self.browser.quit()
        super(FunctionalTest, self).tearDown()
        
