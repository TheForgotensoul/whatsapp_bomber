import random
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def app(tn, cnt, txt_op, dv=1):
    if dv == 2:
        driver = webdriver.Chrome()
        print("Browser = Chrome")
    else:
        print("Browser = Firefox")
        driver = webdriver.Firefox()
    driver.get("https://web.whatsapp.com/")
    wait = WebDriverWait(driver, 60)
    target = f'"{tn}"'
    print(f"target = {target}")
    print(f"sending {txt_op}, {cnt} times")
    emoji = ['😀', '😃', '😄', '😁', '😆', '😅', '😂', '😊', '😇', '🙂', '🙃', '😉', '😌', '😍', '🥰', '😘',
             '😗', '😙', '😚', '😋', '😛', '😝', '😜', '🤪', '🤨', '🧐', '🤓', '😎', '🤩', '🥳', '😏', '😒', '😞', '😔',
             '😟', '😕', '🙁', '☹️', '😣', '😖', '😫', '😩', '🥺', '😢', '😭', '😤', '😠', '😡', '🤬', '🤯', '😳', '🥵',
             '🥶', '😱', '😨', '😰', '😥', '😓', '🤗', '🤭', '🤫', '🤥', '😶', '😐', '😑', '😬', '🙄', '😯', '😦',
             '😧', '😮', '😲', '🥱', '😴', '🤤', '😪', '😵', '🤐', '🥴', '🤢', '🤮', '🤧', '😷', '🤒', '🤕', '🤑', '🤠',
             '😈', '👿']
    x_arg = '//span[contains(@title,' + target + ')]'
    group_title = wait.until(EC.presence_of_element_located((
        By.XPATH, x_arg)))
    group_title.click()
    inp_xpath = '//*[@id="main"]/footer/div[1]/div[2]/div/div[2]'
    input_box = wait.until(EC.presence_of_element_located((
        By.XPATH, inp_xpath)))
    for i in range(cnt):
        random.shuffle(emoji)
        em = random.choice(emoji)
        if txt_op.lower() == "emoji":
            input_box.send_keys(em)
            print(f"message sent #{i + 1} > {em}")
            input_box.send_keys(Keys.ENTER)
            time.sleep(1)
        else:
            input_box.send_keys(txt_op)
            print(f"message sent #{i + 1} > {txt_op}")
            input_box.send_keys(Keys.ENTER)
            time.sleep(1)


drv = int(input("""
    1 > Firefox
    2 > Chrome
    choose browser: """))

target_name = input("enter the target name or group name: ")
num = int(input("enter the number of times to send the message: "))
txt = input(f"""type the text to send (Remember the names are case sensitive
so type exactly as the contact name...)
            OR
type "emoji" to send random emojis ("Chrome browser does not support emojis"): """)


try:
    app(target_name, num, txt, drv)
except Exception as e:
    print(e)
