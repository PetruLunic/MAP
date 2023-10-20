import time
import pyautogui
import keyboard

def google_search(url):
    camp_google = pyautogui.locateOnScreen(r".\img\google_search_bar.png", confidence=0.7)
    if camp_google is not None:
        pyautogui.click(camp_google)
        time.sleep(1)
        pyautogui.write(url)
        time.sleep(1)
        pyautogui.press('enter')

def youtube_subscribe():
    subscribe_button = pyautogui.locateOnScreen(r".\img\youtube_subscribe_button.png", confidence=0.8)
    if subscribe_button is not None:
        pyautogui.click(subscribe_button)

response = pyautogui.confirm("Doriti sa incepeti rularea programului?", "Confirmare")
if (response == "OK"):
    google_search("https://www.youtube.com/c/ZonaitTvro/videos")
    time.sleep(10)
    youtube_subscribe()
else:
    pyautogui.alert("Ati ales Anulare", "Anulare")