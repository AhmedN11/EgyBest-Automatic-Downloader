# Egybest-Automatic-Downloader
This is a python script I've developed that downloads a movie/series of your choice from the egy.best website automatically to avoid annoying ads.

### For this script to work on your machine, you'll need :
  ###### - Requests Library
  ###### - BeautifulSoup Library
  ###### - Selenium Library
  ###### - msedge-selenium-tools Library

These can be installed using the command : pip install -r requirements.txt

And a Microsoft Edge or Google Chrome browser.

Please make sure that the browser and webdriver are up to date and are compatible (more on that below).

NOTE : The folder containing the files MUST be named "EGYBEST" AND MUST be located on your DESKTOP.


## How to use :

The usage of this program is pretty straightforward.

DISCLAIMER : For this version to work, you MUST delete the driver you are not going to need, e.g. Chrome users MUST delete "msedgedriver.exe", and vice-versa.

First, you get to define how long the headless browser will wait for the website to load in the background, increase depending on how slow your internet speed is.

<p align="center">
  <img src="https://i.imgur.com/uN8gCBi.png" />
</p>

Then, you can search for any content in the egy.best website and see the results.

![ ](https://i.imgur.com/pqlM0vn.png)

After that, you can specify the season and the episode you want to download, or you can choose to download the whole season (Please make sure you have enough storage space).
And choose the quality of the episode/whole season you want to download.

![ ](https://i.imgur.com/rZQ57x0.png)

Finally, all you have to do is to wait for the program to find and start the download for you.

![ ](https://i.imgur.com/gWduykM.png)

Tada! After the download is finished, your episode/season should be available in a new folder on your desktop, all with their respective names.

<p align="center">
  <img src="https://i.imgur.com/eqknar2.png" />
</p>


### How update Edge WebDriver (in case it stops working) :

- First of all, you have to make sure that your browser is up to date.

- Then, go to [Edge webdriver page](https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/) and download the latest webdriver according to which browser you have (Stable/Beta/...). The same goes to [Chrome](https://chromedriver.chromium.org/downloads).

![ ](https://i.imgur.com/88aUNr2.png)

- Move to the folder containing your .py file and replace the old driver (the folder MUST be named "EGYBEST" AND MUST be located on your DESKTOP).

- Done!

## V1 :

	- Added download quality options.
	- Added whole season download.

## V2 :

	- Added support for Chrome users (for this version to work, you MUST delete the driver you are not going to need, e.g. Chrome users MUST delete "msedgedriver.exe", and vice-versa). Make sure the drivers AND the browsers are up to date.
	- Now supports download via IDMan if you have it installed alongside its browser extension, if not, the download starts in the browser.

## V3 :

	- Added support for anime content (newly hosted on the website).

## V4 :

	- Fixed wrong quality bug.

## V4.1 :

	- Fixed minor bugs.