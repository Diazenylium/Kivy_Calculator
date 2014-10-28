from __future__ import division
import math
import re

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView

Builder.load_file('main.kv')


class LayoutWidget(BoxLayout):
    @staticmethod
    def evaluate(n):
        # .strip makes 01 -> 1 to evade 'invalid token' error.
        # .replace changes ^ to ** to evaluate
        n = n.strip('0').replace('^', '**')
        if eval(n):
            return str(eval(n))
        else:
            return '0'


class Calculator(App):
    def build(self):
        return LayoutWidget()

if __name__ == '__main__':
    Calculator().run()
