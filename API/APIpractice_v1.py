import requests
import pyautgui


r = requests.get("https://randomfox.ca/floof")

print(r.text)
