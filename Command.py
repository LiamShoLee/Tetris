#Command Class for Tetris
from abc import ABCMeta, abstractmethod


class IButton(metaclass = ABCMeta):
   
    @staticmethod 
    @abstractmethod
    def execute():
        #the function name for button presses
