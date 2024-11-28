from os.path import dirname
from os.path import join
import subprocess
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.floatlayout import FloatLayout
from kivy.core.window import Window
from kivymd.app import MDApp

kv_file = 'MainScreen.kv'
Builder.load_file(join(dirname(__file__), kv_file))
fontName= 'Kangwon Light.ttf'
fontNameTitle = 'Kangwon Bold.ttf' #글씨체
Window.size = (350,600) #핸드폰 사이즈로 실행

class RootLayout(FloatLayout):
    def button01_clicked(self):
        subprocess.call("MainChat.py",shell=True) #MainChat 실행
        # App.get_running_app().stop() #종료 시키기

    def button02_clicked(self):
        subprocess.call("serchcsv.py",shell=True) 
        # App.get_running_app().stop()

class MainApp(MDApp):
    def build(self):
        return RootLayout()


def main():
    MainApp().run()


if __name__ == "__main__":
    main()