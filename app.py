import random
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait


def app(tn, cnt, txt_op, dv=1):
    if dv == 2:
        print("Browser = Chrome")
        print("""[INFO] Initializing the browser..... 
        Scan the QR code to continue.....""")
        driver = webdriver.Chrome()
    else:
        print("Browser = Firefox")
        print("""[INFO] Initializing the browser..... 
        Scan the QR code to continue.....""")
        driver = webdriver.Firefox()

    driver.get("https://web.whatsapp.com/")
    wait = WebDriverWait(driver, 60)
    target = f'"{tn}"'
    emoji = ['😀', '😃', '😄', '😁', '😆', '😅', '😂', '😊', '😇', '🙂', '🙃', '😉', '😌', '😍', '🥰', '😘',
             '😗', '😙', '😚', '😋', '😛', '😝', '😜', '🤪', '🤨', '🧐', '🤓', '😎', '🤩', '🥳', '😏', '😒', '😞', '😔',
             '😟', '😕', '🙁', '☹️', '😣', '😖', '😫', '😩', '🥺', '😢', '😭', '😤', '😠', '😡', '🤬', '🤯', '😳', '🥵',
             '🥶', '😱', '😨', '😰', '😥', '😓', '🤗', '🤭', '🤫', '🤥', '😶', '😐', '😑', '😬', '🙄', '😯', '😦',
             '😧', '😮', '😲', '🥱', '😴', '🤤', '😪', '😵', '🤐', '🥴', '🤢', '🤮', '🤧', '😷', '🤒', '🤕', '🤑', '🤠',
             '😈', '👿']
    x_arg = '//span[contains(@title,' + target + ')]'
    group_title = wait.until(ec.presence_of_element_located((
        By.XPATH, x_arg)), message="QR code not scanned program terminated..")
    group_title.click()
    inp_xpath = '//*[@id="main"]/footer/div[1]/div[2]/div/div[2]'
    input_box = wait.until(ec.presence_of_element_located((
        By.XPATH, inp_xpath)))
    print(f"target = {target}")
    print(f"sending {txt_op}, {cnt} times")
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
            print(f"Message sent #{i + 1} > {txt_op}")
            input_box.send_keys(Keys.ENTER)
            time.sleep(1)
    print("Task completed Successfully...")


try:
    drv = int(input("""
        1 > Firefox
        2 > Chrome
        choose browser: """))

    target_name = input("""
    enter the target name or group name
    (Remember the names are case sensitive so type exactly as the contact name...): """)
    num = int(input("enter the number of times to send the message: "))
    if num != 0:
        txt = input(f"""type the text to send 
                    OR
        type "emoji" to send random emojis ("Chrome browser does not support emojis"): """)
        app(target_name, num, txt, drv)
    else:
        print("\nProgram terminated...Enter a valid number of times to send a message")

except ValueError as v:
    print("\nOnly numbers are accepted")
except KeyboardInterrupt as k:
    print(f"\nProgram terminated by {k}")
except Exception as e:
    open(e)
finally:
    print("\nRerun the program")
