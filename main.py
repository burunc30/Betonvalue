import time
import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def send_message(message):
    token = "8106341353:AAFIi3nfPOlydtCM_eYHiSIbDR0C1RFoaG4"
    chat_id = "1488455191"
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    data = {"chat_id": chat_id, "text": message}
    try:
        response = requests.post(url, data=data)
        if response.status_code != 200:
            print(f"Telegram xətası: {response.text}")
    except Exception as e:
        print(f"Telegram mesaj xəta: {e}")

def login(driver):
    try:
        driver.get("https://www.betonvalue.com/en/login/")
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "username"))).send_keys("burunc")
        driver.find_element(By.NAME, "password").send_keys("131313")
        driver.find_element(By.XPATH, "//button[contains(text(), 'Login')]").click()
        
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//a[contains(@href, '/surebets')]")))

        send_message("Login uğurla tamamlandı.")
        return True
    except Exception as e:
        send_message(f"Login zamanı xəta baş verdi: {e}")
        return False

def main():
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(options=chrome_options)

    if not login(driver):
        driver.quit()
        return

    try:
        driver.get("https://www.betonvalue.com/en/surebets/")
        time.sleep(3)
        page_source = driver.page_source

        if "No surebets found" in page_source or "0 surebets" in page_source:
            send_message("Surebet məlumatları tapılmadı.")
        else:
            send_message("Surebet tapıldı. Ətraflı yoxlanmalıdır.")
    except Exception as e:
        send_message(f"Surebet səhifəsində xəta baş verdi: {e}")
    finally:
        driver.quit()

if __name__ == "__main__":
    main()
