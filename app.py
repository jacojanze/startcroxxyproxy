from flask import Flask, jsonify, request
from flask_cors import CORS

import os

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC




def getProxyUrl(url):
    # Path to chromedriver executable
    chrome_driver_path = '/driver/chromedriver'

    # Initialize Chrome driver with Selenium
    chrome_options = Options()
    # chrome_options.add_argument("--headless")  # To run Chrome in headless mode
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

    # while not ("/__cpi.php?s=" in driver.current_url):
        # pass

    proxyUrl = driver.current_url

    driver.quit()

    return proxyUrl


app = Flask(__name__)
CORS(app)

@app.route('/proxy')
def hello_world():
    url = getProxyUrl(request.args.get('url'))
    return jsonify({"proxyUrl": url})

if __name__ == '__main__':
    app.run(debug=True)



# from flask import Flask, jsonify, request
# from flask_cors import CORS

# import os
# import zipfile
# import requests
# import tempfile

# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.support import expected_conditions as EC

# # Function to download and extract Chrome driver
# def download_and_extract_chromedriver(chrome_driver_url):
    # # Download Chrome driver zip file
    # with tempfile.NamedTemporaryFile(delete=False) as temp_zip_file:
        # response = requests.get(chrome_driver_url)
        # temp_zip_file.write(response.content)

    # # Extract Chrome driver to /tmp directory
    # with zipfile.ZipFile(temp_zip_file.name, 'r') as zip_ref:
        # extracted_path = tempfile.mkdtemp()
        # zip_ref.extractall(extracted_path)

    # # Find the extracted Chrome driver path
    # chrome_driver_path = os.path.join(extracted_path, "chromedriver")

    # return chrome_driver_path

# def getProxyUrl(url):
    # # URL to download Chrome driver
    # chrome_driver_url = "https://storage.googleapis.com/chrome-for-testing-public/121.0.6167.184/linux64/chrome-linux64.zip"
    
    # # Download and extract Chrome driver
    # chrome_driver_path = download_and_extract_chromedriver(chrome_driver_url)

    # # Initialize Chrome driver with Selenium
    # chrome_options = Options()
    # # chrome_options.add_argument("--headless")  # To run Chrome in headless mode
    # service = Service(chrome_driver_path)
    # driver = webdriver.Chrome(service=service, options=chrome_options)

    # driver.get("https://64.227.120.231/")

    # driver.implicitly_wait(1)

    # text_box = driver.find_element(by=By.NAME, value="url")
    # text_box.send_keys(url)

    # text_box.send_keys(Keys.RETURN)

    # x = 0

    # # Wait for two redirects
    # redirect_count = 0
    # while redirect_count < 1:
        # current_url = driver.current_url
        # WebDriverWait(driver, 10).until(EC.url_changes(current_url))
        # redirect_count += 1

    # proxyUrl = driver.current_url

    # driver.quit()

    # return proxyUrl

# app = Flask(__name__)
# CORS(app)

# @app.route('/proxy')
# def hello_world():
    # url = getProxyUrl(request.args.get('url'))
    # return jsonify({"proxyUrl": url})

# if __name__ == '__main__':
    # app.run(debug=True)
