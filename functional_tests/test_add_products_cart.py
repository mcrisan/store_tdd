from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from .base import FunctionalTest


class NewVisitorTest(FunctionalTest): 
    
    def test_can_add_products_to_cart(self):  
        # Ana has heard about a cool new online store. She goes
        # to check out its homepage
        self.browser.get(self.server_url)

        # She notices the page title and header mention store
        self.assertIn('Store', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('Store', header_text)

        # She notices on the homepage a list of products
        list_products = self.browser.find_element_by_css_selector(
            '.list_products'
        )
        self.assertIn(
                'List of products',
                list_products.text
                
        )

        # She notices that each product has an input box under it
        products = list_products.find_elements_by_css_selector(
            '.product'
        )
        inputs = self.browser.find_elements_by_tag_name('input')
        self.assertEqual(len(products), len(inputs))

        # On the list of products she saw the product milk. So she decided
        # to buy 5 bottles
        milk = list_products.find_element_by_css_selector(".product[data-name='Milk']")
        input_ = milk.find_element_by_tag_name('input')
        input_.send_keys(5)
        input_.send_keys(Keys.ENTER)
        
        # She can see on the sidebar that her cart was updated with the 
        # product she wanted
        cart = self.browser.find_elements_by_css_selector(
            '.cart'
        )
        cartprod = cart.find_elements_by_css_selector(
            '.cartprod'
        )
        self.assertIn("Milk 2", [prod.text for prod in cartprod])
        self.fail()
        
