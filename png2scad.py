from PIL import Image

import os



if __name__ == '__main__':
    import sys
    meta = open(sys.argv[1],'r')
    scad = open(sys.argv[2],'w')
    workdir = os.path.dirname(sys.argv[1])
    os.chdir(workdir)
    dimensions = meta.readline()[:-1].split(',')
    print(dimensions)
    for z in range(int(dimensions[2])):
        layername = meta.readline()[:-1]
        print(layername)
        layer = Image.open(layername)
        
        for y in range(int(dimensions[1])):
            for x in range(int(dimensions[0])):
                px = layer.getpixel((x,y))
                if(px[3]>128):
                    scad.write('translate([{},{},{}])'.format(x,y,z))
                    scad.write('\tcube();\n')
                print(px)
