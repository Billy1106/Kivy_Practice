# Kivy_Practice
Practicing python GUI system




# kvファイル
## kvファイルを使うことでLabelの設定(fontなど)をまとめて設定できる

## kvファイルは.kvの前に.pyのクラス名にする

E.g 

TestKevy.py

    from kivy.app import App
    from kivy.uix.label import Label

    from kivy.core.text import LabelBase,DEFAULT_FONT
    from kivy.resources import resource_add_path

    resource_add_path('/System/Library/Fonts')
    LabelBase.register(DEFAULT_FONT,'ヒラギノ明朝 ProN.ttc')

    class TestApp(App):
        pass 

    if  __name__=='__main__':
        TestApp().run()

test.kv

    Label:
        text:'Hello World!'


### TestAppがpassされているがHello Worldが表示される。

### つまり


    class TextApp(App):
        def build(self):
            return Label(text="Hello World")
    TextApp().run()



### と同じ



### BoxyLayoutを使用することで複数のラベルやボタンを設定/追加できる

    BoxLayout:
        Label:
            text:'Hello World!'
        Button:
            text:'Hello World!'
        TextInput:
            text:'Hello World!'
        Image:
            source: './img/Dog001.jpg'
               
##　縦横の幅


    from kivy.config import Config
    Config.set('graphics','width','640')
    Config.set('graphics','height','640')

# Widget

### 作ったウィンドウに配置できる部品

https://alis.to/nonota/articles/aoNL8Q9RY4pk

    from kivy.uix.widget import Widget
    class ImageWidget(Widget):
        #kvから呼び出す
        img_source = StringProperty('./img/Dog001.jpg')
        #initは定型文として覚えてok
        def __init__(self,**kwargs):
            super(ImageWidget,self).__init__(**kwargs)
            pass
        #ボタン1が押された場合に呼ぶ
        def buttonStarted(self):
            self.img_source = './img/Dog001.jpg'
        #ボタン2
        def buttonRandom(self):
            self.img_source = f'./img/Dog00{randint(1,3)}.jpg'

#アプリ起動

    class TestApp(App):
        def __init__(self,**kwargs):
            super(TestApp,self).__init__(**kwargs)
            self.title = 'Test window'

    if  __name__=='__main__':
        TestApp().run()

# Kivy Language

    #<ImageWidget>呼び出し
    ImageWidget:

    #test-kv1内のImageWidgetクラスを定義する
    <ImageWidget>:
        #プログラム内のConfig.setに加えて色などを追加
        canvas.before:
            Color:
                rgba: 0.6,0.6,0.6,1
            Rectangle:#デフォルトを持ってくる
                pos: self.pos
                size: self.size
        #構成部分
        BoxLayout:
            #ImageとBoxyLayoutを縦に並べる
            orientation: 'vertical'
            size: root.size

            Image:
                #rootは一番最初のwidget(ImageWidget内)のコードを読み込む
                #selfだった場合Image内のコード
                source: root.img_source
            
            BoxLayout:
                #size_hint_yは上の要素のなん%か
                size_hint_y:0.3
                #各要素の余白
                padding: 20,10,20,10

                Button:
                    id: b1
                    text: "Button 1"
                    front_size:30
                    #ボタンがプレスされた場合
                    on_press:root.buttonStarted()
                Button:
                    id: b2
                    text: "Button 2"
                    front_size:30
                    #ボタンがプレスされた場合
                    on_press:root.buttonRandom()

https://www.youtube.com/watch?v=usbEwmOIhwo
