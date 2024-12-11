import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from pages.create_event_page import CreateEventPage
from pages.event_page import EventPage

URL = 'https://sharrine8.github.io/code-jam_react/#/events'
event_details = {
    'event_name': 'Thanksgiving',
    'location': 'New Jersey',
    'date': '12/07/2024',
    'time': '09:49',
    'dish_names': ['Wolibah', 'Salad', 'Pie','Pizza', 'Kebab', 'Doner','HelalGuys',
                   'Boritto', 'Rolls','Donuts', 'Cakes', 'Baklava'],
    'names': ['Berkuk', 'Alex', 'Deniz','Lizbeth', 'Alex', 'Aydin','Hasan', 'Asim',
              'Sijan','Nahide', 'Ali', 'Meliha']
}
@pytest.fixture(scope="module")
def create_event_page(driver):
    create_event_page = CreateEventPage(driver)
    yield create_event_page

@pytest.fixture(scope="module")
def event_page(driver):
    event_page = EventPage(driver)
    yield event_page

@pytest.fixture(scope="module")
def driver():
    driver = webdriver.Chrome()
    driver.implicitly_wait(4)
    driver.wait = WebDriverWait(driver, 10)
    yield driver
    driver.quit()

def test_create_event(driver, create_event_page, event_page):
    driver.get(URL)

    create_event_page.enter_event_name(event_details['event_name'])
    create_event_page.enter_location(event_details['location'])
    create_event_page.enter_date(event_details['date'])
    create_event_page.enter_time(event_details['time'])
    create_event_page.click_create_button()

    assert event_page.get_event_name() == event_details['event_name']
    assert event_page.get_event_location().endswith(event_details['location'])
    parsed_created_event_date = event_page.get_event_date().replace('Date: ', '')
    sorted_created_event_date = sorted(parsed_created_event_date.split('-'))
    parsed_date = sorted(event_details['date'].split('/'))
    assert sorted_created_event_date == parsed_date
    parsed_created_event_time = event_page.get_event_time().replace('Time: ', '')
    assert parsed_created_event_time == event_details['time']

def test_add_dish(driver, event_page):

    for dish_name, name in zip(event_details['dish_names'], event_details['names']):
        event_page.enter_dish_name(dish_name)
        event_page.enter_your_name(name)
        event_page.click_add_dish_button()
    for index, dish_name in enumerate(event_details['dish_names']):
        displayed_dish_name = event_page.get_displayed_dish_names(index)
        assert dish_name == displayed_dish_name
    pass
