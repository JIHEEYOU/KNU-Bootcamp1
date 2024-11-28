import os
from kivymd.app import MDApp
from kivy.lang.builder import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.uix.button import button
from kivy.core.window import Window
from kivy.core.text import Label as CLabel
from kivy.core.text import LabelBase

Window.size = (350,600)
CLabel.register('Kfont',   #font 이름 정의                         
                fn_regular='Kangwon Light.ttf',  # regular font
                fn_italic=None,                 # italic font
                fn_bold=None,                      # bold font
                fn_bolditalic=None)   

screen_helper = """
ScreenManager:
    FirstQ:
    FirstQy: 
    FirstQn:
    OtherQy:
    OtherQn:

<FirstQ>:
    name: 'firstquestion'
    MDLabel:
        font_name: 'Kangwon Light.ttf'
        text: '생리통약이 필요하시군요,'
        font_size: 22
        pos_hint: {'center_x':0.7,'center_y':0.75} #x축 가운데로

    MDLabel:
        font_name: 'Kangwon Light.ttf'
        text: ' 아랫배 통증이 있습니까?'
        font_size: 22
        pos_hint: {'center_x':0.7,'center_y':0.7}

    MDRectangleFlatButton:
        pos_hint: {'center_x':0.5,'center_y':0.5}
        text: 'Yes'
        on_press: root.manager.current = 'firstquestiony'
    MDRectangleFlatButton:
        text: 'No'
        pos_hint: {'center_x':0.5,'center_y':0.3}
        on_press: root.manager.current = 'firstquestionn'
    
<FirstQy>:
    name: 'firstquestiony'
    MDLabel:
        font_name : 'Kangwon Light.ttf'
        text: '샤이닝정이나 부스코판 플러스정을 복용하세요!'
        font_size: 22
        pos_hint: {'center_x':0.65,'center_y':0.7}
    Image:
        source:'샤이코판.png'
        size_hint: 0.7,0.7
        pos_hint: {'center_x': 0.45, 'center_y': 0.55}

    MDRectangleFlatButton:
        text: 'Home'
        pos_hint: {'center_x':0.5,'center_y':0.3}
        on_press: root.manager.current = 'firstquestion'
        
<FirstQn>:
    name: 'firstquestionn'
    MDLabel:
        font_name : 'Kangwon Light.ttf'
        text: '위장장애가 있습니까?'
        font_size: 22
        pos_hint: {'center_x':0.75,'center_y':0.7}

    MDRectangleFlatButton:
        text: 'Yes'
        pos_hint: {'center_x':0.5,'center_y':0.5}
        on_press: root.manager.current = 'otherquestiony'
    MDRectangleFlatButton:
        text: 'No'
        pos_hint: {'center_x':0.5,'center_y':0.3}
        on_press: root.manager.current = 'otherquestionn'

<OtherQy>
    name: 'otherquestiony'
    MDLabel:
        font_name : 'Kangwon Light.ttf'
        text: '탁센이브나 이지엔6이브를 복용하세요!'
        font_size: 22
        pos_hint: {'center_x':0.6,'center_y':0.7}
    Image:
        source:'탁센6이브.png'
        size_hint: 0.7,0.7
        pos_hint: {'center_x': 0.47, 'center_y': 0.5}
    MDRectangleFlatButton:
        text: 'Home'
        pos_hint: {'center_x':0.5,'center_y':0.3}
        on_press: root.manager.current = 'firstquestion'

<OtherQn>
    name: 'otherquestionn'
    MDLabel:
        font_name : 'Kangwon Light.ttf'
        text: '탁센400을 복용하세요!'
        font_size: 22
        pos_hint: {'center_x':0.75,'center_y':0.7}
    Image:
        source:'텍센400.png'
        size_hint: 0.25,0.25
        pos_hint: {'center_x': 0.5, 'center_y': 0.53}
    MDRectangleFlatButton:
        text: 'Home'
        pos_hint: {'center_x':0.5,'center_y':0.3}
        on_press: root.manager.current = 'firstquestion'
"""

class FirstQ(Screen):
    pass

class FirstQy(Screen):
    pass

class FirstQn(Screen):
    pass

class OtherQy(Screen):
    pass

class OtherQn(Screen):
    pass


# Create the screen manager
sm = ScreenManager()
sm.add_widget(FirstQ(name='firstquestion'))
sm.add_widget(FirstQy(name='firstquestiony'))
sm.add_widget(FirstQn(name='firstquestionn'))
sm.add_widget(OtherQy(name='otherquestiony'))
sm.add_widget(OtherQn(name='otherquestionn'))


class DemoApp(MDApp):

    def build(self):
        screen = Builder.load_string(screen_helper)
        return screen

DemoApp().run()