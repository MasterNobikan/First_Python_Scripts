"""
Purpose: process an image in different ways
Author: JT Vannoy
Date: May 1st, 2018
COSC 235, Dr. Beau Christ
"""

from image import *

pic = Image(file='earth.gif', title='Imaging')


def greyscale(pic):
    """Changes all the colors in an image to shades of gray

    Parameters:
        pic: a gif image

    Return value:
        the greyscale image
    """

    pic2 = Image(pic.width(), pic.height(), title='Greyscale Image')
    for x in range(pic.width()):
        for y in range(pic.height()):
            r, g, b = pic.get(x,y)
            # equation for better greyscale
            intensity = int(0.2126 * r + 0.7152 * g + 0.0722 * b)
            # change the pixels in new image to grey shades
            pic2.set(x, y, (intensity, intensity, intensity))
    return pic2


def blur(pic):
    """Blurs an image

       Parameters:
           pic: a gif image

       Return value:
           the blurred image
       """
    pic2 = Image(pic.width(), pic.height(), title='Blurred Image')
    for x in range(pic.width()):
        for y in range(pic.height()):
            # avoid image borders
            if 0 < x < pic.width()-1 and 0 < y < pic.height()-1:
                list_r = []
                list_g = []
                list_b = []
                # list of pixel and neighboring pixel coordinates
                list_offsets = [(-1, -1), (0, -1), (1, -1), (-1, 0), (0, 0), (1, 0),
                               (-1, 1), (0, 1), (1, 1)]
                # loop and add r,g,b values of pixels to lists
                for i in range(9):
                    r, g, b = pic.get(x+list_offsets[i][0],y+list_offsets[i][1])
                    list_r.append(r)
                    list_g.append(g)
                    list_b.append(b)
                # set pixels to average color of neighboring pixels
                pic2.set(x, y, (int(sum(list_r)/9), int(sum(list_g)/9), int(sum(list_b)/9)))
    return pic2


def mirror(pic):
    """Mirrors the left side of an image down the middle

       Parameters:
           pic: a gif image

       Return value:
           the mirrored image
       """
    pic2 = Image(pic.width(), pic.height(), title='Mirrored Image')
    for x in range(int(pic.width()/2)):  # only loops over half the image
        for y in range(pic.height()):
            r, g, b = pic.get(x,y)  # read pixels
            pic2.set(x, y, (r, g, b))  # set pixels normal
            pic2.set(pic.width()-1-x, y, (r, g, b))  # set pixels backwards
    return pic2


def main():
    """Displays the original image, greyscaled image,
    blurred image, and mirrored image in separate windows.
    Exits program when all windows are closed by user.
    """

    pic.show()
    greyscale(pic).show()
    blur(pic).show()
    mirror(pic).show()
    mainloop()


main()
