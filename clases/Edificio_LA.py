class Edificio_LA:
    def __del__(self):
        print('Destrucción {}'.format(self.name))
    def __init__(self,name):
        self.name=name