"/surebets")]')))
        send_message("Login uÄŸurla tamamlandÄ±.")
        return True

    except Exception as e:
        send_message(f"Login zamanÄ± xÉ™ta baÅŸ verdi: {e}")
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
            send_message("Surebet mÉ™lumatlarÄ± tapÄ±lmadÄ±.")
        else:
            send_message("Surebet tapÄ±ldÄ±. ÆtraflÄ± yoxlanmalÄ±dÄ±r.")
    except Exception as e:
        send_message(f"Surebet sÉ™hifÉ™sindÉ™ xÉ™ta baÅŸ verdi: {e}")
    finally:
        driver.quit()

if __name__ == "__main__":
    main()
