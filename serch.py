
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

pill = {'tylenol':'This medicine is a concern, neuralgia, neuralgia, menstrual pain, neuralgia, pain and neuralgia, pain and neuralgia.','케토톱플라스타':'파스','노스카나겔':'연소 / 여드름흉터','아렌스대형':'파스','후시딘연고':'연고','비판텐연고':'연고 / 피부염'}#여기다가 약 정보 입력하기

# CLabel.register('Kfont',                              # alias
#                 fn_regular='강원교육모두 Light.ttf',  # regular font
#                 fn_italic=None,                             # italic font
#                 fn_bold=None,                               # bold font
#                 fn_bolditalic=None)
fontName = '강원교육모두 Light.ttf'

username_helper = '''
MDTextField:
    id: text_field_error
    hint_text: 'Enter the drug name'
    hint_text: "Helper text on error (press 'Enter')"
    helper_text_mode: "on_error"
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
        self.screen.ids.text_field_error.bind(on_text_validate=self.set_error_message,on_focus=self.set_error_message)
        self.screen.ids.text_field_error.error = True
        print( self.username.text)
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