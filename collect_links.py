# collect_links.py
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

def collect_links(base_url: str = "https://distill.pub/") -> list:
    chrome_options = Options()
    chrome_options.add_argument("--headless=new")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    driver = webdriver.Chrome(options=chrome_options)
    driver.get(base_url)
    time.sleep(3)
    elements = driver.find_elements(By.XPATH, "//h2")
    links = []
    for el in elements:
        parent = el.find_element(By.XPATH, "./ancestor::a[1]")
        href = parent.get_attribute("href")
        if href:
            links.append(href)
    driver.quit()
    return links
