from kivy.app import App
from kivy.uix.image import Image
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button



class Machiavelli(App):
    def build(self):

        class Main_Window:
            self._app_window = GridLayout(cols = 1, size_hint = (0.6, 0.9))
            self._app_window.pos_hint = {'center_x':0.5, 'center_y':0.5}

        class Img:
            self._app_window.add_widget(Image(source='2.jpg'))

        class Greeting:
            self.greeting = Label(text='Hey, what is your name?', color = '#00ffce', font_size = 18)
            self._app_window.add_widget(self.greeting)
            self.user = TextInput(multiline = False, padding_y = (20, 20), size_hint = (1, 0.2))
            self._app_window.add_widget(self.user)

        class Greet_button:
            self.greet = Button(text = 'Greet', color = '#fefefe', font_size = 18, padding_y = (20,20),
                                size_hint = (1, 0.3), background_color = '#3e4290', background_normal = '' )
            self._app_window.add_widget(self.greet)
            self.greet.bind(on_press = self.callback)


        return self._app_window

    def callback(self, instance):
        self.greeting.text = 'Hello ' + self.user.text + '!'


if __name__=='__main__':
    Machiavelli().run()
