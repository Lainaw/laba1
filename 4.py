colors = { 'красный', 'синий', 'жёлтый' }

def isPurple(a, b):
  return a == 'красный' and b == 'синий' or a == 'синий' and b == 'красный'

def isOrange(a, b):
  return a == 'красный' and b == 'жёлтый' or a == 'жёлтый' and b == 'красный'

def isGreen(a, b):
  return a == 'синий' and b == 'жёлтый' or a == 'жёлтый' and b == 'синий'

while (True):
  colorA = input('Введите первый цвет: ')
  colorB = input('Введите второй цвет: ')

  if colorA in colors and colorB in colors:
    if isPurple(colorA, colorB):
      print('Получится фиолетовый!')
    if isOrange(colorA, colorB):
      print('Получится оранжевый!')
    if isGreen(colorA, colorB):
      print('Получится зелёный!')
  else:
    print('Неизвестный базовый цвет...')
