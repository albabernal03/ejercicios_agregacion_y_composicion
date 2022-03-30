<h1 align="center">	Ejercicios de composición y agregación</h1>

<h2>Repositorio:</h2>

Este es el link del [repositorio](https://github.com/albabernal03/ejercicios_agregacion_y_composicion)

***
<h2>¿De qué trata esta tarea?</h2>
***

## Índice 

1. [Ejercicio 1](#id1)
2. [Ejercicio 2](#id2)
3. [Ejercicio 3](#id3)

***


## Ejercicio 1:<a name="id1"></a>

```
class NewYork:
    def __del__(self):
        print('Se destruye la ciudad de New York')
    
    def __init__(self):
        self.edificios= [Edificio_NY(name) for name in ['edifcio A', 'edificio B']]
        self.empleados= [Empleados_NY(name) for name in ['Sres.Martin', 'Salim']]

class Edificio_NY:
    def __del__(self):
        print('Destrucción {}'.format(self.name))
    def __init__(self,name):
        self.name=name

class Empleados_NY:
    def __del__(self):
        print('Ha muerto {}'.format(self.name)) 
    def __init__(self,name):
        self.name = name



class LosAngeles:
    def __del__(self):
        print('Se destruye la ciudad de Los Ángeles')
    
    def __init__(self):
        self.edificios= [Edificio_LA(name) for name in ['edifcio C']]
        self.empleados= [Empleados_LA(name) for name in ['Sra.Xing']]

class Edificio_LA:
    def __del__(self):
        print('Destrucción {}'.format(self.name))
    def __init__(self,name):
        self.name=name

class Empleados_LA:
    def __del__(self):
        print('Ha muerto {}'.format(self.name)) 
    def __init__(self,name):
        self.name = name



ciudad = str(input('¿Que ciudad deseas destruir, New York o Los Ángeles?'))
if ciudad == 'New York':
    NY = NewYork()
    del NY
elif ciudad == 'Los Ángeles':
    LA = LosAngeles()
    del LA
else:
    print('La opción seleccionada no es válida')

```

**UML:**

<img width="804" alt="diagrama catastrofe" src="https://user-images.githubusercontent.com/91721875/160852850-2d2ba61f-b223-4bd8-bc70-31b5487c4be2.png">



***


## Ejercicio 2:<a name="id2"></a>

```

class Yin: pass 
class Yang: 
    def __del__(self): 
        print("Yang destruido") 
      
 
yin = Yin() 
yang = Yang() 
yin.yang = yang 
 

print(yang is yin.yang) 
Yang.__del__(yang)
print("?") 
```

**UML:**

<img width="469" alt="inmortal" src="https://user-images.githubusercontent.com/91721875/160868887-9f2539bf-4a81-44e9-9a17-b9ce1b55f33c.png">


***

## Ejercicio 3:<a name="id3"></a>


```
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


```

**UML:**

<img width="654" alt="herencia" src="https://user-images.githubusercontent.com/91721875/160872300-fe19c7ac-de31-4ddc-ba37-85f2b98b58b6.png">


***
