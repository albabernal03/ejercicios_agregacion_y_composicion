<h1 align="center">	Ejercicios de composición y agregación</h1>

<h2>Repositorio:</h2>

Este es el link del [repositorio](https://github.com/albabernal03/ejercicios_agregacion_y_composicion)

***
<h2>¿De qué trata esta tarea?</h2>

En esta tarea se nos proponen una serie de ejercicios los cuales se han de resolver a través de la agregación y composición.
***


## Índice 

1. [Ejercicio 1](#id1)
2. [Ejercicio 2](#id2)
3. [Ejercicio 3](#id3)

***


## Ejercicio 1:<a name="id1"></a>

**Enunciado:**
*Modelar lo siguiente. Una empresa es propietaria de varios edificios y emplea a varios empleados. Un edificio está necesariamente ubicado en una ciudad y una ciudad está formada por varios edificios. Empresa, empleado, ciudad y edificio tienen cada uno un nombre. Estas ciudades incluyen New York, donde se encuentran los edificios A y B, y Los Ángeles, donde está el edificio C. Estos tres edificios son propiedad de YooHoo! que emplea a los Sres. Martin, Salim y la Sra. Xing.*


**Código:**
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

**Enunciado:**

*Teniendo en cuenta el siguiente código(se muestra en la tarea), explique por qué el mensaje Yang destruido, se muestra después del signo de interrogación. ¿Qué hay que hacer para que aparezca antes?*

**Código:**

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

**Corrección:**

Lo que he hecho es linkear la clase del Yang correctamente.

**UML:**

<img width="469" alt="inmortal" src="https://user-images.githubusercontent.com/91721875/160868887-9f2539bf-4a81-44e9-9a17-b9ce1b55f33c.png">


***

## Ejercicio 3:<a name="id3"></a>

**Enunciado:**

*Modifique las clases Ventana y ParedCortina para que usen esta nueva clase-interfaz Cristal.*

**Código:**

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
