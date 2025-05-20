from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

print("BOT BAŞLADI")

# Chrome üçün headless konfiqurasiya
options = Options()
options.add_argument("--headless=new")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--no-sandbox")

# Driver başlat
driver = webdriver.Chrome(options=options)

try:
    # Sayta keçid et
    driver.get("https://www.betonvalue.com")
    time.sleep(5)
    
    print("Sayt açıldı:", driver.title)

    # Burada sadəcə saytı açırıq. Əlavə scraping kodlarını sən əlavə edəcəksən
    # Məsələn:
    surebet_elements = driver.find_elements(By.CLASS_NAME, "surebet-row")
    if surebet_elements:
        print(f"{len(surebet_elements)} surebet tapıldı.")
    else:
        print("Surebet məlumatı tapılmadı.")
    
except Exception as e:
    print("Xəta baş verdi:", e)

finally:
    driver.quit()
