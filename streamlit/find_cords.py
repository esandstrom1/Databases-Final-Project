


coordinates = []

width = 40
height = 35
spacer = 3
count = 7

x = 120
y = 195
origin = [x,y]

for i in range(count):
  coordinates.append(origin)

  x_second = origin[0] + width
  y_second = origin[1] + height

  coordinates.append([x_second, y_second])

  origin[0] += width + spacer

print(coordinates)