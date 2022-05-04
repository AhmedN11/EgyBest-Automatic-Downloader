import os
import requests
from bs4 import BeautifulSoup
import json
from time import sleep
from msedge.selenium_tools import Edge, EdgeOptions
import webbrowser
from selenium import webdriver






# defining the function that takes care of the download after you choose what to download

def download(link) :

  # defining some technical stuff nobody has to know about

  options = EdgeOptions()
  options.use_chromium = True
  options.add_argument("headless")
  options.add_argument("disable-gpu")
  options.add_argument("--log-level=0")
  options.add_argument("--mute-audio")
  try :
      driver = Edge(executable_path = os.getcwd() + '\\Desktop\\EGYBEST\\msedgedriver.exe', options=options)
  except :
      from selenium.webdriver.chrome.options import Options
      chrome_options = Options()
      chrome_options.add_argument("--mute-audio")
      chrome_options.add_argument("--disable-extensions")
      chrome_options.add_argument("--disable-gpu")
      chrome_options.add_argument("--headless")
      driver = webdriver.Chrome(executable_path = os.getcwd() + '\\Desktop\\EGYBEST\\chromedriver.exe', options=chrome_options)



  # visiting the link and looking for the download website

  print("\n\n> Gathering the download link, please wait : \n")
  driver.get(link)

  driver.find_element_by_xpath(f'//*[@id="watch_dl"]/table/tbody/tr[{quality}]/td[4]/a[1]').click()
  sleep(waiting)
  driver.get( link.replace('?ref=search-p1', '?refresh=1'))
  sleep(waiting)
  driver.find_element_by_xpath('//*[@id="mainLoad"]/div/a').click()
  sleep(waiting)
  driver.find_element_by_xpath('//*[@id="mainLoad"]/div/a').click()
  sleep(waiting)
  driver.get(link)
  sleep(waiting + 3)
  driver.get('https://seen.egybest.ltd' + driver.find_element_by_xpath(f'//*[@id="watch_dl"]/table/tbody/tr[{quality}]/td[4]/a[1]').get_attribute('data-url'))
  sleep(waiting)
  driver.find_element_by_xpath('/html/body/div[1]/div/p/a[1]').click()
  sleep(waiting + 3)
  dl = driver.find_element_by_xpath('/html/body/div[1]/div/p/a[1]').get_attribute('href').strip()


  print("\n\nDownload link Found !\n")

  driver.quit()


  webbrowser.register('edge', None, webbrowser.BackgroundBrowser("C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe"))
  browser = webbrowser.get('edge')
  if browser.open('about:blank') :
    sleep(4)
    browser.open(dl)
  else :
    webbrowser.register('chrome', None, webbrowser.BackgroundBrowser("C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"))
    browser = webbrowser.get('chrome')
    browser.open('about:blank')
    sleep(4)
    browser.open(dl)


  return



# THE WAITING PARAMETER COMES HANDY IS YOU HAVE A BIT SLOWER INTERNET SPEED

waiting = int(input("Enter loading page waiting time (default is 2, increase if you have slow internet, hit enter to skip) : ") or "2")


choice = 0
while choice == 0 :
  showtitles, showlinks = [], []

  # REQUESTING WHAT TO LOOK FOR ON EGYBEST AND TAKING A CHOICE

  name = input("\n> What Movie/Show/Anime you're looking for : ")
  

  url = f"https://seen.egybest.ltd/explore/?page=1&output_format=json&q={name}"
  headers = {
    'authority': 'seen.egybest.ltd',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="96", "Google Chrome";v="96"',
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'x-requested-with': 'XMLHttpRequest',
    'sec-ch-ua-mobile': '?0',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/5waiting7.waiting6 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/5waiting7.waiting6',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer': f'https://seen.egybest.ltd/explore/?q={name}',
    'accept-language': 'fr-FR,fr;q=0.9,en-US;q=0.8,en;q=0.7',
    'cookie': 'EGUDI=Skwaiting516waiting98644waiting7zeuu.e80dbd59dfacafcbffb00e5bf6ea5c8406462fba0a147b042125ede7waiting65waitingdcewaiting7cf6c8e087cb809cwaitingwaiting752b2c8ce1a112d774f927waiting01d01920405fd5811244aca; PSSID=OafJrlnFuJeC0S5NX226h6uqjBFcaH2Qjk1GnIZx4PP9BXyFwA4OwlGD5GIrp27SlDKVuBGA0xmf7EWRmpx6IxUz46UGEewaitingwkmmQnBo7u89SjFAQ1WMbPIZti%2CQvLYoH; waiting24e9a7c=MvvvVKTkzYrVvWXUcXWXIBXcXUXWBXXWVvVGpovVvWvVXPviZXvzFXmBXafkURvVWVvVopfevVvWvVigwXvzBWFZBVCdvVvc-1b69e62a5waitingea7eef8d0100waiting62c6dc1c6; __cf_bm=mKO8fYLVp4kH7tiLyOS0rEe_pDvFdxC64gKo.7fqXrw-1640861waiting8waiting-0-AfOhATOrCfVDPFfGCoBmAUYGBn7Ji4waitingvswaovilSb0hfGdeH1eMH5VRUIVxH4TOj5pFHSxdxr/jcbJOUEnMw8tM=; JS_TIMEZONE_OFFSET=-waiting600; OUAMgwaitingmBI5MGMY8CX=1F4GgG9WUSAvsqXKWNWPTBKfpQhGJwwaitinghLRVkzOENEgprP2eMISPfUGD6UuoR; push_subscribed=ignore'
  }
  data = BeautifulSoup(json.loads(requests.get(url, headers=headers).text)['html'], 'lxml').findAll('a', {'class' : 'movie'})

  for show in data :
    showlink = 'https://seen.egybest.ltd' + show['href']
    showtitle = show.find('span', {'class' : 'title'}).text
    showlinks.append(showlink)
    showtitles.append(showtitle)
    print(f"{showtitles.index(showtitle) + 1} - {showtitle} : {showlink}")
  print("0 - Search again")
  choice = int(input('> Choose a Movie/Show/Anime : '))


# SHOWING THE AVAILABLE SEASONS IF IT'S A SERIE AND TAKING A CHOICE IF APPLICABLE

print('\n')
if "/series/" in showlinks[choice - 1] :
  seasons = BeautifulSoup(requests.get(showlinks[choice - 1]).text, 'lxml').find('div', {'class' : 'contents movies_small'}).findAll('a')
  c = 0
  seasontitles, seasonlinks = [], []
  for season in seasons[-1:-len(seasons)-1:-1] :
    seasonlink = season['href']
    seasontitle = season.find('span', {'class' : 'title'}).text
    seasonlinks.append(seasonlink)
    seasontitles.append(seasontitle)
    c += 1
    print(f"{c} - Season {c} : {seasonlink}")

  schoice = int(input('> Choose a season : '))


  # SHOWING THE EPISODES OF THE CHOSEN SEASON AND TAKING A CHOICE

  print('\n')
  eps = BeautifulSoup(requests.get(seasonlinks[schoice - 1]).text, 'lxml').find('div', {'class' : 'movies_small'}).findAll('a')
  c = 0
  eplinks, eptitles = [], []
  for ep in eps[-1:-len(eps)-1:-1] :
    c += 1
    eplink = ep['href']
    eptitle = ep.find('span', {'class' : 'title'}).text
    eplinks.append(eplink)
    eptitles.append(eptitle)
    print(f"{c} - Ep {c} : {eplink}")
  c += 1
  print(f"{c} - Download all episodes")

  epchoice = int(input('> Choose an episode : '))


  # SHOWING AVAILABLE QUALITITES AND TAKING A CHOICE

  try :
    
    qualities = BeautifulSoup(requests.get(eplinks[epchoice - 1]).text, 'lxml').find('tbody').findAll('tr')
    print("\n> CHOOSE A QUALITY : ")

    for w in range(0, len(qualities)) :
      print(f'\t {w + 1} - ' + qualities[w].findAll('td')[1].text + ' : ' + qualities[w].findAll('td')[2].text)
    

    quality = int(input('> '))
    download(eplinks[epchoice - 1])
  
  except :
    print("DOWNLOADING ALL EPISODES")
    print("\n> CHOOSE ONE QUALITY FOR ALL EPISODES : ")
    
    for w in range(0, len(qualities := BeautifulSoup(requests.get(eplinks[1]).text, 'lxml').find('tbody').findAll('tr'))) :
      print(f'\t {w + 1} - ' + qualities[w].findAll('td')[1].text + ' : ' + qualities[w].findAll('td')[2].text)

    quality = int(input("> "))

    for link in eplinks :
      print(f"DOWNLOADING EPISODE {eplinks.index(link) + 1}")
      download(link)


# IF IT'S A MOVIE INSTEAD, SHOW THE AVAILABLE QUALITIES AND TAKING A CHOICE

elif "/anime/" in showlinks[choice - 1] :
  seasons = BeautifulSoup(requests.get(showlinks[choice - 1]).text, 'lxml').find('div', {'class' : 'contents movies_small'}).findAll('a')
  c = 0
  seasontitles, seasonlinks = [], []
  for season in seasons[-1:-len(seasons)-1:-1] :
    seasonlink = season['href']
    seasontitle = season.find('span', {'class' : 'title'}).text
    seasonlinks.append(seasonlink)
    seasontitles.append(seasontitle)
    c += 1
    print(f"{c} - Season {c} : {seasonlink}")

  schoice = int(input('> Choose a season : '))

  # SHOWING THE EPISODES OF THE CHOSEN SEASON AND TAKING A CHOICE

  print('\n')
  eps = BeautifulSoup(requests.get(seasonlinks[schoice - 1]).text, 'lxml').findAll('td', {'class' : 'ep_title'})
  c = 0
  eplinks, eptitles = [], []
  for ep in eps :
    c += 1
    eplink = ep.a['href']
    eptitle = ep.span.text
    eplinks.append(eplink)
    eptitles.append(eptitle)
    print(f"{c} - Ep {c} : {eplink}")
  c += 1
  print(f"{c} - Download all episodes")

  epchoice = int(input('> Choose an episode : '))


  # SHOWING AVAILABLE QUALITITES AND TAKING A CHOICE

  try :
    
    qualities = BeautifulSoup(requests.get(eplinks[epchoice - 1]).text, 'lxml').find('tbody').findAll('tr')
    print("\n> CHOOSE A QUALITY : ")

    for w in range(0, len(qualities)) :
      print(f'\t {w + 1} - ' + qualities[w].findAll('td')[1].text + ' : ' + qualities[w].findAll('td')[2].text)
    

    quality = int(input('> '))
    download(eplinks[epchoice - 1])
  
  except :
    print("DOWNLOADING ALL EPISODES")
    print("\n> CHOOSE ONE QUALITY FOR ALL EPISODES : ")
    
    for w in range(0, len(qualities := BeautifulSoup(requests.get(eplinks[1]).text, 'lxml').find('tbody').findAll('tr'))) :
      print(f'\t {w + 1} - ' + qualities[w].findAll('td')[1].text + ' : ' + qualities[w].findAll('td')[2].text)

    quality = int(input("> "))

    for link in eplinks :
      print(f"DOWNLOADING EPISODE {eplinks.index(link) + 1}")
      download(link)

else :
  print(f"> YOU CHOSE : {showtitles[choice - 1].replace(':', '')}")
  qualities = BeautifulSoup(requests.get(showlinks[choice - 1]).text, 'lxml').find('tbody').findAll('tr')
  print("\n> CHOOSE A QUALITY : ")
  qq = ['\t1 - Full HD 1080p : ', '\t2 - HD 720p : ', '\t3 - SD 480p : ', '\t4 - SD 360p : ', '\t5 - Low 240p : ']
  
  for w in range(0, len(qualities)) :
    print(f'\t {w + 1} - ' + qualities[w].findAll('td')[1].text + ' : ' + qualities[w].findAll('td')[2].text)

  quality = int(input('> '))

  download(showlinks[choice - 1])

