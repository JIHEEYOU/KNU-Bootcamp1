import os
from ast import Try
import subprocess
import requests
from tkinter import Label
from turtle import textinput
import urllib.request as urllib
from kivymd.app import MDApp
from kivy.app import App
from kivy.core.window import Window
from kivymd.uix.screen import Screen
from kivymd.uix.button import MDRectangleFlatButton,MDFlatButton
from kivymd.uix.dialog import MDDialog
from kivy.lang import Builder
from tkinter import E
from kivy.uix.boxlayout import BoxLayout


def classify(text):
    key = "88891da0-1e14-11ed-9449-f99ca48f45151604e192-ebc0-4963-956a-a3178fe94692"#머신러닝 포키즈에서 따온 키값
    url = "https://machinelearningforkids.co.uk/api/scratch/"+ key + "/classify"

    response = requests.get(url, params={ "data" : text })

    if response.ok:
        responseData = response.json()
        topMatch = responseData[0]
        return topMatch
    else:
        response.raise_for_status()

chatbot_dic={
    'digestive_medicine': '소화제가 필요하시네요',
    'menstrual_pain_medication':'생리통약이 필요하시네요',
    'antiallergic_drug': '알레르기 약이 필요하시네요',
    'ointment': '연고가 필요하시네요',
    'pain_relief_patch': '파스가 필요하시네요'
    }

fontName = '강원교육모두 Light.ttf'

username_helper = '''
MDTextField:
    hint_text: 'Enter your symptoms'
    # helper_text: 'or click on forgor username'# hint_text 외에 또 할말 있으면 적기
    helper_text_mode: 'on_focus'#클릭 전에 보이게 할지 말지
    # icon_right: 'android'
    icon_irght_color: app.theme_cls.primary_color
    pos_hint: {'center_x':0.42,'center_y':0.7}
    size_hint_x: None 
    width: 230
    font_name: '강원교육모두 Light.ttf'
    
'''

Window.size = (350,600)
class DemoApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette="Green"
        screen = Screen()

        button = MDRectangleFlatButton(text = '찾기',pos_hint={'center_x': 0.84, 'center_y': 0.705},
                                        on_release=self.show_data,font_name = fontName)
        self.username = Builder.load_string(username_helper)
        screen.add_widget(self.username)
        screen.add_widget(button)
        return screen


    def show_data(self,obj):
        demo=classify(self.username.text)
        label = demo["class_name"]
        confidence = demo["confidence"]
        if confidence<40:
            print('  [포켓 약국]: 잘 모르겠습니다, 증상을 다시 입력해주세요')#여기서 경고창 나오게
        else:
            print(f'[포켓 약국]:{chatbot_dic[label]}')
            print ("result: '%s' with %d%% confidence\n" % (label, confidence))

        if  label == '':
            chech_string = 'Please enter a pill name'

        elif label == 'digestive_medicine' :#소화제
            subprocess.call("digestive_medicine.py",shell=True)#digestive_medicine을 실행
            App.get_running_app().stop()#종료

        elif label == 'menstrual_pain_medication' :#생리통약
            subprocess.call("menstrual_pain_medication.py",shell=True)
            App.get_running_app().stop()

        elif label == 'antiallergic_drug' :#알레르기
            subprocess.call("antiallergic_drug.py",shell=True)
            App.get_running_app().stop()

        elif label == 'ointment' :#연고
            subprocess.call("ointment.py",shell=True)
            App.get_running_app.stop()

        elif label == 'pain_relief_patch' :#파스
            subprocess.call("pain_relief_patch.py",shell=True)
            App.get_running_app().stop()
        else:
            self.dialog = MDDialog(title = 'Pill name serch', text = label, size_hint=(0.7, 1), buttons = [close_button])#여기서 한글로 안 나옴 이유는 모름
            self.dialog.open(font_name = fontName)
        
    def close_dialog(self,obj):
            self.dialog.dismiss()
DemoApp().run()
