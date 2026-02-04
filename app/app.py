from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
import random

# Sample Bible verses
verses = [
    "For God so loved the world, that he gave his only Son. - John 3:16",
    "I can do all things through Christ who strengthens me. - Philippians 4:13",
    "The Lord is my shepherd; I shall not want. - Psalm 23:1",
    "Trust in the Lord with all your heart. - Proverbs 3:5"
]

class VerseHubLayout(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.padding = 20
        self.spacing = 20

        self.title = Label(text="VerseHub", font_size=32, size_hint=(1, 0.2))
        self.add_widget(self.title)

        self.verse_label = Label(text=self.get_random_verse(), font_size=20)
        self.add_widget(self.verse_label)

        self.button = Button(text="Get Another Verse", size_hint=(1, 0.2))
        self.button.bind(on_press=self.update_verse)
        self.add_widget(self.button)

    def get_random_verse(self):
        return random.choice(verses)

    def update_verse(self, instance):
        self.verse_label.text = self.get_random_verse()

class VerseHubApp(App):
    def build(self):
        return VerseHubLayout()

if __name__ == "__main__":
    VerseHubApp().run()
