
class Empleados_LA:
    def __del__(self):
        print('Ha muerto {}'.format(self.name)) 
    def __init__(self,name):
        self.name = name