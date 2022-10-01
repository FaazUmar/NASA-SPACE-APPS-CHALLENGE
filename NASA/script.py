from curses.ascii import HT
from email import message
from requests_html import HTMLSession
import subprocess
import time
from playsound import playsound
import tkinter as tk



def weather(name):
  count = 0
  while True:
    count += 1 
    class data():
      s = HTMLSession()
      url = 'https://www.spaceweather.com/'

      r = s.get(url, headers={'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.3 Safari/605.1.15'})

      q = (r.html.find('span.solarWindText', first=True).text)

    string = data.q
    result = " ".join(line.strip() for line in string.splitlines())

    l = list(result)

    speedtxt = "".join(l[:31])
    speed = float(speedtxt[19:24])

    l[31]='D'
    density = "".join(l[31:])

    d = speedtxt + '\n' + density


    CMD = '''
    on run argv
      display notification (item 2 of argv) with title (item 1 of argv)
    end run
    '''
    
    def notify(title, text):
      subprocess.call(['osascript', '-e', CMD, title, text])

    notify("Current space weather: ", d)

    if speed < 600:
      playsound('normal.mp3')
    elif speed > 599.0 :
      playsound('danger.mp3')
    
    name.iconify()
    if count == 48:
      exit()
    time.sleep(1800)


  









