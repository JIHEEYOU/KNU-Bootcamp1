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
    FirstQ_s:
    FirstQy_s: 
    FirstQn_s:
    FirstQyy_s:
    FirstQnn_s:
    OtherQy_s:
    OtherQn_s:
    LastQy_s:
    LastQn_s:
    FirstQ2yyy_s:
    FirstQ2yyn_s

<FirstQ_s>:
    name: 'firstquestion_s'
    MDLabel:
        font_name: 'Kangwon Light.ttf'
        text: '소화제가 필요하시군요,'
        font_size: 22
        pos_hint: {'center_x':0.75,'center_y':0.75} #x축 가운데로

    MDLabel:
        font_name: 'Kangwon Light.ttf'
        text: ' 알약 형태의 약을 원하시나요?'
        font_size: 22
        pos_hint: {'center_x':0.7,'center_y':0.7} #x축 가운데로

    MDRectangleFlatButton:
        pos_hint: {'center_x':0.5,'center_y':0.5}
        text: 'Yes'
        on_press: root.manager.current = 'firstquestiony_s'
    
    MDRectangleFlatButton:
        text: 'No'
        pos_hint: {'center_x':0.5,'center_y':0.3}
        on_press: root.manager.current = 'firstquestionn_s'
    
<FirstQy_s>:
    name: 'firstquestiony_s'
    MDLabel:
        font_name : 'Kangwon Light.ttf'
        text: '가스가 차시나요?'
        font_size: 22
        pos_hint: {'center_x':0.8,'center_y':0.7}

    MDRectangleFlatButton:
        pos_hint: {'center_x':0.5,'center_y':0.5}
        text: 'Yes'
        on_press: root.manager.current = 'firstquestionyy_s'
    MDRectangleFlatButton:
        text: 'No'
        pos_hint: {'center_x':0.5,'center_y':0.3}
        on_press: root.manager.current = 'firstquestionnn_s'

<FirstQn_s>:
    name: 'firstquestionn_s'
    MDLabel:
        font_name : 'Kangwon Light.ttf'
        text: '임산부이신가요?'
        font_size: 22
        pos_hint: {'center_x':0.8,'center_y':0.7}

    MDRectangleFlatButton:
        pos_hint: {'center_x':0.5,'center_y':0.5}
        text: 'Yes'
        on_press: root.manager.current = 'lastquestiony_s'
    MDRectangleFlatButton:
        text: 'No'
        pos_hint: {'center_x':0.5,'center_y':0.3}
        on_press: root.manager.current = 'lastquestionn_s'

<FirstQyy_s>:
    name: 'firstquestionyy_s'
    MDLabel:
        font_name : 'Kangwon Light.ttf'
        text: '기름진 음식을 드셨나요?'
        font_size: 22
        pos_hint: {'center_x':0.75,'center_y':0.7}

    MDRectangleFlatButton:
        pos_hint: {'center_x':0.5,'center_y':0.5}
        text: 'Yes'
        on_press: root.manager.current = 'firstquestion2yyy_s'
    MDRectangleFlatButton:
        text: 'No'
        pos_hint: {'center_x':0.5,'center_y':0.3}
        on_press: root.manager.current = 'firstquestion2yyn_s'

<FirstQ2yyy_s>
    name: 'firstquestion2yyy_s'

    Image:
        source:'닥터베아제.png'
        size_hint: 0.7,0.7
        pos_hint: {'center_x': 0.4, 'center_y': 0.55}

    MDLabel:
        font_name : 'Kangwon Light.ttf'
        text: '닥터베아제를 복용하세요!'
        font_size: 22
        pos_hint: {'center_x':0.75,'center_y':0.7}

    MDRectangleFlatButton:
        text: 'Home'
        pos_hint: {'center_x':0.5,'center_y':0.3}
        on_press: root.manager.current = 'firstquestion_s'
        
<FirstQ2yyn_s>
    name: 'firstquestion2yyn_s'

    Image:
        source:'베아제.png'
        size_hint: 0.7,0.7
        pos_hint: {'center_x': 0.55, 'center_y': 0.5}

    MDLabel:
        font_name : 'Kangwon Light.ttf'
        text: '베아제를 복용하세요!'
        font_size: 22
        pos_hint: {'center_x':0.75,'center_y':0.7}

    MDRectangleFlatButton:
        text: 'Home'
        pos_hint: {'center_x':0.5,'center_y':0.3}
        on_press: root.manager.current = 'firstquestion_s'

<FirstQnn_s>:
    name: 'firstquestionnn_s'
    MDLabel:
        font_name : 'Kangwon Light.ttf'
        text: '과식을 하셨나요?'
        font_size: 22
        pos_hint: {'center_x':0.8,'center_y':0.7}

    MDRectangleFlatButton:
        pos_hint: {'center_x':0.5,'center_y':0.5}
        text: 'Yes'
        on_press: root.manager.current = 'otherquestiony_s'
    MDRectangleFlatButton:
        text: 'No'
        pos_hint: {'center_x':0.5,'center_y':0.3}
        on_press: root.manager.current = 'otherquestionn_s'

<OtherQy_s>:
    name: 'otherquestiony_s'

    Image:
        source:'훼스탈 플러스정.png'
        size_hint: 0.7,0.7
        pos_hint: {'center_x': 0.55, 'center_y': 0.5}

    MDLabel:
        font_name : 'Kangwon Light.ttf'
        text: '훼스탈 플러스 정을 복용하세요!'
        font_size: 22
        pos_hint: {'center_x':0.7,'center_y':0.7}

    MDRectangleFlatButton:
        text: 'Home'
        pos_hint: {'center_x':0.5,'center_y':0.3}
        on_press: root.manager.current = 'firstquestion_s'

<OtherQn_s>:
    name: 'otherquestionn_s'

    Image:
        source:'큐자임정.png'
        size_hint: 0.7,0.7
        pos_hint: {'center_x': 0.55, 'center_y': 0.5}

    MDLabel:
        font_name : 'Kangwon Light.ttf'
        text: '큐자임정을 복용하세요!'
        font_size: 22
        pos_hint: {'center_x':0.75,'center_y':0.7}

    MDRectangleFlatButton:
        text: 'Home'
        pos_hint: {'center_x':0.5,'center_y':0.3}
        on_press: root.manager.current = 'firstquestion_s'

<LastQy_s>:
    name: 'lastquestiony_s'

    Image:
        source:'까스명수.png'
        size_hint: 0.7,0.7
        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
    
    MDLabel:
        font_name : 'Kangwon Light.ttf'
        text: '까스 명수를 복용하세요!'
        font_size: 22
        pos_hint: {'center_x':0.75,'center_y':0.7}

    MDRectangleFlatButton:
        text: 'Home'
        pos_hint: {'center_x':0.5,'center_y':0.3}
        on_press: root.manager.current = 'firstquestion_s'

<LastQn_s>:
    name: 'lastquestionn_s'

    Image:
        source:'까스활명수.png'
        size_hint: 0.7,0.7
        pos_hint: {'center_x': 0.5, 'center_y': 0.5}

    MDLabel:
        font_name : 'Kangwon Light.ttf'
        text: '까스활명수를 복용하세요!'
        font_size: 22
        pos_hint: {'center_x':0.75,'center_y':0.7}

    MDRectangleFlatButton:
        text: 'Home'
        pos_hint: {'center_x':0.5,'center_y':0.3}
        on_press: root.manager.current = 'firstquestion_s'
"""

class FirstQ_s(Screen):
    pass

class FirstQy_s(Screen):
    pass

class FirstQyy_s(Screen):
    pass

class FirstQnn_s(Screen):
    pass

class FirstQn_s(Screen):
    pass

class OtherQy_s(Screen):
    pass

class OtherQn_s(Screen):
    pass

class LastQy_s(Screen):
    pass

class LastQn_s(Screen):
    pass

class FirstQ2yyy_s(Screen):
    pass

class FirstQ2yyn_s(Screen):
    pass

#FirstQyy_s
FirstQ_s

# Create the screen manager
sm = ScreenManager()
sm.add_widget(FirstQ_s(name='firstquestion_s'))
sm.add_widget(FirstQy_s(name='firstquestiony_s'))
sm.add_widget(FirstQn_s(name='firstquestionn_s'))
sm.add_widget(FirstQyy_s(name='firstquestionyy_s'))
sm.add_widget(FirstQnn_s(name='firstquestionnn_s'))
sm.add_widget(LastQy_s(name='lastquestiony_s'))
sm.add_widget(LastQy_s(name='lastquestionn_s'))
sm.add_widget(OtherQy_s(name='otherquestiony_s'))
sm.add_widget(OtherQn_s(name='otherquestionn_s'))
sm.add_widget(FirstQ2yyy_s(name='firstquestion2yyn_s'))
sm.add_widget(FirstQ2yyn_s(name='firstquestion2yyy_s'))



class DemoApp(MDApp):

    def build(self):
        screen = Builder.load_string(screen_helper)
        return screen

DemoApp().run()
