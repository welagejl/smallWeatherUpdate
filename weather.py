from bs4 import BeautifulSoup
import time
import arcade
import urllib.request
import sys

#window constants
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 400

#create window/events
class window(arcade.Window):
    def __init__(self,SCREEN_WIDTH,SCREEN_HEIGHT, title = "Today's Weather"):
        super().__init__(SCREEN_WIDTH,SCREEN_HEIGHT, title = "Today's Weather")
        arcade.set_background_color(arcade.color.BLACK)
               
    def on_draw(self):
        arcade.start_render()
        
        temp = getTemp()
        cond = getCond()
        
        arcade.draw_text("Today's Temperature: ",100,350,color = arcade.color.RED)
        arcade.draw_text(temp + ' F',100,300,color = arcade.color.RED)
        arcade.draw_text(cond,100,250,color = arcade.color.RED)

        #determine picture based on cond
        if cond == 'Partly Cloudy':
            image = arcade.Sprite("partly_cloudy.png")
            image.center_x = 200
            image.center_y = 150
            image.draw()
        elif cond == 'Cloudy':
            image = arcade.Sprite("cloudy.png")
            image.center_x = 200
            image.center_y = 150
            image.draw()
        elif cond == 'Sunny' or cond == 'Clear':
            image = arcade.Sprite("happy_sun.png")
            image.center_x = 200
            image.center_y = 150
            image.draw()
        elif cond == 'Showers' or cond == 'Rain':
            image = arcade.Sprite("rain.png")
            image.center_x = 200
            image.center_y = 150
            image.draw()
        else:
            image = arcade.Sprite("neutral_sun.png")
            image.center_x = 200
            image.center_y = 150
            image.draw()
        #finish render
        arcade.finish_render()
        time.sleep(5)
        arcade.close_window()
        
#find temperature from www.wunderground.com
def getTemp():
    i = 0
    while i == 0:
        webpage = "https://www.wunderground.com/weather/us/oh/cincinnati/45201"
        
        web = urllib.request.Request(webpage, headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36"})
        websource = urllib.request.urlopen(web)
        #allow for page to update
        time.sleep(3)
        
        soup = BeautifulSoup(websource, "html.parser")
        #look for current temp
        soup = soup.find_all('span', {'class', 'wu-value wu-value-to'},{'style', '"color:#93c124;"'})
        try:
             s = str(soup[1])
        except IndexError:
            i = 0
        else:
            i = 1
            
    return s[62:64]

#Get the sky conditions
def getCond():
    i = 0
    while i == 0:
        webpage = "https://www.wunderground.com/weather/us/oh/cincinnati/45201"
        
        web = urllib.request.Request(webpage, headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36"})
        websource = urllib.request.urlopen(web)
        #allow for page to update
        time.sleep(3)
            
        soup = BeautifulSoup(websource, "html.parser")
        #look for current condition
        soup = soup.find_all({'p', '_nncontent-c30'})
        #make sure data is found
        try:
             newString = str(soup[4])
        except IndexError:
            i = 0
        else:
            i = 1        
    i = 0
    x = 0
    cond = ''
    while newString[i] != '>':
        x = i
        i +=1
    x = x + 2
    while newString[x] !=  '<':
            cond = cond + newString[x]
            x += 1
    return cond

def main():
        weather = window(SCREEN_WIDTH, SCREEN_HEIGHT)
        weather.on_draw()
        arcade.run()   
    
if __name__ == "__main__":
    main()

    

   




