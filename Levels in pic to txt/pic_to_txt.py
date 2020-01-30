from PIL import Image

sprites = dict()
sprites[(255, 255, 255)] = '.'
sprites[(0, 0, 0)] = 'h'  # House
############## "e" Piranha
sprites[(34, 177, 76)] = 'g'  # grass
sprites[(185, 122, 87)] = 'd'  # dirty
sprites[(127, 127, 127)] = 's'  # stone
sprites[(237, 28, 36)] = "u"  # улитка
sprites[(255, 242, 0)] = 'o'  # оса
sprites[(143, 113, 48)] = 'p'  # Платформа
sprites[(163, 73, 164)] = 's'  # Шипы
sprites[(0, 162, 232)] = 'c'  # сундук
sprites[(15, 240, 223)] = '@'  # Player

print("Введите название файла")
name = input()
image = Image.open(name)
x, y = image.size
pix = image.load()
result = ""
for j in range(y):
    for i in range(x):
        rgb = pix[i, j]
        try:
            result += sprites[rgb]
        except Exception as e:
            raise Exception(f"Нету {rgb}")
    result += '\n'

with open(name.rsplit('.', maxsplit=1)[0], 'w') as f:
    f.write(result)
