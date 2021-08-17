#movie recommendation automation
from selenium import webdriver
import speech_recognition as sr
import pyttsx3 as p

class recom():
    '''
    r=sr.Recognizer()
    engine=p.init()
    engine.say("Hola! Speak out a number in between 1 to 3")
    engine.say("1 for IMDB Rating, 2 for Release Date and 3 for Number of ratings")
    engine.runAndWait()
    
    with sr.Microphone() as source:
        text = r.listen(source)   #to get voice input
    #using google cloud API to recognize the voice
    try:
        query=r.recognize_google(text)
        print(query)
    except sr.UnknownValueError :
        print("Google speech Recognition could not understand audio")
    except sr.RequestError :
        print("Couldnt get the result from google speech recognition")
        '''
    def __init__(self):
        self.driver=webdriver.Chrome()
    def give_recom(self):
         #default option chosen in dropdown is Rankings
         self.driver.get(url="https://www.imdb.com/chart/moviemeter/?ref_=nv_mv_mpm")
'''
         #for automating IMDb Ratings option in dropdown
         enter=self.driver.find_element_by_xpath('//*[@id="lister-sort-by-options"]')
         enter.click()
         select=self.driver.find_element_by_xpath('//*[@id="lister-sort-by-options"]/option[2]')    
         select.click()
         enter.click()
         #for automating Release Date option in dropdown
         enter=self.driver.find_element_by_xpath('//*[@id="lister-sort-by-options"]')
         enter.click()
         select=self.driver.find_element_by_xpath('//*[@id="lister-sort-by-options"]/option[3]')    
         select.click()
         enter.click()
         #for automating Number of ratings option in dropdown  
         enter=self.driver.find_element_by_xpath('//*[@id="lister-sort-by-options"]')
         enter.click()
         select=self.driver.find_element_by_xpath('//*[@id="lister-sort-by-options"]/option[4]')    
         select.click()
         enter.click()
         #for automating Your Rating option in dropdown
         enter=self.driver.find_element_by_xpath('//*[@id="lister-sort-by-options"]')
         enter.click()
         select=self.driver.find_element_by_xpath('//*[@id="lister-sort-by-options"]/option[5]')    
         select.click()
         enter.click()
         #to Convert ascending to descending order
         select=self.driver.find_element_by_xpath(' //*[@id="main"]/div/span/div/div/div[3]/div/div/div[1]/span')    
         select.click()
'''
'''
bot=recom()
bot.give_recom()
'''
