import array as arr
from PIL import Image
import numpy as np

class Color:
    r = 0
    g = 0 
    b = 0

    def __init__(self, r, g, b):
        self.r = r
        self.g = g
        self.b = b
    
    def getValue(self):
        return [self.r, self.g, self.b, self.a]

mappings = (
    (127, 178, 56),
    (247, 233, 163),
    (199, 199, 199),
    (255, 0, 0),
    (160, 160, 255),
    (167, 167, 167),
    (0, 124, 0),
    (255, 255, 255),
    (164, 168, 184),
    (151, 109, 77),
    (112, 112, 112),
    (64, 64, 255),
    (143, 119, 72),
    (255, 252, 245),
    (216, 127, 51),
    (178, 76, 216),
    (102, 153, 216),
    (229, 229, 51),
    (127, 204, 25),
    (242, 127, 165),
    (76, 76, 76),
    (153, 153, 153),
    (76, 127, 153),
    (127, 63, 178),
    (51, 76, 178),
    (102, 76, 51),
    (102, 127, 51),
    (153, 51, 51),
    (25, 25, 25),
    (250, 238, 77),
    (92, 219, 213),
    (74, 128, 255),
    (0, 217, 58),
    (129, 86, 49),
    (112, 2, 0),
    (209, 177, 161),
    (159, 82, 36),
    (149, 87, 108),
    (112, 108, 138),
    (186, 133, 36),
    (103, 117, 53),
    (160, 77, 78),
    (57, 41, 35),
    (135, 107, 98),
    (87, 92, 92),
    (122, 73, 88),
    (76, 62, 92),
    (76, 50, 35),
    (76, 82, 42),
    (142, 60, 46),
    (37, 22, 16),
    (189, 48, 49),
    (148, 63, 97),
    (92, 25, 29),
    (22, 126, 134),
    (58, 142, 140),
    (86, 44, 62),
    (20, 180, 133),
    (100, 100, 100),
    (216, 175, 147),
    (127, 167, 150,)
)

def gfAlgorithm(c1, c2):
    rmean = (c1[0] + c2[0]) / 2
    r = c1[0] - c2[0]
    g = c1[1] - c2[1]
    b = c1[2] - c2[2]
    return (((512 + rmean) * r * r) / 2**8) + 4 * g * g + (((767 - rmean) * b * b) / 2**8)

def getBestPixel(true_color, mapping):
    mindist = float('inf')
    best_approximate = 0

    for mapcolor in mapping:
        distance = gfAlgorithm(true_color, mapcolor)
        if mindist > distance:
            mindist = distance
            best_approximate = mapcolor
    
    return best_approximate


try: 
    img  = Image.open("test.png")
    width, height = img.size
    pixels = img.load()

    for x in range (width):
        for y in range (height):
            bestcolor = getBestPixel(pixels[x, y], mappings)
            # print(bestcolor)
            pixels[x, y] = bestcolor

    img.save("out.png")

except IOError:
    pass

