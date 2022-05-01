import requests
from bs4 import BeautifulSoup
import json
from time import sleep
from pySmartDL import SmartDL
import os
from msedge.selenium_tools import Edge, EdgeOptions







def download(link) :

  options = EdgeOptions()
  options.use_chromium = True
  options.add_argument("headless")
  options.add_argument("disable-gpu")
  options.add_argument("--log-level=0")
  driver = Edge(executable_path = os.getcwd() + '\\Desktop\\EGYBEST\\msedgedriver.exe', options=options)



  print("> Gathering the download link, please wait : \n")
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


  try :
    os.mkdir(os.getcwd() + f"\\Desktop\\{showtitles[choice - 1]}")
  except :
    pass


  try :
    task = SmartDL(dl, os.getcwd() + f"\\Desktop\\{showtitles[choice - 1]}\\Season {schoice} - {eptitles[eplinks.index(link)]}.mp4")
    task.start()
    task.wait()
    print('EPISODE DOWNLOAD FINISHED.')
  except :
    task = SmartDL(dl, os.getcwd() + f"\\Desktop\\{showtitles[choice - 1]}\\{showtitles[choice - 1].replace(':', '')}.mp4")
    task.start()
    task.wait()
    print('MOVIE DOWNLOAD FINISHED.')


  return



waiting = int(input("Enter loading page waiting time (default is 2, increase if you have slow internet, hit enter to skip) : ") or "2")


choice = 0
while choice == 0 :
  showtitles, showlinks = [], []
  name = input("> What Movie/Show you're looking for : ")
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
  choice = int(input('> Choose a Show/Movie : '))


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



  try :
    check = eplinks[epchoice - 1]
    qualities = BeautifulSoup(requests.get(eplinks[epchoice - 1]).text, 'lxml').find('tbody').findAll('tr')
    print("> CHOOSE A QUALITY : ")
    qq = ['\t1 - Full HD 1080p : ', '\t2 - HD 720p : ', '\t3 - SD 480p : ', '\t4 - SD 360p : ', '\t5 - Low 240p : ']

    for w in range(0, len(qualities)) :
      print(qq[w] + qualities[w].findAll('td')[2].text)

    quality = int(input())
    download(eplinks[epchoice - 1])

  except :
    print("DOWNLOADING ALL EPISODES")
    quality = int(input("> CHOOSE ONE QUALITY FOR ALL EPISODES : \n\t1 - Full HD 1080p\n\t2 - HD 720p\n\t3 - SD 480p\n\t4 - SD 360p\n\t5 - Low 240p\n"))
    
    for link in eplinks :
      print(f"DOWNLOADING EPISODE {eplinks.index(link) + 1}")
      download(link)

else :
  print(f"> YOU CHOSE : {showtitles[choice - 1].replace(':', '')}")
  qualities = BeautifulSoup(requests.get(showlinks[choice - 1]).text, 'lxml').find('tbody').findAll('tr')
  print("> CHOOSE A QUALITY : ")
  qq = ['\t1 - Full HD 1080p : ', '\t2 - HD 720p : ', '\t3 - SD 480p : ', '\t4 - SD 360p : ', '\t5 - Low 240p : ']
  
  for w in range(0, len(qualities)) :
    print(qq[w] + qualities[w].findAll('td')[2].text)

  quality = int(input())

  download(showlinks[choice - 1])