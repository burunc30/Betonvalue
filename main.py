from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
import telegram

USERNAME = "burunc"
PASSWORD = "131313"
TELEGRAM_TOKEN = "8106341353:AAFIi3nfPOlydtCM_eYHiSIbDR0C1RFoaG4"
TELEGRAM_CHAT_ID = "1488455191"

def fetch_surebets():
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    driver = webdriver.Chrome(options=options)

    try:
        driver.get("https://www.betonvalue.com/sign-in/")
        time.sleep(3)

        # Tap və daxil et
        username_input = driver.find_element(By.NAME, "username")
        password_input = driver.find_element(By.NAME, "password")
        login_button = driver.find_element(By.XPATH, "//button[@type='submit']")

        username_input.send_keys(USERNAME)
        password_input.send_keys(PASSWORD)
        login_button.click()
        time.sleep(5)

        # Surebet səhifəsinə keç
        driver.get("https://www.betonvalue.com/en/tools/surebets")
        time.sleep(5)

        # Surebet cədvəlini oxu
        rows = driver.find_elements(By.CSS_SELECTOR, "table#surebet_table tbody tr")
        messages = []
        for row in rows:
            cols = row.find_elements(By.TAG_NAME, "td")
            if len(cols) >= 7:
                game = cols[0].text.strip()
                odds1 = cols[2].text.strip()
                odds2 = cols[4].text.strip()
                profit = cols[6].text.strip()
                messages.append(f"{game} | {odds1} vs {odds2} | Profit: {profit}")

        return "\n".join(messages) if messages else "Hazırda surebet yoxdur."

    except Exception as e:
        return f"Xəta baş verdi: {e}"
    finally:
        driver.quit()

def send_to_telegram(message):
    bot = telegram.Bot(token=TELEGRAM_TOKEN)
    bot.send_message(chat_id=TELEGRAM_CHAT_ID, text=message)

if __name__ == "__main__":
    msg = fetch_surebets()
    send_to_telegram(msg)
