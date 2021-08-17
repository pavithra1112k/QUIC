from selenium import webdriver
import speech_recognition as sr
import pyttsx3 as p

class music():
    def __init__(self):
        self.driver=webdriver.Chrome()
    def play_music(self,name):
        self.name=name
        self.driver.get(url="https://www.youtube.com/results?search_query="+name)            # driver to open youtube music
        video=self.driver.find_element_by_xpath('//*[@id="img"]')    
        video.click()
       
'''
bot=music()
bot.play_music("Yarayum ivlo azhaga")
'''
