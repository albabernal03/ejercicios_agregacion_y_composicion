from Edificio_LA import Edificio_LA
from Empleado_LA import Empleados_LA

class LosAngeles:
    def __del__(self):
        print('Se destruye la ciudad de Los Ángeles')
    
    def __init__(self):
        self.edificios= [Edificio_LA(name) for name in ['edifcio C']]
        self.empleados= [Empleados_LA(name) for name in ['Sra.Xing']]
