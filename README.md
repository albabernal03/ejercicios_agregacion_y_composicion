<h1 align="center">	Ejercicios de composición y agregación</h1>

<h2>Repositorio:</h2>

Este es el link del [repositorio](https://github.com/albabernal03/ejercicios_agregacion_y_composicion)

***
<h2>¿De qué trata esta tarea?</h2>
***

## Índice 

1. ekdf
2. fif
3. jf

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

<img width="812" alt="diagrama catástrofe" src="https://user-images.githubusercontent.com/91721875/160846028-73c5164c-086f-4d85-a9ac-19f701d21389.png">


***


## Ejercicio 2:<a name="id2"></a>

**Opción 1:**

```
class Yin: pass 
class Yang: 
    def __del__(self): 
        print("Yang destruido") 
      
 
yin = Yin() 
yang = Yang() 
yin.yang = yang 
 

print("?") 

print(yang is yin.yang) 
del(yang)

```
**Opción 2:**

