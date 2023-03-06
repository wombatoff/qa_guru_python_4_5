import os

import pytest
from selene import be, by, have
from selene.support.shared import browser
from selenium.webdriver import Keys

TEST_URL = 'https://demoqa.com/automation-practice-form'
TEST_NAME = 'Oleg'
TEST_LAST_NAME = 'Greckiy'
TEST_EMAIL = 'GreckiyOleg@gmail.com'
TEST_USER_NUMBER = '1234567890'
TEST_DATE_OF_BIRTH = '16 Jan 1991'
TEST_SUBJECT = 'Maths'
TEST_ADDRESS = '221B Baker Street'
TEST_STATE = 'NCR'
TEST_CITY = 'Delhi'

TEST_PICTURE = os.getcwd() + r'\tests\data\Oleg.jpg'


@pytest.fixture
def configured_browser():
    browser.config.window_width = 1980
    browser.config.window_height = 1080
    browser.config.click_by_js = True
    return browser


def test_registration_form(configured_browser):
    # Fill form
    browser.open(TEST_URL)
    browser.element(by.id('firstName')).type(TEST_NAME)
    browser.element(by.id('lastName')).type(TEST_LAST_NAME)
    browser.element(by.id('userEmail')).type(TEST_EMAIL)
    browser.element(by.id('gender-radio-1')).click()
    browser.element(by.id('userNumber')).type(TEST_USER_NUMBER)
    browser.element(by.id('dateOfBirthInput')
                    ).send_keys(Keys.CONTROL, 'a').type(TEST_DATE_OF_BIRTH).send_keys(Keys.ENTER)
    browser.element(by.id('subjectsInput')).type(TEST_SUBJECT).send_keys(Keys.ENTER)
    browser.element(by.id('hobbies-checkbox-1')).click()
    browser.element(by.id('uploadPicture')).set_value(TEST_PICTURE)
    browser.element(by.id('currentAddress')).type(TEST_ADDRESS)
    browser.element(by.id('react-select-3-input')).set_value(TEST_STATE).send_keys(Keys.ENTER)
    browser.element(by.id('react-select-4-input')).set_value(TEST_CITY).send_keys(Keys.ENTER)

    # Submit form
    browser.element(by.id('submit')).click()

    # Check form
    browser.element(by.xpath('//td[contains(text(), "Student Name")]/following-sibling::td[1]')
                    ).should(have.text(f'{TEST_NAME} {TEST_LAST_NAME}'))
    browser.element(by.xpath('//td[contains(text(), "Student Email")]/following-sibling::td[1]')
                    ).should(have.text(TEST_EMAIL))
    browser.element(by.xpath('//td[contains(text(), "Gender")]/following-sibling::td[1]')
                    ).should(have.text('Male'))
    browser.element(by.xpath('//td[contains(text(), "Mobile")]/following-sibling::td[1]')
                    ).should(have.text(TEST_USER_NUMBER))
    browser.element(by.xpath('//td[contains(text(), "Date of Birth")]/following-sibling::td[1]')
                    ).should(have.text('16 January,1991'))
    browser.element(by.xpath('//td[contains(text(), "Subjects")]/following-sibling::td[1]')
                    ).should(have.text(TEST_SUBJECT))
    browser.element(by.xpath('//td[contains(text(), "Hobbies")]/following-sibling::td[1]')
                    ).should(have.text('Sports'))
    browser.element(by.xpath('//td[contains(text(), "Picture")]/following-sibling::td[1]')
                    ).should(have.text('Oleg.jpg'))
    browser.element(by.xpath('//td[contains(text(), "Address")]/following-sibling::td[1]')
                    ).should(have.text(TEST_ADDRESS))
    browser.element(by.xpath('//td[contains(text(), "State and City")]/following-sibling::td[1]')
                    ).should(have.text(f'{TEST_STATE} {TEST_CITY}'))
