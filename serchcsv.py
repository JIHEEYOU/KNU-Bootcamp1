
import os
from ast import Try
from tkinter import Label
from turtle import textinput
from kivymd.app import MDApp
from kivy.app import App
from kivymd.uix.screen import Screen
from kivymd.uix.button import MDRectangleFlatButton,MDFlatButton
from kivymd.uix.dialog import MDDialog
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window

pill = {'샤이닝정':'Effective for dysfunctional and convulsive pain in female reproductive machinery such as seizure pain or biliary tract system, urinary system, and menstrual distress in gastrointestinal diseases. One to two tablets per adult are administered three times a day.',
'부스코판 플러스정':'Effective for dysfunctional and convulsive pain in female reproductive machinery such as seizure pain or biliary tract system, urinary system, and menstrual distress in gastrointestinal diseases. One to two tablets per adult are administered three times a day.',
'탁센이브연질캡슐':'Headache, toothache, post-tooth pain (pain), sore throat, ear pain, joint pain, neuralgia, back pain, muscle pain, shoulder pain, percussion pain, fracture pain, sprain pain, menstrual pain, pain, pain in trauma, chills (cold and trembling symptoms) and fever.',
'이지엔6이브연질캡슐':'Headache, toothache, post-tooth pain (pain), sore throat, ear pain, joint pain, neuralgia, back pain, muscle pain, shoulder pain, percussion pain, fracture pain, sprain pain, menstrual pain, pain, pain in trauma, chills (cold and trembling symptoms) and fever.',
'탁센400이부프로펜연질캡슐':'Effective for fever and pain (pain), urinary (back) pain, menstrual pain, rheumatoid arthritis, combustible (young or young) rheumatoid arthritis, osteoarthritis (degenerative joint disease), and postoperative pain (pain).',
'지르텍':'effective in seasonal and multi-year allergic rhinitis, allergic conjunctivitis, chronic idiopathic urticaria, skin irritation, eczema, and dermatitis.',
'클라리틴':'effective for allergic rhinitis (sneezing, nasal congestion, itching, burning of the eyes)',
'힐텀스카겔':'an ointment for burns',
'후시딘':'an ointment containing ointment',
'마데카솔 케어':'an ointment containing ointment',
'메디폼':'Hydrophilic foam dressing band that protects wounds from external contamination.',
'복합 마데카솔':'Initial treatment of corticoid reactive skin disease secondary to infection by neomycin-sensitive bacteria: dermatitis, effective against infected wounds, and an appropriate amount is applied to the affected area 1-2 times a day.',
'마데카솔겔':'Gel for the treatment of wounds, supplementary parts of skin ulcers.Apply an appropriate amount once or twice a day to the disease rea.',
'맨소래담 로션':'Effective for sprains, bruises, and muscle pain. Apply about 1 to 4 cm thin three times a day and once a day to the affected area, rub lightly so that it permeates well, and if there is no doctor\'s instruction, the treatment period should not exceed 5 days.',
'신신파스 COOL':'Pain and anti-inflammatory (anti-inflammatory): Effective for sprains, bruises, muscle pain, joint pain, fracture pain, lumbar pain, shoulder stiffness, neuralgia, and rheumatoid pain. Apply it once or twice a day to the affected area (the diseased area). Restrict use on infants under 30 months old, dermatitis caused by eczema, lacquer, and other wounds.',
'신신파스 HOT':'Pain and anti-inflammatory (anti-inflammatory): It is effective in sprain (pim), bruise, muscle pain, joint pain, fracture pain, back pain, shoulder pain, neuralgia, and rheumatoid pain. Attach it to the affected area (disease area) once to twice a day.',
'신신파스 아렉스':'This medicine is used for shoulder stiffness, back pain, neuralgia, rheumatism, bruise, sprain, muscle pain, and arthritis. If skin rashes, redness, itching, or pain appear due to congestion, stop using immediately.',
'닥터 배아제':'It is effective for indigestion, loss of appetite (slack of appetite), overeating, indigestion, digestion promotion, and gastric bloating due to indigestion. Take one tablet once per adult three times a day after meals. Not available for children under 7 years of age.',
'배아제':'It is effective for indigestion, loss of appetite (slack of appetite), overeating, indigestion, digestion promotion, and gastric bloating due to indigestion.',
'훼스탈 플러스정':'It is effective for indigestion, loss of appetite (slack of appetite), overeating, diet (stomach), digestion promotion, and gastric bloating due to indigestion.',
'큐자임정':'It is effective for loss of appetite, stomach bloating, indigestion, overeating, indigestion, nausea, vomiting, digestive stimulation, and indigestion',
'가스명수에프액':'It is effective for loss of appetite (deprivation), gastric bloating, indigestion, overeating, vegetation (stomach), nausea, and vomiting.',
'가스활명수큐액':'It is effective for loss of appetite (slack of appetite), gastric bloating, indigestion, overeating, indigestion, nausea, and vomiting.',
'아렉스':'It is easy to attach to various areas and curved parts of the body such as shoulder, knee, waist, neck, and thigh, and provides a solution to various pains such as muscle pain, neuralgia, rheumatism, arthralgia, stiff shoulder, and back pain that appear periodically and repeatedly.'}#여기다가 약 정보 입력하기

fontName = '강원교육모두 Light.ttf'

username_helper = '''
MDTextField:
    hint_text: 'Enter the drug name'
    # helper_text: 'or click on forgor username'
    helper_text_mode: 'on_focus'#클릭 전에 보이게 할지 말지
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
        if  self.username.text == '':
            chech_string = 'Please enter a pill name'
        else:#elif 써서 약 이름과 동일한지 구분하기 
            pill_velue = pill.get(self.username.text, 'can\'t find it')
            chech_string = pill_velue
    
        close_button = MDFlatButton(text = '닫기', on_release = self.close_dialog, font_name=fontName)
        

        self.dialog = MDDialog(title = 'Pill name serch', text = chech_string, size_hint=(0.7, 1), buttons = [close_button])#여기서 한글로 안 나옴 이유는 모름
        self.dialog.open(font_name = fontName)
    def close_dialog(self,obj):
        self.dialog.dismiss()

DemoApp().run()