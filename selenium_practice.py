from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import csv

driver = webdriver.Chrome()
driver.get("https://data.gov/")
elem = driver.find_element(By.CLASS_NAME, "usa-input")
elem.send_keys("student")
elem.send_keys(Keys.RETURN)

with open('student_related_datasets.csv', mode='w', newline='', encoding='utf-8') as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(['Dataset Name', 'Dataset Link'])

    try:
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "justify-content-center"))
        )

        page_link = element.find_element(By.CLASS_NAME, 'page-link').get_attribute('href')

        for i in range(1,10):
            new_page_link = page_link[:-1] + str(i)
            driver.get(new_page_link)
            time.sleep(3)

            dataset_cards = driver.find_elements(By.CLASS_NAME, 'dataset-content')

            for dataset_card in dataset_cards:
                dataset_name = dataset_card.find_element(By.TAG_NAME, 'a')
                dataset_link = dataset_name.get_attribute('href')
                csv_writer.writerow([dataset_name.text, dataset_link])

        

    finally:
        driver.close()







