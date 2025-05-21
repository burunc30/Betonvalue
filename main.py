import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def send_message(message):
    print(message)

def login(driver):
    try:
        driver.get("https://www.betonvalue.com/en/login/")
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "username"))).send_keys("burunc")
        driver.find_element(By.NAME, "password").send_keys("131313")
        driver.find_element(By.XPATH, "//button[contains(text(), 'Login')]").click()
        
        # Login sonrası surebets səhifəsinə yönləndiriləcəyini gözləyirik
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
