import calculator

from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager
from kivy.lang import Builder
from kivy.uix.scrollview import ScrollView
import calculator

class Ui(ScreenManager):
    def calculate_data(self):
        distance = float(self.ids.distance.text)
        speed = float(self.ids.speed.text)
        barrel_length = float(self.ids.barrel_length.text)
        weight = float(self.ids.weight.text)
        diameter = float(self.ids.diameter.text)
        wspeed = float(self.ids.wspeed.text)
        wdirection = float(self.ids.wdirection.text)
        obstacles = int(self.ids.obstacles.text)
        
        print("Distancia:", distance, "Velocidad:", speed, " Longitud del cañón:", barrel_length, " Peso de la munición:", weight, " Diámetro de la munición:", diameter, " Wind speed:", wspeed, " Wind direction:", wdirection, " Obstacles:", obstacles)
        
        t, height, desplazamiento = 0, 0, 0
        t = calculator.time(distance, speed, weight, diameter)
        height = calculator.altura(distance, speed, weight, diameter)
        if obstacles != 0:
            desplazamiento = calculator.viento(True, distance, speed, weight, diameter, obstacles, wdirection, wspeed)
        else:
            desplazamiento = calculator.viento(False, distance, speed, weight, diameter, obstacles, wdirection, wspeed)
            
        print("Tiempo:", t, "Altura:", height, "Desplazamiento:", desplazamiento)
        
        self.ids.time.text = str(t)
        self.ids.height.text = str(height)
        self.ids.desplazamiento.text = str(desplazamiento)
        
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
