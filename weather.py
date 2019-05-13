from bs4 import BeautifulSoup
import re
import time
import arcade
import urllib.request
import mmap
#windows constants
SCREEN_WIDTH = 300
SCREEN_HEIGHT = 300

#create window
class window(arcade.Window):
    def __init__(self,SCREEN_WIDTH,SCREEN_HEIGHT, title = "Today's Weather"):
        super().__init__(SCREEN_WIDTH,SCREEN_HEIGHT, title = "Today's Weather")
        arcade.set_background_color(arcade.color.WHITE)
        arcade.run()
        
    def on_draw(self):
        arcade.start_render()
        temp = getTemp()
        arcade.draw_text(temp,150,150,color = arcade.color.BLACK)
        arcade.finish_render()
#find temperature from www.wunderground.com
def getTemp():    
    webpage = "https://www.wunderground.com/weather/us/oh/cincinnati/45201"
    websource = urllib.request.urlopen(webpage)
    #allow for page to update
    time.sleep(6)
    
    soup = BeautifulSoup(websource, "html.parser")
    #look for current temp
    soup = soup.find_all('span', {'class', 'wu-value wu-value-to'},{'style', '"color:#93c124;"'})
    s = str(soup[1])
    return s[62:64]
def getCond():
       
def main():
    window(SCREEN_WIDTH, SCREEN_HEIGHT)
    window.on_draw(window)
    
    

if __name__ == "__main__":
    main()

   




