
import requests
from bs4 import BeautifulSoup
import os
import telebot

USERNAME = os.getenv("BETONVALUE_USERNAME")
PASSWORD = os.getenv("BETONVALUE_PASSWORD")
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

LOGIN_URL = "https://www.betonvalue.com/en/logmein/"
SUREBETS_URL = "https://www.betonvalue.com/en/tools/surebets"

bot = telebot.TeleBot(TELEGRAM_TOKEN)

def fetch_surebets():
    with requests.Session() as session:
        login = session.post(LOGIN_URL, data={
            "userName": USERNAME,
            "password": PASSWORD
        })
        response = session.get(SUREBETS_URL)
        soup = BeautifulSoup(response.text, "html.parser")
        table = soup.find("table", {"id": "surebet_table"})
        if not table:
            return "Surebet məlumatları tapılmadı."

        rows = table.find_all("tr")[1:]  # Bütün surebetləri al
        messages = []
        for row in rows:
            cols = row.find_all("td")
            if len(cols) >= 7:
                game = cols[0].get_text(strip=True)
                odds1 = cols[2].get_text(strip=True)
                odds2 = cols[4].get_text(strip=True)
                profit = cols[6].get_text(strip=True)
                messages.append(f"{game} | {odds1} vs {odds2} | Profit: {profit}")

        if not messages:
            return "Hazırda surebet yoxdur."
        return "\n".join(messages)

def main():
    try:
        message = fetch_surebets()
        bot.send_message(TELEGRAM_CHAT_ID, message)
    except Exception as e:
        bot.send_message(TELEGRAM_CHAT_ID, f"Xəta baş verdi: {e}")

if __name__ == "__main__":
    main()
