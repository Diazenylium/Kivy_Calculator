from __future__ import division
# -*- coding: utf-8 -*-
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
    return math.gamma(x+1)


class LayoutWidget(BoxLayout):
    @staticmethod
    def evaluate(n):
        # .strip makes 01 -> 1 to evade 'invalid token' error.
        # .replace changes ^ to ** to evaluate exponents
        # we also need to do a thing where it evaluates e and phi instead of just adding them to the screen
        if '!' in n:
            factorial_string = str(re.findall(r'\((.*?)\!', str(n)))[2:-3]
            n = n.replace(factorial_string, 'factorial(' + factorial_string + ')').replace('!', '')

        n = n.lstrip('0').replace('^', '**').replace('Φ', str((1+5**.5)/2))
        try:
            return str(eval(n))
        except:
            return 'YOU ARE A BAD CHILD'

    def until_other(x):
        i = -1
        while x[i:].isdigit():
            i -= 1
        return x[i+1:]


class Calculator(App):
    def build(self):
        return LayoutWidget()

if __name__ == '__main__':
    Calculator().run()