from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

class CreateEventPage:
    def __init__(self, driver):
        self.driver = driver
        self.event_name_input = (By.ID, 'name')
        self.location_input = (By.ID, 'location')
        self.date_input = (By.ID, 'date')
        self.time_input = (By.ID, 'time')
        self.create_button = (By.XPATH, '//button[contains(text(),"Create")]')

    def enter_event_name(self, event_name):
        self.driver.find_element(*self.event_name_input).send_keys(event_name)

    def enter_location(self, location):
        self.driver.find_element(*self.location_input).send_keys(location)

    def enter_date(self, date):
        self.driver.find_element(*self.date_input).send_keys(date)

    def enter_time(self, time):
        self.driver.find_element(*self.time_input).send_keys(time)
        self.driver.find_element(*self.time_input).send_keys(Keys.ARROW_UP)

    def click_create_button(self):
        self.driver.find_element(*self.create_button).click()
