class Edificio:
  def __del__(self):
    x = str(input('¿Que ciudad desea destruir?'))
    if x == 'New York':
      print('Se ha destruido la ciudad de New York')
    else:
      print('Se ha destruido la ciudad de Los Ángeles')
  def __init__(self, ciudad_New_York, ciudad_Los_Angeles):
    self.ciudad_New_York = ciudad_New_York
    self.ciudad_Los_Angeles = ciudad_Los_Angeles
   
  