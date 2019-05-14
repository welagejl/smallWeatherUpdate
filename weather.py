from bs4 import BeautifulSoup
import time
import arcade
import urllib.request

#windows constants
SCREEN_WIDTH = 300
SCREEN_HEIGHT = 300

#create window
class window(arcade.Window):
    def __init__(self,SCREEN_WIDTH,SCREEN_HEIGHT, title = "Today's Weather"):
        super().__init__(SCREEN_WIDTH,SCREEN_HEIGHT, title = "Today's Weather")
        arcade.set_background_color(arcade.color.WHITE)
        
        
    def on_draw(self):
        arcade.start_render()
        
        temp = getTemp()
        cond = getCond()
        
        values = [temp, cond]
        
        arcade.draw_text(temp,150,150,color = arcade.color.BLACK)
        arcade.draw_text(cond,200,200,color = arcade.color.BLACK)
        if values[0]
        
        arcade.finish_render()

        return values
        
#find temperature from www.wunderground.com
def getTemp():    
    webpage = "https://www.wunderground.com/weather/us/oh/cincinnati/45201"
    websource = urllib.request.urlopen(webpage)
    #allow for page to update
    time.sleep(3)
    
    soup = BeautifulSoup(websource, "html.parser")
    #look for current temp
    soup = soup.find_all('span', {'class', 'wu-value wu-value-to'},{'style', '"color:#93c124;"'})
    s = str(soup[1])
    return s[62:64]
#Get the sky conditions
def getCond():
    webpage = "https://www.wunderground.com/weather/us/oh/cincinnati/45201"
    websource = urllib.request.urlopen(webpage)
    #allow for page to update
    time.sleep(3)
        
    soup = BeautifulSoup(websource, "html.parser")
    #look for current condition
    soup = soup.find_all({'p', '_nncontent-c30'})
    newString = str(soup[4])

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
    values = window.on_draw(weather)
    arcade.run()
    
if __name__ == "__main__":
    main()

   




