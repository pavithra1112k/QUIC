#getting a movie review


from selenium import webdriver


class movie():
    def __init__(self):
        self.driver=webdriver.Chrome()
    def movie_review(self,name):
        #self.query=query
        self.driver.get(url="https://www.google.com")            # driver to open google
        search=self.driver.find_element_by_xpath(' /html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input')     #copy the xpath by inspecting the search bar of wiki page
        search.click()
        search.send_keys(name + " movie reviews")
        submit=self.driver.find_element_by_xpath('/html/body/div[1]/div[3]/form/div[1]/div[1]/div[3]/center/input[1]')
        search.submit()
'''
bot=movie()
bot.movie_review("Interception")
'''
