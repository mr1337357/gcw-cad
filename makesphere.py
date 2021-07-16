import math
from PIL import Image
import os

os.chdir('examples/sphere')



size = 100
metafile = open('meta.txt','w')

metafile.write('{},{},{}\n'.format(size,size,size))

for layer in range(0,size):
    layer += 1
    outfile = Image.new(mode="RGBA",size=(size,size))
    pixels = outfile.load()
    z = layer - 1
    for y in range(size):
        for x in range(size):
            if math.sqrt(x*x+y*y+z*z) < size/2:
                pixels[x,y] = (255,255,255,255)
            else:
                pixels[x,y] = (0,0,0,0)
    #outfile.show()
    outfile.save('img{}.png'.format(layer))
    metafile.write('img{}.png\n'.format(layer))
