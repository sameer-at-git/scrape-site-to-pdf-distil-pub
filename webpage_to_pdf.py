# webpage_to_pdf.py
import os
import base64
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from datetime import datetime

def webpage_to_pdf(url: str, output_path: str = None) -> str:
    chrome_options = Options()
    chrome_options.add_argument("--headless=new")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])
    chrome_options.add_argument("--log-level=3")

    driver = webdriver.Chrome(options=chrome_options)
    driver.get(url)
    time.sleep(3)

    scroll_height = driver.execute_script("return document.body.scrollHeight")
    px_to_in = 96
    standard_height_in = 11  # standard A4 height
    max_height_in = scroll_height / px_to_in

    pdf_height = min(max_height_in, standard_height_in)

    pdf_data = driver.execute_cdp_cmd("Page.printToPDF", {
        "printBackground": True,
        "paperWidth": 8.5,
        "paperHeight": pdf_height,
        "scale": 1,
        "landscape": False
    })

    if not output_path:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        output_path = os.path.join(os.getcwd(), f"/pdfs/webpage_{timestamp}.pdf")

    with open(output_path, "wb") as f:
        f.write(base64.b64decode(pdf_data['data']))

    driver.quit()
    return output_path
