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
    FirstQyy:
    FirstQnn:
    OtherQy:
    OtherQn:
    LastQy:
    LastQn:

<FirstQ>:
    name: 'firstquestion'
    MDLabel:
        font_name: 'Kangwon Light.ttf'
        text: '연고가 필요하시군요, '
        font_size: 22
        pos_hint: {'center_x':0.75,'center_y':0.75} #x축 가운데로

    MDLabel:
        font_name: 'Kangwon Light.ttf'
        text: '다친 지 2~3주 정도 지났습니까?'
        font_size: 22
        pos_hint: {'center_x':0.65,'center_y':0.7} #x축 가운데로

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
        text: '화상을 입었습니까?'
        font_size: 22
        pos_hint: {'center_x':0.8,'center_y':0.7}
    MDRectangleFlatButton:
        pos_hint: {'center_x':0.5,'center_y':0.5}
        text: 'Yes'
        on_press: root.manager.current = 'firstquestionyy'
    MDRectangleFlatButton:
        text: 'No'
        pos_hint: {'center_x':0.5,'center_y':0.3}
        on_press: root.manager.current = 'firstquestionnn'

<FirstQn>:
    name: 'firstquestionn'
    MDLabel:
        font_name : 'Kangwon Light.ttf'
        text: '스테로이드 성분이 들어간 제품을 찾으시나요?'
        font_size: 22
        pos_hint: {'center_x':0.65,'center_y':0.7}

    MDRectangleFlatButton:
        pos_hint: {'center_x':0.5,'center_y':0.5}
        text: 'Yes'
        on_press: root.manager.current = 'lastquestiony'
    MDRectangleFlatButton:
        text: 'No'
        pos_hint: {'center_x':0.5,'center_y':0.3}
        on_press: root.manager.current = 'lastquestionn'

<FirstQyy>:
    name: 'firstquestionyy'

    Image:
        source:'힐텀스카겔.png'
        size_hint: 0.7,0.7
        pos_hint: {'center_x': 0.5, 'center_y': 0.5}

    MDLabel:
        font_name : 'Kangwon Light.ttf'
        text: '힐텀스카겔을 사용하세요!'
        font_size: 22
        pos_hint: {'center_x':0.7,'center_y':0.7}

    MDRectangleFlatButton:
        text: 'Home'
        pos_hint: {'center_x':0.5,'center_y':0.3}
        on_press: root.manager.current = 'firstquestion'

<FirstQnn>:
    name: 'firstquestionnn'
    MDLabel:
        font_name : 'Kangwon Light.ttf'
        text: '항생제가 들어있는 제품을 찾으시나요?'
        font_size: 22
        pos_hint: {'center_x':0.6,'center_y':0.7}

    MDRectangleFlatButton:
        pos_hint: {'center_x':0.5,'center_y':0.5}
        text: 'Yes'
        on_press: root.manager.current = 'otherquestiony'
    MDRectangleFlatButton:
        text: 'No'
        pos_hint: {'center_x':0.5,'center_y':0.3}
        on_press: root.manager.current = 'otherquestionn'

<OtherQy>:
    name: 'otherquestiony'

    Image:
        source:'후시딘.png'
        size_hint: 0.7,0.7
        pos_hint: {'center_x': 0.5, 'center_y': 0.6}

    Image:
        source:'마데카솔케어.png'
        size_hint: 0.7,0.7
        pos_hint: {'center_x': 0.5, 'center_y': 0.45}

    MDLabel:
        font_name : 'Kangwon Light.ttf'
        text: '후시딘 혹은 마데카솔 케어를 사용하세요!'
        font_size: 22
        pos_hint: {'center_x':0.55,'center_y':0.7}
        
    MDRectangleFlatButton:
        text: 'Home'
        pos_hint: {'center_x':0.5,'center_y':0.3}
        on_press: root.manager.current = 'firstquestion'

<OtherQn>:
    name: 'otherquestionn'

    Image:
        source:'마데카솔케어.png'
        size_hint: 0.7,0.7
        pos_hint: {'center_x': 0.5, 'center_y': 0.5}

    MDLabel:
        font_name : 'Kangwon Light.ttf'
        text: '마데카솔 케어을 사용하세요!'
        font_size: 22
        pos_hint: {'center_x':0.75,'center_y':0.7}

    MDRectangleFlatButton:
        text: 'Home'
        pos_hint: {'center_x':0.5,'center_y':0.3}
        on_press: root.manager.current = 'firstquestion'

<LastQy>:
    name: 'lastquestiony'

    Image:
        source:'복합 마데카솔.png'
        size_hint: 0.7,0.7
        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
    
    MDLabel:
        font_name : 'Kangwon Light.ttf'
        text: '복합 마데카솔을 사용하세요!'
        font_size: 22
        pos_hint: {'center_x':0.7,'center_y':0.7}

    MDRectangleFlatButton:
        text: 'Home'
        pos_hint: {'center_x':0.5,'center_y':0.3}
        on_press: root.manager.current = 'firstquestion'

<LastQn>:
    name: 'lastquestionn'

    Image:
        source:'마데카솔겔.png'
        size_hint: 0.7,0.7
        pos_hint: {'center_x': 0.5, 'center_y': 0.5}

    MDLabel:
        font_name : 'Kangwon Light.ttf'
        text: '마데카솔겔을 사용하세요!'
        font_size: 22
        pos_hint: {'center_x':0.7,'center_y':0.7}

    MDRectangleFlatButton:
        text: 'Home'
        pos_hint: {'center_x':0.5,'center_y':0.3}
        on_press: root.manager.current = 'firstquestion'
"""

class FirstQ(Screen):
    pass

class FirstQy(Screen):
    pass

class FirstQyy(Screen):
    pass

class FirstQnn(Screen):
    pass

class FirstQn(Screen):
    pass

class OtherQy(Screen):
    pass

class OtherQn(Screen):
    pass

class LastQy(Screen):
    pass

class LastQn(Screen):
    pass
FirstQyy

# Create the screen manager
sm = ScreenManager()
sm.add_widget(FirstQ(name='firstquestion'))
sm.add_widget(FirstQy(name='firstquestiony'))
sm.add_widget(FirstQn(name='firstquestionn'))
sm.add_widget(FirstQyy(name='firstquestionyy'))
sm.add_widget(FirstQnn(name='firstquestionnn'))
sm.add_widget(LastQy(name='lastquestiony'))
sm.add_widget(LastQy(name='lastquestionn'))
sm.add_widget(OtherQy(name='otherquestiony'))
sm.add_widget(OtherQn(name='otherquestionn'))


class DemoApp(MDApp):

    def build(self):
        screen = Builder.load_string(screen_helper)
        return screen

DemoApp().run()