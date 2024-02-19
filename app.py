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
    # Initialize Chrome driver with Selenium
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    driver = webdriver.Chrome(options=chrome_options)

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
