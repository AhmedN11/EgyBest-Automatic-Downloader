# Egybest-Automatic-Downloader
This is a python script I've developed that downloads a movie/series of your choice from the egy.best website automatically to avoid annoying ads.

### For this script to work on your machine, you'll need :
  ###### - Requests Library
  ###### - BeautifulSoup Library
  ###### - pySmartDL Library
  ###### - Selenium Library
  ###### - Helium Library
  ###### - msedge-selenium-tools Library

These can be installed using the command : pip install -r requirements.txt

And a Microsoft Edge browser (if you don't have a python IDE, you can turn the .py file into .exe using pyinstaller, just make sure to move the .exe file to the same location as the .py file).

Please make sure that the browser and webdriver are up to date and are compatible (more on that below).


## How to use :

The usage of this program is pretty straightforward. After extracting the EGYBEST folder to the "DESKTOP" (or else it won't work because the path to the webdrivers is hard-coded) :

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


### How update Edge WebDriver (in case it doesn't work) :

- First of all, you have to make sure that your browser is up to date.

- Then, go to [Edge webdriver page](https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/) and download the latest webdriver according to which browser you have (Stable/Beta/...)

![ ](https://i.imgur.com/88aUNr2.png)

- Move to the folder containing your .py file and replace the old driver.

- Done!

## V1 :

	- Added download quality options.
	- Added whole season download.
	- Only supports Edge browser.