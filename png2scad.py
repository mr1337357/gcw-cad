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
                px = [float(n)/255 for n in px]
                if(px[3]>0):
                    scad.write('translate([{},{},{}]) '.format(x,y,z))
                    scad.write('color([{},{},{},{}]) '.format(px[0],px[1],px[2],px[3]))
                    scad.write('\tcube();\n')
                #print(px)
