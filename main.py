import os

from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

# Load variables from .env file
load_dotenv()

email = os.getenv("EMAIL")
password = os.getenv("PASSWORD")

options = webdriver.FirefoxOptions()
driver = webdriver.Firefox()
driver.set_window_size(1130, 560)
# driver.get("https://kdp.amazon.com")
# Access create page directly to lessen touchpoints
driver.get("https://kdp.amazon.com/en_US/create")

wait = WebDriverWait(driver, 10)


def login_to_kindle():
    print("Logging in...")
    email_input = driver.find_element(By.XPATH, '//*[@id="ap_email"]')
    email_input.send_keys(email)
    password_input = driver.find_element(By.XPATH, '//*[@id="ap_password"]')
    password_input.send_keys(password)
    signin = driver.find_element(By.XPATH, '//*[@id="signInSubmit"]')
    signin.click()


def create_book():
    element = wait.until(EC.presence_of_element_located((By.XPATH,
                                                         '/html/body/div[1]/div[1]/div[4]/div[2]/div/div[2]/div/div/div[2]/div/div/div/div[4]/div/div[2]/div/span/span/button')))
    element.click()


def details_form():
    print("Populating details form...")
    title_input = driver.find_element(By.XPATH, '//*[@id="data-print-book-title"]')
    title_input.send_keys("Lorem Ipsum")
    author_last_name_input = driver.find_element(By.XPATH, '//*[@id="data-print-book-primary-author-last-name"]')
    author_last_name_input.send_keys("Doe")
    driver.find_element(By.XPATH, '/html/body')


if __name__ == "__main__":
    login_to_kindle()
    # Creates book
    create_book()
    # Populates Paperback Details
    details_form()
