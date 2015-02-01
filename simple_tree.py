from PIL import Image, ImageDraw
import random
import math
from os import system

rand = random.random

size = (3000,3000)
im = Image.new('RGB', size)
draw = ImageDraw.Draw(im)
sticklength = 50.00
depth_max = 500.0
startx, starty = size[0] / 2, 0

totalc = [0]

def random_tree(depth, draw, lastx, lasty):
  if (depth == depth_max):
    return

  if (rand() < 0.4):
    return

  leftx =  lastx - sticklength * math.cos(rand() * math.pi / 2.0)
  rightx = lastx + sticklength * math.cos(rand() * math.pi / 2.0)
  lefty =  lasty + sticklength * math.sin(rand() * math.pi / 2.0)
  righty = lasty + sticklength * math.sin(rand() * math.pi / 2.0)

  draw.line(((lastx,lasty),(rightx,righty)), fill=(0, int(255 * depth / depth_max), 120), width=1)
  #im.save("out_complex_tree%06d.png" % totalc[0], "PNG")
  print totalc[0]
  totalc[0] = totalc[0] + 1
  random_tree(depth + 1, draw, rightx, righty)

  draw.line(((lastx,lasty),(leftx,lefty)), fill=(0, int(255 * (depth / depth_max)), 255), width=1)
  random_tree(depth + 1, draw, leftx, lefty)
  #im.save("out_complex_tree%06d.png" % totalc[0], "PNG")
  print totalc[0]
  totalc[0] = totalc[0] + 1

random_tree(1.0, draw, startx, starty)  
im.save("out_simple_tree.png", "PNG")
#system("convert out_complex_tree000*.png -delay 20 -loop 0 complex_tree.gif")
