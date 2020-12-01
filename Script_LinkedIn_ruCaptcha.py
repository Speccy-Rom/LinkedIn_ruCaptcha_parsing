from selenium.common.exceptions import NoSuchElementException
from selenium import webdriver
from selenium.webdriver.common.keys import Keys



TEXTMESSAGE = """Привет. Нашел тебя в своих контактах. Может тебе будет интересно поработать преподавателем на 
онлайн-курсах по питону. Ссылка на вакансию: <ТУТ> """
SEARCH_LINK = 'https://www.linkedin.com/uas/login?session_redirect=https%3A%2F%2Fwww%2Elinkedin%2Ecom%2Fsearch' \
              '%2Fresults%2Fpeople%2F%3FfacetGeoUrn%3D%255B%2522101728296%2522%252C%2522102264497%2522%255D' \
              '%26keywords%3Djunior%2520python%26origin%3DFACETED_SEARCH%26page%3D2&fromSignIn=true&trk' \
              '=cold_join_sign_in '
def open_links_by_browser(driver, link):
    driver.get(link)
    driver.quit()
driver = webdriver.Chrome("/usr/lib/chromium-browser/chromedriver")
driver.get(LINK)
email_field = driver.find_element_by_css_selector('#username')
password_field = driver.find_element_by_css_selector('#password')
submit_button = driver.find_element_by_css_selector('.btn__primary--large')
email_field.send_keys('YOUEMAIL@gmail.com')
password_field.send_keys('YOUR_PASSWORD')
submit_button.click()