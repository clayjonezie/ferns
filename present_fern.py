from PIL import Image, ImageDraw
import random

size = (3600,3600)
im = Image.new('RGB', size)
draw = ImageDraw.Draw(im)
x, y = random.random(), random.random()

for i in xrange(10000000):
  rand = random.random()
  if rand < 0.01:
    x, y = 0.0, 0.16 * y;
  elif rand < 0.86:
    newx = (0.85 * x) + (0.04 * y)
    newy = (-0.04 * x) + (0.85 * y) + 1.6
    x, y = newx, newy
  elif rand < 0.93:
    newx = (0.2 * x) - (0.26 * y)
    newy = (0.23 * x) + (0.22 * y) + 1.6
    x, y = newx, newy
  else:
    newx = (-0.15 * x) + (0.28 * y)
    newy = (0.26 * x) + (0.24 * y) + 0.44
    x, y = newx, newy

  draw.point(
    (size[0]/2.0  + x*size[0]/10.0, y*size[1]/12.0),
    fill='#0f0')	

im.save("out_present_fern.png", "PNG")

