from __future__ import division
from decimal import Decimal, getcontext
import math
import re

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView

Builder.load_file('main.kv')


def factorial(x):
    walrus = 1
    if x == 0:
        walrus = 1
    for i in range(1, x+1):
        walrus *= i
    return walrus


class LayoutWidget(BoxLayout):
    @staticmethod
    def until_other(x):
        i = -1
        while x[i:].isdigit():
            i -= 1
        return x[i+1:]

    def evaluate(n):
        # .strip makes 01 -> 1 to evade 'invalid token' error.
        # .replace changes ^ to ** to evaluate exponents
        n = n.lstrip('0').replace('^', '**')
        if eval(n):
            return str(eval(n))
        else:
            return '0'


class Calculator(App):
    def build(self):
        return LayoutWidget()

if __name__ == '__main__':
    Calculator().run()
