import math

def time(distancia, velocidad_salida, peso, diametro):
    mps = velocidad_salida / 3.2808399
    tiempo = (2 * distancia) / (mps + math.sqrt(mps ** 2 - 4 * ((-0.5 * 0.001 * math.pi * (diametro/2) ** 2) / (0.001 * peso * 0.47))))
    return tiempo
    
def altura(distancia: int, velocidad_salida: int, peso: int, diametro: int):
    tiempo = time(distancia, velocidad_salida, peso, diametro)
    altura = (0.5 * 9.81 * tiempo ** 2)
    return altura

def viento(arboles: bool, distancia: int, velocidad_salida: int, peso: int, diametro: int, numarboles:int, angulo_viento:int, velocidad_viento: float):
    tiempo = time(distancia, velocidad_salida, peso, diametro)

    if arboles:
        reduccion_viento = 0.05  # (sujeto a modificaciones) cada arbol reduce el viento un 5% mas o menos, ya que son distancias cortas y si hay 50 arboles es practicamente que no hay viento
        velocidad_viento *= (1 - numarboles * reduccion_viento)
    
    desviacion = velocidad_viento * tiempo
    
    desviacion_horizontal = desviacion * math.sin(math.radians(angulo_viento))
    
    return desviacion_horizontal