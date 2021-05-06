from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import StringProperty
from kivy.uix.label import Label

from kivy.core.text import LabelBase,DEFAULT_FONT
from kivy.resources import resource_add_path

from kivy.config import Config
Config.set('graphics','width','800')
Config.set('graphics','height','600')

from random import randint

resource_add_path('/System/Library/Fonts')
LabelBase.register(DEFAULT_FONT,'ヒラギノ明朝 ProN.ttc')
#ウィンドウ
MAX_NUM_IMAGE = 3
class ImageWidget(Widget):

    #kvから呼び出す
    animal_id = 1;
    img_source = StringProperty('./img/Dog001.jpg')
    #initは定型文として覚えてok
    def __init__(self,**kwargs):
        super(ImageWidget,self).__init__(**kwargs)
        pass
    
    
    def buttonDog(self):
        self.img_source = f'./img/Dog00{self.animal_id}.jpg'
        self.animalCounter() # To call method within same class, include self
        
    def buttonCat(self):
        self.img_source = f'./img/Cat00{self.animal_id}.jpg'
        self.animalCounter()

 
    def buttonRandom(self):
        animal = 'Dog'
        if(randint(0,1)):
            animal = 'Cat'
        self.img_source = f'./img/{animal}00{randint(1,3)}.jpg'
    
    #set animal_id
    def animalCounter(self):
        if(self.animal_id>=MAX_NUM_IMAGE):
            self.animal_id = 1
        else:
            self.animal_id += 1
#アプリ
class AnimalApp(App):
    def __init__(self,**kwargs):
        super(AnimalApp,self).__init__(**kwargs)
        self.title = 'Main window'

if  __name__=='__main__':
    AnimalApp().run()
