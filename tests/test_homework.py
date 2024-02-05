from selene import browser, have, be, by
import os


def test_complete_todo():
    browser.open('/')
    if browser.element(by.text('Соглашаюсь')).matching(be.visible):
        browser.element(by.text('Соглашаюсь')).click()
    browser.element('#firstName').should(be.blank).type('Zarina')
    browser.element('#lastName').should(be.blank).type('Ansar')
    browser.element('#userEmail').should(be.blank).type('zari12@gmail.com')
    browser.element('[for="gender-radio-2"]').click()
    browser.element('#userNumber').should(be.blank).type('7778234566')
    browser.element('#dateOfBirthInput').should(be.visible).click()
    browser.element('.react-datepicker__month-select').element('[value="5"]').click()
    browser.element('.react-datepicker__year-select').element('[value="1999"]').click()
    browser.element('.react-datepicker__day--005').click()
    browser.element('#subjectsInput').should(be.blank).type('Physics').press_enter()
    browser.element('#subjectsInput').type('Maths').press_enter()
    browser.element('[for="hobbies-checkbox-1"]').click()
