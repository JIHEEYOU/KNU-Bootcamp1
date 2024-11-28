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
    FirstQ_a:
    FirstQy_a: 
    FirstQn_a:
    OtherQy_a:
    OtherQn_a:

<FirstQ_a>:
    name: 'firstquestion'
    MDLabel:
        font_name: 'Kangwon Light.ttf'
        text: '알레르기약이 필요하시군요,'
        font_size: 22
        pos_hint: {'center_x':0.7,'center_y':0.75} #x축 가운데로

    MDLabel:
        font_name: 'Kangwon Light.ttf'
        text: '결막염이 있습니까?'
        font_size: 22
        pos_hint: {'center_x':0.8,'center_y':0.7}

    MDRectangleFlatButton:
        pos_hint: {'center_x':0.5,'center_y':0.5}
        text: 'Yes'
        on_press: root.manager.current = 'firstquestiony'
    MDRectangleFlatButton:
        text: 'No'
        pos_hint: {'center_x':0.5,'center_y':0.3}
        on_press: root.manager.current = 'firstquestionn'
    
<FirstQy_a>:
    name: 'firstquestiony'

    Image:
        source:'지르텍.png'
        size_hint: 0.7,0.7
        pos_hint: {'center_x': 0.5, 'center_y': 0.5}

    MDLabel:
        font_name : 'Kangwon Light.ttf'
        text: '지르텍을 복용하세요!'
        font_size: 22
        pos_hint: {'center_x':0.75,'center_y':0.7}

    MDRectangleFlatButton:
        text: 'Home'
        pos_hint: {'center_x':0.5,'center_y':0.3}
        on_press: root.manager.current = 'firstquestion'
        
<FirstQn_a>:
    name: 'firstquestionn'
    MDLabel:
        font_name : 'Kangwon Light.ttf'
        text: '졸림현상에 예민하신가요?'
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

<OtherQy_a>
    name: 'otherquestiony'

    Image:
        source:'지르텍.png'
        size_hint: 0.7,0.7
        pos_hint: {'center_x': 0.5, 'center_y': 0.5}

    MDLabel:
        font_name : 'Kangwon Light.ttf'
        text: '지르텍을 복용하세요!'
        font_size: 22
        pos_hint: {'center_x':0.75,'center_y':0.7}

    MDRectangleFlatButton:
        text: 'Home'
        pos_hint: {'center_x':0.5,'center_y':0.3}
        on_press: root.manager.current = 'firstquestion'

<OtherQn_a>
    name: 'otherquestionn'

    Image:
        source:'클라리틴.png'
        size_hint: 0.7,0.7
        pos_hint: {'center_x': 0.5, 'center_y': 0.5}

    MDLabel:
        font_name : 'Kangwon Light.ttf'
        text: '클라리틴을 복용하세요!'
        font_size: 22
        pos_hint: {'center_x':0.75,'center_y':0.7}

    MDRectangleFlatButton:
        text: 'Home'
        pos_hint: {'center_x':0.5,'center_y':0.3}
        on_press: root.manager.current = 'firstquestion'
"""


class FirstQ_a(Screen):
    pass

class FirstQy_a(Screen):
    pass

class FirstQn_a(Screen):
    pass

class OtherQy_a(Screen):
    pass

class OtherQn_a(Screen):
    pass


# Create the screen manager
sm = ScreenManager()
sm.add_widget(FirstQ_a(name='firstquestion'))
sm.add_widget(FirstQy_a(name='firstquestiony'))
sm.add_widget(FirstQn_a(name='firstquestionn'))
sm.add_widget(OtherQy_a(name='otherquestiony'))
sm.add_widget(OtherQn_a(name='otherquestionn'))


class DemoApp(MDApp):

    def build(self):
        screen = Builder.load_string(screen_helper)
        return screen

DemoApp().run()