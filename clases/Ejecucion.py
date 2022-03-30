from clases.LosAngeles import LosAngeles
from clases.NewYork import NewYork

class ejecucion:
  
 ciudad = str(input('¿Que ciudad deseas destruir, New York o Los Ángeles?'))
 if ciudad == 'New York':
    NY = NewYork()
    del NY
 elif ciudad == 'Los Ángeles':
    LA = LosAngeles()
    del LA
 else:
    print('La opción seleccionada no es válida')