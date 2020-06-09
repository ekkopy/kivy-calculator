# -*- coding: utf-8 -*-

import kivy

from kivy.app import App
from kivy.config import Config
from kivy.uix.gridlayout import GridLayout
from math import factorial as fatorial

kivy.require('1.11.1')

# Configurações sobre a janela e redimensionamento
Config.set('graphics', 'resizable', 1)

class CalulatorGridLayout(GridLayout):

    def factorial(self, number):
        if number:
            try:
                number = eval(number)
                if number <= 0:
                    self.display.text = str(1)
                else:
                    facnumber = fatorial(number)
                    self.display.text = str(facnumber)
            except Exception as e:
                self.display.text = "Algum erro ocorreu - Verifique o console!"
                print(e)
    
    def percent(self, percent):
        if percent:
            try :
                percent = eval(percent)
                total = percent / 100.0
                self.display.text = str(total)
            except Exception as e:
                pass
     
    def calculate(self, number):
        if number:
            try :
                self.display.text = str(eval(number))
            except Exception as e:
                self.display.text = "Algum erro ocorreu - Verifique o console!"
                print(e)

class CalculatorApp(App):
    
    def build(self):
        return CalulatorGridLayout()

# run =)
CalculatorApp().run()