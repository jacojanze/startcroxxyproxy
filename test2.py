import os
import zipfile
import requests

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC

# Function to download and extract Chrome driver
def download_and_extract_chromedriver(chrome_driver_url, extract_path):
    # Download Chrome driver zip file
    response = requests.get(chrome_driver_url)
    zip_file_path = os.path.join(extract_path, "chromedriver.zip")
    with open(zip_file_path, 'wb') as zip_file:
        zip_file.write(response.content)

    # Extract Chrome driver
    with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
        zip_ref.extractall(extract_path)

    # Get the path to the extracted Chrome driver
    chrome_driver_path = os.path.join(extract_path, "chromedriver.exe")

    return chrome_driver_path

def getProxyUrl(url):
    # URL to download Chrome driver
    chrome_driver_url = "https://storage.googleapis.com/chrome-for-testing-public/121.0.6167.184/win64/chromedriver-win64.zip"
    
    # Directory to extract Chrome driver
    extract_path = os.path.join(os.getcwd(), "")

    # Download and extract Chrome driver
    chrome_driver_path = download_and_extract_chromedriver(chrome_driver_url, extract_path)

    # Initialize Chrome driver with Selenium
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # To run Chrome in headless mode
    service = Service(chrome_driver_path)
    driver = webdriver.Chrome(service=service, options=chrome_options)

    driver.get("https://64.227.120.231/")

    driver.implicitly_wait(1)

    text_box = driver.find_element(by=By.NAME, value="url")
    text_box.send_keys(url)

    text_box.send_keys(Keys.RETURN)

    x = 0

    # Wait for two redirects
    redirect_count = 0
    while redirect_count < 1:
        current_url = driver.current_url
        WebDriverWait(driver, 10).until(EC.url_changes(current_url))
        redirect_count += 1

    proxyUrl = driver.current_url

    driver.quit()

    return proxyUrl

if __name__ == '__main__':
    url = input("Enter URL: ")
    proxy_url = getProxyUrl(url)
    print("Proxy URL:", proxy_url)
