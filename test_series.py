import urllib.request
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


#Series Downloader from theNetNaija
__author__ = 'Dzhud'

class SeriesDLerforNetNaija:

    def inputURL(self, url):
        self.url = url
        requestSeries = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        openSeriesPage = urlopen(requestSeries)
        soupy = BeautifulSoup(openSeriesPage, "html.parser")
        return soupy

    def getSeriesDLLink(self):
        prefix = 'https://www.thenetnaija.com'
        for i in SeriesDLerforNetNaija.inputURL(self, self.url).find_all('a', href=True):
            ty = i['href']
            if 'download' in ty and 'download-sub' not in ty:
                return prefix+ty
            
    def getSRTDLLink(self):
        prefix = 'https://www.thenetnaija.com'
        for i in SeriesDLerforNetNaija.inputURL(self, self.url).find_all('a', href=True):
           ty = i['href']
           if 'download-sub' in ty:
               return prefix+ty

    def enable_download_headless(self, browser, download_dir, executable_path_for_chrome):
        browser.command_executor._commands["send_command"] = ("POST", '/session/$sessionId/chromium/send_command')
        params = {'cmd':'Page.setDownloadBehavior', 'params': {'behavior': 'allow', 'downloadPath': download_dir}}
        browser.execute("send_command", params)

        chrome_options = Options()
        chrome_options.add_argument("--disable-notifications")
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--window-size=1920x1080")
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--verbose')
        chrome_options.add_experimental_option("prefs", {
        "download.default_directory": download_dir,
        "download.prompt_for_download": False,
        "download.directory_upgrade": True,
        "safebrowsing_for_trusted_sources_enabled": False,
        "safebrowsing.enabled": False })
        chrome_options.add_argument('--disable-gpu')
        chrome_options.add_argument('--disable-software-rasterizer')
        driver = webdriver.Chrome(options=chrome_options, executable_path=executable_path_for_chrome)

        browser.get(SeriesDLerforNetNaija.getSRTDLLink(self))
        srtDL = browser.find_element_by_xpath("//*[@id='action-buttons']/button")
        browser.execute_script("arguments[0].click();", srtDL)

        browser.get(SeriesDLerforNetNaija.getSeriesDLLink(self))
        videoDL = browser.find_element_by_xpath("//*[@id='action-buttons']/button")
        videoDL.click()

initializer = SeriesDLerforNetNaija()
initializer.inputURL('https://www.thenetnaija.com/videos/series/14277-tom-and-jerry-in-new-york/season-1/episode-2')
initializer.getSRTDLLink()
initializer.getSeriesDLLink()
chrome_options = Options()
browser = webdriver.Chrome(options=chrome_options, executable_path=r"C:\\Program Files\\ChromeDriver for Selenium\\chromedriver.exe")
download_dir = r"C:\Users\Priceless\Documents\Programming Projects\showDLer\netNaijaDLer"
executable_path_for_chrome = r"C:\\Program Files\\ChromeDriver for Selenium\\chromedriver.exe" 

initializer.enable_download_headless(browser, download_dir, executable_path_for_chrome)
                

        
