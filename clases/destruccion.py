class Edificio:
  def __del__(self):
    x = str(input('¿Que ciudad desea destruir?'))
    if x == 'New York':
      print('Se ha destruido la ciudad de New York')
    else:
      print('Se ha destruido la ciudad de Los Ángeles')
   
  