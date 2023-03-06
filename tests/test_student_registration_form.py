import pytest
from selene import be, by, have
from selene.support.shared import browser
from selenium.webdriver import Keys

TEST_URL = 'https://demoqa.com/automation-practice-form'


@pytest.fixture
def configured_browser():
    browser.config.window_width = 1980
    browser.config.window_height = 1080
    browser.config.click_by_js = True
    return browser


def test_1_positive(configured_browser):
    browser.open(TEST_URL)
    browser.element(by.id('firstName')).should(be.blank).type('Oleg')
    browser.element(by.id('lastName')).should(be.blank).type('Greckiy')
    browser.element(by.id('userEmail')).should(be.blank).type('GreckiyOleg@gmail.com')
    browser.element('[for="gender-radio-1"]').should(be.clickable).click()
    browser.element(by.id('userNumber')).should(be.clickable).type('1234567890')
    browser.element(by.id('dateOfBirthInput')
                    ).send_keys(Keys.CONTROL, 'a').type('16 Jan 1991').send_keys(Keys.ENTER)
    browser.element(by.id('subjectsInput')).should(be.clickable).type('Maths').send_keys(Keys.ENTER)
    browser.element(by.id('hobbies-checkbox-1')).should(be.existing).click()
    browser.element(by.id('uploadPicture')).set_value('D:\\Oleg.jpg')
    browser.element(by.id('currentAddress')).should(be.blank).type('221B Baker Street')
    browser.element(by.id('react-select-3-input')).set_value('NCR').send_keys(Keys.ENTER)
    browser.element(by.id('react-select-4-input')).set_value('Delhi').send_keys(Keys.ENTER)
    browser.element(by.id('submit')).should(be.clickable).click()

    assert browser.element(by.id('example-modal-sizes-title-lg')
                           ).should(have.text('Thanks for submitting the form'))
