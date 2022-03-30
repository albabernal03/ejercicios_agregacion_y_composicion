from clases.Edificio_LA import Edificio_LA
from clases.Edificio_NY import Edificio_NY
from clases.Empleado_LA import Empleados_LA
from clases.Edificio_NY import Empleados_NY
from clases.LosAngeles import LosAngeles
from clases.NewYork import NewYork
from clases.inmortal import Yin
from clases.inmortal import Yang

if __name__ == '__main__':
 Edificio_LA()
 Edificio_NY()
 Empleados_LA()
 Empleados_NY()
 LosAngeles()
 NewYork()
 ciudad = str(input('¿Que ciudad deseas destruir, New York o Los Ángeles?'))
 if ciudad == 'New York':
    NY = NewYork()
    del NY
 elif ciudad == 'Los Ángeles':
    LA = LosAngeles()
    del LA
 else:
    print('La opción seleccionada no es válida')

if __name__ == '__main__':
  Yin()
  Yang()



