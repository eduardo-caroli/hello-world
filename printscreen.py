import time
import pytest

class printscreen:
    def __init__(self, segundos):
        t = time.gmtime(segundos)
        self.dia_da_semana = t.tm_wday
        minuto = t.tm_hour * 60 + t.tm_min
        self.tempo = minuto

class horario:
    def __init__(self, nome_do_horario, inicio, duracao):
        self.nome = nome_do_horario
        if type(inicio) == str:
            inicio = inicio.split(":")
            horas = int(inicio[0])
            minutos = int(inicio[1])
            minutos += horas*60
            self.inicio = minutos
            self.fim = minutos + duracao


def test_classes():
    printscreen_teste = printscreen(1596108851.0)
    horario_teste = horario("Alfredo", "16:25", 50)
    assert  printscreen_teste.dia_da_semana == 3
    assert  printscreen_teste.tempo == 694
    assert  horario_teste.nome == "Alfredo"
    assert  horario_teste.inicio == 985
    assert  horario_teste.fim == 1035
    

    
        
        
        
        
