#파스
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
    FirstQ_r:
    FirstQy_r: 
    FirstQn_r:
    FirstQyy_r:
    FirstQnn_r:
    OtherQy_r:
    OtherQn_r:

<FirstQ_r>:
    name: 'firstquestion'
    MDLabel:
        font_name: 'Kangwon Light.ttf'
        font_size: 22
        text: '염증이 동반된 통증입니까?'
        pos_hint: {'center_x':0.7,'center_y':0.8} #x축 가운데로

    MDRectangleFlatButton:
        pos_hint: {'center_x':0.5,'center_y':0.5}
        text: 'Yes'
        on_press: root.manager.current = 'firstquestiony'
    MDRectangleFlatButton:
        text: 'No'
        pos_hint: {'center_x':0.5,'center_y':0.3}
        on_press: root.manager.current = 'firstquestionn'
    
<FirstQy_r>:
    name: 'firstquestiony'
    MDLabel:
        font_name : 'Kangwon Light.ttf'
        font_size: 22
        text: 'COOL한 느낌을 원하시나요?'
        pos_hint: {'center_x':0.7,'center_y':0.8}
    MDRectangleFlatButton:
        pos_hint: {'center_x':0.5,'center_y':0.5}
        text: 'Yes'
        on_press: root.manager.current = 'firstquestionyy'
    MDRectangleFlatButton:
        text: 'No'
        pos_hint: {'center_x':0.5,'center_y':0.3}
        on_press: root.manager.current = 'firstquestionnn'

<FirstQn_r>:
    name: 'firstquestionn'

    Image:
        source:'아렉스.png'
        size_hint: 0.6,0.6
        pos_hint: {'center_x': 0.5, 'center_y': 0.55}
    
    MDLabel:
        font_name : 'Kangwon Light.ttf'
        font_size: 22
        text: '아렉스를 사용하세요!'
        pos_hint: {'center_x':0.75,'center_y':0.85}
    MDRectangleFlatButton:
        text: 'Home'
        pos_hint: {'center_x':0.5,'center_y':0.3}
        on_press: root.manager.current = 'firstquestion'

<FirstQyy_r>:
    name: 'firstquestionyy'
    MDLabel:
        font_name : 'Kangwon Light.ttf'
        font_size: 22
        text: '로션 형태를 원하십니까?'
        pos_hint: {'center_x':0.7,'center_y':0.8}
    MDRectangleFlatButton:
        pos_hint: {'center_x':0.5,'center_y':0.5}
        text: 'Yes'
        on_press: root.manager.current = 'otherquestiony'
    MDRectangleFlatButton:
        text: 'No'
        pos_hint: {'center_x':0.5,'center_y':0.3}
        on_press: root.manager.current = 'otherquestionn'

<FirstQnn_r>:
    name: 'firstquestionnn'

    Image:
        source:'신신파스핫.png'
        size_hint: 0.7,0.7
        pos_hint: {'center_x': 0.55, 'center_y': 0.55}
    
    MDLabel:
        font_name : 'Kangwon Light.ttf'
        font_size: 22
        text: '신신파스 HOT을 사용하세요!'
        pos_hint: {'center_x':0.75,'center_y':0.85}
    MDRectangleFlatButton:
        text: 'Home'
        pos_hint: {'center_x':0.5,'center_y':0.3}
        on_press: root.manager.current = 'firstquestion'

<OtherQy_r>:
    name: 'otherquestiony'

    Image:
        source:'맨소래담 로션.png'
        size_hint: 0.5,0.5
        pos_hint: {'center_x': 0.5, 'center_y': 0.55}
    
    MDLabel:
        font_name : 'Kangwon Light.ttf'
        font_size: 22
        text: '맨소래담 로션을 사용하세요!'
        pos_hint: {'center_x':0.7,'center_y':0.8}
    MDRectangleFlatButton:
        text: 'Home'
        pos_hint: {'center_x':0.5,'center_y':0.3}
        on_press: root.manager.current = 'firstquestion'

<OtherQn_r>
    name: 'otherquestionn'

    Image:
        source:'신신파스쿨.png'
        size_hint: 0.75,0.75
        pos_hint: {'center_x': 0.5, 'center_y': 0.55}
    
    MDLabel:
        font_name : 'Kangwon Light.ttf'
        font_size: 22
        text: '신신파스 COOL을 사용하세요!'
        pos_hint: {'center_x':0.7,'center_y':0.85}
    MDRectangleFlatButton:
        text: 'Home'
        pos_hint: {'center_x':0.5,'center_y':0.3}
        on_press: root.manager.current = 'firstquestion'
"""

class FirstQ_r(Screen):
    pass

class FirstQy_r(Screen):
    pass

class FirstQyy_r(Screen):
    pass

class FirstQnn_r(Screen):
    pass

class FirstQn_r(Screen):
    pass

class OtherQy_r(Screen):
    pass

class OtherQn_r(Screen):
    pass


# Create the screen manager
sm = ScreenManager()
sm.add_widget(FirstQ_r(name='firstquestion'))
sm.add_widget(FirstQy_r(name='firstquestiony'))
sm.add_widget(FirstQyy_r(name='firstquestionyy'))
sm.add_widget(FirstQnn_r(name='firstquestionnn'))
sm.add_widget(FirstQn_r(name='firstquestionn'))
sm.add_widget(OtherQy_r(name='otherquestiony'))
sm.add_widget(OtherQn_r(name='otherquestionn'))


class DemoApp(MDApp):

    def build(self):
        screen = Builder.load_string(screen_helper)
        return screen

DemoApp().run()
