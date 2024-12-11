from selenium.webdriver.common.by import By

class EventPage:
    def __init__(self, driver):
        self.driver = driver
        self.event_name = (By.XPATH, '//h1[@class="my-event__title"]')
        self.event_location = (By.XPATH, '//p[@class="my-event__subtitle" and contains(text(),"Location")]')
        self.event_date = (By.XPATH, '//p[@class="my-event__subtitle" and contains(text(),"Date")]')
        self.event_time = (By.XPATH, '//p[@class="my-event__subtitle" and contains(text(),"Time")]')
        self.dish_name_input = (By.XPATH, '//input[@name="title"]')
        self.enter_your_name_input = (By.XPATH, '//input[@name="name"]')
        self.add_dish_button = (By.XPATH, '//button[contains(text(),"Add")]')
        self.displayed_dish_names = (By.XPATH, '//h4[@class="menu-section__menu-name"]')
        self.displayed_names = (By.XPATH, '//p[@class="menu-section__chef-name"]')

    def get_event_name(self):
        return self.driver.find_element(*self.event_name).text

    def get_event_location(self):
        return self.driver.find_element(*self.event_location).text

    def get_event_date(self):
        return self.driver.find_element(*self.event_date).text

    def get_event_time(self):
        return self.driver.find_element(*self.event_time).text

    def enter_dish_name(self, dish_name):
        self.driver.find_element(*self.dish_name_input).send_keys(dish_name)

    def enter_your_name(self, name):
        self.driver.find_element(*self.enter_your_name_input).send_keys(name)

    def click_add_dish_button(self):
        self.driver.find_element(*self.add_dish_button).click()

    def get_displayed_dish_names(self, index):
        displayed_dish_names = self.driver.find_elements(*self.displayed_dish_names)
        return displayed_dish_names[index].text