from selene import browser, have, be, by
import os


def test_complete_todo():
    browser.open('/')
    if browser.element(by.text('Соглашаюсь')).matching(be.visible):
        browser.element(by.text('Соглашаюсь')).click()
    browser.driver.execute_script("document.querySelector('.body-height').style.transform='scale(.50)'")
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
    browser.element('[for="hobbies-checkbox-1"]').click()
    browser.element('#uploadPicture.form-control-file').send_keys(os.path.abspath('2.jpg'))
    browser.element('#currentAddress').should(be.blank).type('Via Nemorense, 100')
    browser.element('#state').should(be.clickable).click()
    browser.element(by.text('Uttar Pradesh')).should(be.clickable).click()
    browser.element('#city').should(be.clickable).click()
    browser.element(by.text('Lucknow')).should(be.clickable).click()
    browser.element('#submit').click()

    browser.element('.table-responsive').all('td:nth-child(2)').should(have.texts(
        'Zarina Ansar',
        'zari12@gmail.com',
        'Female',
        '7778234566',
        '05 June,1999',
        'Physics',
        'Sports',
        '2.jpg',
        'Via Nemorense, 100',
        'Uttar Pradesh Lucknow'
    ))


