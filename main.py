from selenium import webdriver
import time



options = webdriver.ChromeOptions()
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_extension("MetaMask.crx")
options.add_argument("--window-size=1920,1080")

driver = webdriver.Chrome(executable_path=r"chromedriver\chromedriver.exe", options=options)
try:
    private =("") # PrivateKey
    passw = ("bkdgsDLGskdg#52kl51") #Пароль от метамаска

    time.sleep(2)
    driver.switch_to.window(driver.window_handles[0])
    driver.get(
        "chrome-extension://nkbihfbeogaeaoehlefnkodbefgpgknn/home.html#initialize/create-password/import-with-seed-phrase")
    time.sleep(1)
    print("Начинаем импортировать ключи и добавлять пароль")
    clu4iki = driver.find_element_by_xpath("//input[@type='password']")
    # clu4iki = driver.find_element_by_xpath("MuiInput-input")
    clu4iki.send_keys(private)
    password1 = driver.find_element_by_id("password")
    password1.send_keys(passw)
    password2 = driver.find_element_by_id("confirm-password")
    password2.send_keys(passw)
    driver.find_element_by_class_name("first-time-flow__terms").click()
    driver.find_element_by_class_name("first-time-flow__button").click()
    print("Были импортированны ключи и добавлен пароль")
    time.sleep(5)
    driver.find_element_by_class_name("btn-primary").click()
    time.sleep(2)
    driver.get("chrome-extension://nkbihfbeogaeaoehlefnkodbefgpgknn/home.html#settings/networks/add-network")
    time.sleep(1)
    elems = driver.find_elements_by_class_name("form-field__input")
    print("Начинаем добавлять сеть Polygon")
    elems[0].send_keys("Smart Chain")
    elems[1].send_keys("https://bsc-dataseed.binance.org/")
    elems[2].send_keys("56")
    elems[3].send_keys("BNB")
    elems[4].send_keys("https://bscscan.com")
    driver.find_element_by_class_name("btn-primary").click()
    print("Сеть BSC добавлена")
    time.sleep(5)
    driver.switch_to.window(driver.window_handles[1])
    driver.get("https://neonearth.io/mini-game/find-hero")
    time.sleep(1)
    driver.find_element_by_xpath("//nav[@id='main-nav']/ul/div/a").click()
    time.sleep(1)
    meta = driver.find_elements_by_class_name("web3modal-provider-container")
    meta[0].click()
    time.sleep(2)
    driver.switch_to.window(driver.window_handles[0])
    driver.refresh()
    driver.refresh()
    driver.get("chrome-extension://nkbihfbeogaeaoehlefnkodbefgpgknn/home.html#")
    time.sleep(1)
    driver.find_element_by_class_name("btn-primary").click()
    time.sleep(1)
    driver.find_element_by_class_name("btn-primary").click()
    time.sleep(1)
    driver.switch_to.window(driver.window_handles[1])
    time.sleep(5)
    play = 0
    while True:
        while 5 > play:
            driver.find_element_by_xpath("//button[@data-key='1']").click()
            time.sleep(0.5)
            driver.find_element_by_xpath("//button[@data-key='4']").click()
            time.sleep(0.5)
            driver.find_element_by_xpath("//button[@data-key='8']").click()
            time.sleep(0.5)
            driver.find_element_by_xpath("//button[@data-key='3']").click()
            time.sleep(0.5)
            driver.find_element_by_xpath("//button[@data-key='11']").click()
            time.sleep(1)
            driver.find_element_by_class_name("btn-primary").click()
            play = play + 1
            print(f"Сыграл: {play} раз")
        else:
            print("Работа всё")
            play = 0
            time.sleep(87000)
            driver.refresh()
            time.sleep(5)



except Exception as ex:
    print(ex)

finally:
    driver.close()
    driver.quit()
