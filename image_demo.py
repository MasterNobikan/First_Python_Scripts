"""Examples of image processing in PY
23 April, 2018"""

# load libraries
from image import *
from random import *

# load image into program
pic = Image(file='earth.gif', title='Image Processing Demo')
# for blank image pic = Image(200,200,title='')

# Common functions to use, uncomment for use
'''
pic.show()
pic.width() / pic.height()
pic.get(x,y) / pic,set(x,y,(r,g,b,)
'''
pic.show()

'''#Binary
for x in range(pic.width()):
    for y in range(pic.height()):
        r, g, b = pic.get(x,y)
        intensity = int((r + g + b)/3)
        pic.set(x,y,(intensity,intensity,intensity))
    pic.update()
'''

'''#Brighten
for x in range(pic.width()):
    for y in range(pic.height()):
        r, g, b = pic.get(x,y)  # not spaced
        new_r = r*2
        new_g = g*2
        new_b = b*2
        if new_r > 255:
            new_r = 255
        if new_g > 255:
            new_g = 255
        if new_b > 255:
            new_b = 255
        pic.set(x, y, (new_r, new_g, new_b))
    pic.update()
'''

'''#Darken
for x in range(pic.width()):
    for y in range(pic.height()):
        r, g, b = pic.get(x,y)  # not spaced
        new_r = int(r/2)
        new_g = int(g/2)
        new_b = int(b/2)
        pic.set(x, y, (new_r, new_g, new_b))
    pic.update()
'''

'''#Color Channels
for x in range(pic.width()):
    for y in range(pic.height()):
        r, g, b = pic.get(x,y)  # not spaced
        new_r = r
        new_g = 0
        new_b = 0
        pic.set(x, y, (new_r, new_g, new_b))
    pic.update()
'''

'''#Greyscale
for x in range(pic.width()):
    for y in range(pic.height()):
        r, g, b = pic.get(x,y)  # not spaced
        if g > 10:
            pic.set(x,y,(255,255,255))
        else:
            pic.set(x,y,(0,0,0))
'''

'''#White Noise
for x in range(pic.width()):
    for y in range(pic.height()):
        r, g, b = pic.get(x,y)
        pic.set(x,y,(randint(0,255),randint(0,255),randint(0,255)))
    pic.update()
'''

mainloop()
