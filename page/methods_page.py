from selenium.webdriver.common.by import By
from page.base_page import BasePage


class MethodsPage(BasePage):
    def execute(self, page_name):
        xpath = f'//a[contains(text(),"{page_name}")]'
        self.wait_until(By.XPATH, xpath)
        elem =self.browser.find_element(By.XPATH, xpath)
        elem.click()

    def element_request(self):
        request = self.browser.find_element(By.CSS_SELECTOR, '[data-key="url"]')
        return request.text

    def response_code(self):
        code = self.browser.find_element(By.CSS_SELECTOR, '[data-key="response-code"]')
        return code.text

    def response_content(self):
        content = self.browser.find_element(By.CSS_SELECTOR, '[data-key="output-response"]')
        return content.text
