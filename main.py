import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

def main():
    # Chrome üçün başsız (headless) rejimi aktiv et
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--disable-gpu")

    # WebDriver yarat
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)

    try:
        # BetOnValue Surebet səhifəsinə keç
        driver.get("https://www.betexplorer.com/surebets/")  # Nümunə URL (əgər başqadırsa dəyiş)
        time.sleep(5)  # Səhifənin tam yüklənməsi üçün gözlə

        # Məsələn, surebet cədvəlindən məlumat çək
        surebets = driver.find_elements(By.CLASS_NAME, "some-surebet-class")  # Burada class adı düzgün olmalıdır
        for bet in surebets:
            print(bet.text)

    except Exception as e:
        print("Xəta baş verdi:", e)

    finally:
        driver.quit()

if __name__ == "__main__":
    main()
