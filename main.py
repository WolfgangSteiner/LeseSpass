import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.core.audio import SoundLoader
from functools import partial
import random
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.image import Image
from kivy.core.window import Window
Window.clearcolor = (0.0,0.0,0.125,1.0)

def random_text_color():
    return random.choice(random_text_color.colors)

random_text_color.colors = [(1.0,0,0,1.0), (0,1.0,0,1.0), (0,0,1.0,1.0)]


class WordImage(ButtonBehavior, Image):
    def __init__(self, word, **kwargs):
        super().__init__(**kwargs)
        self.word = word
        self.allow_stretch = False
        self.source = "word_images/%s.png" % word
        self.pos_hint = {'center_y': 0.5, 'center_x': 0.5}


class Card(Button):
    def __init__(self, syllable, **kwargs):
        super().__init__(**kwargs)
        self.font_size = self.height
        self.color = random_text_color()
        self.background_color = (0.75,1.0,1.0,0.5)
        #self.pos_hint = {'center_x': 0.5, 'bottom': .125}
        self.syllable=syllable
        self.sound = SoundLoader.load("sounds/%s.wav" % self.syllable)
        self.text = self.syllable.upper()
        self.sound.volume = 1.0
        self.bind(height=partial(Card.on_height, self))



    def on_press(self):
        self.sound.play()


    def on_height(self, instance, value):
        self.font_size = self.height // 2


class MyApp(App):
    def build(self):
        image_box = FloatLayout()
        image_box.add_widget(WordImage("tomato"))
        image_box.padding = '10sp'
        image_box.size_hint = (1.0, 1.5)

        cards = BoxLayout()
        cards.spacing = '40sp'
        cards.padding = '40sp'
        cards.add_widget(Card("to"))
        cards.add_widget(Card("ma"))
        cards.add_widget(Card("te"))

        root = BoxLayout(orientation='vertical')
        root.add_widget(image_box)
        root.add_widget(cards)
        return root
        #return Label(text='HALLO RASMUS')


if __name__ == '__main__':
    MyApp().run()