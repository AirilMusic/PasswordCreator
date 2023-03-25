import calculator

from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager
from kivy.lang import Builder
from kivy.uix.scrollview import ScrollView
import calculator
#print("vertical:", calculator.altura(100, 450, 0.5, 0.6))
#print("horizontal:", calculator.viento(True, 100, 450, 0.5, 0.6, 5, 90, 10))

class Ui(ScreenManager):
    def calculate_data(self):
        distance = float(self.ids.distance.text)
        speed = float(self.ids.speed.text)
        barrel_length = float(self.ids.barrel_length.text)
        weight = float(self.ids.weight.text)
        diameter = float(self.ids.diameter.text)
        
        print("Distancia:", distance, "Velocidad:", speed, " Longitud del cañón:", barrel_length, " Peso de la munición:", weight, " Diámetro de la munición:", diameter)

class MainApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = 'Dark'
        self.theme_cls.primary_palette = 'Teal'
        Builder.load_file('design.kv')

        return Ui()

    def calculate_data(self):
        self.root.calculate_data()

if __name__ == '__main__':
    MainApp().run()