
from selenium import webdriver    #for web automation
import pyttsx3 as p

class info():
    def __init__(self):
        self.driver=webdriver.Chrome()
    def get_info(self,query):
        self.query=query
        self.driver.get(url="https://www.wikipedia.org/")            # driver to open wiki
        search=self.driver.find_element_by_xpath('//*[@id="searchInput"]')     #copy the xpath by inspecting the search bar of wiki page
        search.click()
        search.send_keys(query)
        enter=self.driver.find_element_by_xpath('//*[@id="search-form"]/fieldset/button/i')
        enter.click()
        info=self.driver.find_element_by_xpath('//*[@id="mw-content-text"]/div[1]/p[2]')
        readable_text = info.text
        engine=p.init()
        engine.say(readable_text)
        engine.runAndWait()

        
#bot=info() #creating a class object "bot"
#bot.get_info("Liberty Bell")
