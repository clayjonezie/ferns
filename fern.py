from PIL import Image, ImageDraw
import random
from os import system
import sys

dim = 1000
iters = 500000
size = (dim, dim)

frames = 50
# iter p from 100, 0, 0, 0 to .01 .5 .24 .25
delta = 1.0 / frames
ps = [[1.0 - .98 * delta * x, 
      0.85 * delta * x, 
      0.07 * delta * x, 
      0.04 * delta * x] for x in xrange(frames)]

def output_fern(i, p):
  print p
  x, y = random.random(), random.random()
  color = (0, 255, 0)

  image = Image.new('RGB', size)
  draw = ImageDraw.Draw(image)
  for q in xrange(iters): 
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
  image.save("out_fern%06d.png" % i, "PNG")
  print "out_fern%06d.png" % i

for i, p in enumerate(ps):
  output_fern(i, p)
system("convert *.png -delay 1 -loop 0 anim.gif")
system("convert anim.gif -reverse animr.gif")
system("convert *.gif -delay 1 -loop 0 out.gif")
