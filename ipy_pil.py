# coding: utf-8

from PIL import Image, ImageDraw
im = new Image("RGB", (300, 300))
im = Image("RGB", (300, 300))
im = Image.new("RGB", (300, 300))
draw = ImageDraw.draw(im)
draw = ImageDraw.Draw(im)
draw
draw.line(((0, 0), (95.91684521454673, 95.91684521454673)))
im.save("out.png", "PNG")
draw.line(((95.91684521454673, 95.91684521454673), (174.65438520708062, 174.65438520708062)))
im.save("out.png", "PNG")
