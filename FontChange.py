from kivy.app import App
from kivy.uix.label import Label

from kivy.core.text import LabelBase,DEFAULT_FONT
from kivy.resources import resource_add_path

resource_add_path('/System/Library/Fonts')
LabelBase.register(DEFAULT_FONT,'ヒラギノ明朝 ProN.ttc')

class TextApp(App):
    def build(self):
        return Label(text="こんにちは！")
TextApp().run()
