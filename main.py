from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.config import Config

Config.set('graphics', 'resizable', 0)
Config.set('graphics', 'width', 400)
Config.set('graphics', 'height', 500)


class CalApp(App):
    def add_number(self):

    def build(self):
        # Создаем BoxLayout что бы поместить в него label
        bl = BoxLayout(orientation='vertical', padding=10)

        gl = GridLayout(cols=4, spacing=3, size_hint=(1, .6))

        self.lbl = Label(text='0', font_size=40, halign='right', valign='center', size_hint=(1, .4),
                         text_size=(400 - 50, 500 * .4 - 50))

        # Добавляем в BoxLayout виджет label
        bl.add_widget(self.lbl)

        # Кнопки калькулятора
        gl.add_widget(Button(text='7', on_press = self.add_number))
        gl.add_widget(Button(text='8', on_press = self.add_number))
        gl.add_widget(Button(text='9', on_press = self.add_number))
        gl.add_widget(Button(text='X'))

        gl.add_widget(Button(text='4', on_press = self.add_number))
        gl.add_widget(Button(text='5', on_press = self.add_number))
        gl.add_widget(Button(text='6', on_press = self.add_number))
        gl.add_widget(Button(text='-'))

        gl.add_widget(Button(text='1', on_press = self.add_number))
        gl.add_widget(Button(text='2', on_press = self.add_number))
        gl.add_widget(Button(text='3', on_press = self.add_number))
        gl.add_widget(Button(text='+'))

        gl.add_widget(Widget())
        gl.add_widget(Button(text='0', on_press = self.add_number))
        gl.add_widget(Button(text='.'))
        gl.add_widget(Button(text='='))

        bl.add_widget(gl)
        return bl


if __name__ == '__main__':
    CalApp().run()
