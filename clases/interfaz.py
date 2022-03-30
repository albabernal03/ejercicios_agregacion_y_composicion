class Interfaz_cristal:
  class Pared:
    def __init__(self, orientacion):
        self.orientacion = orientacion
        self.ventanas = []
  class Ventana:
    def __init__(self, pared, superficie):
        self.pared = pared
        self.superficie = superficie
        self.pared.ventanas.append(self)
  class Casa:
    def __init__(self, paredes):
        self.paredes = paredes

    def superficie_cristal(self):
        superficie = 0
        for pared in self.paredes:
            for ventana in pared.ventanas:
                superficie += ventana.superficie
        return superficie

  pared_norte = Pared("NORTE")
  pared_oeste = Pared("OESTEE")
  pared_sur = Pared("SUR")
  pared_este = Pared("ESTE")
  ventana_norte = Ventana(pared_norte, 0.5)
  ventana_oeste = Ventana(pared_oeste, 1)
  ventana_sur = Ventana(pared_sur, 2)
  ventana_este = Ventana(pared_este, 1)
  casa = Casa([pared_norte, pared_oeste, pared_sur, pared_este])
  print(casa.superficie_cristal())
  
  class ParedCortina(Pared, Ventana):
    def __init__(self, orientacion, superficie):
      Interfaz_cristal.Pared.__init__(self, orientacion)
      Interfaz_cristal.Ventana.__init__(self, self, superficie, "Ninguna")

print(Interfaz_cristal.Pared.__init__('self', 'orientacion'))
print(Interfaz_cristal.Ventana.__init__('self', 'pared', 'superficie'))
print(Interfaz_cristal.Casa.__init__('self', 'paredes'))
print(Interfaz_cristal.ParedCortina.__init__('Pared', 'Ventana'))

