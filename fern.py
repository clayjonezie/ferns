from PIL import Image, ImageDraw
import random
from os import system
import sys

dim = 300
iters = 500000
size = (dim, dim)

# iter p from 100, 0, 0, 0 to .01 .5 .24 .25

def output_fern():
  x, y = random.random(), random.random()
  color = (0, 255, 0)

  image = Image.new('RGB', size)
  draw = ImageDraw.Draw(image)
  for i in xrange(iters): 
    p1 = p[0]
    p2 = p1 + p[1]
    p3 = p2 + p[2]
    rand = random.random()
    if rand < p1:
      x, y = 0.0, 0.16 * y;
    elif rand < p2:
      newx = (0.85 * x) + (0.04 * y)
      newy = (-0.04 * x) + (0.85 * y) + 1.6   
      x, y = newx, newy
    elif rand < p3:
      newx = (0.2 * x) - (0.26 * y)
      newy = (0.23 * x) + (0.22 * y) + 1.6
      x, y = newx, newy
    else:
      newx = (-0.15 * x) + (0.28 * y)
      newy = (0.26 * x) + (0.24 * y) + 0.44
      x, y = newx, newy
  
    draw.point(
      (size[0]/2.0  + x*size[0]/10.0, y*size[1]/12.0), fill=color)
  image.save("out_fern.png", "PNG")
  print "out_fern.png"

output_fern()
#system("convert -delay 1 -loop 0 *png anim.gif")
