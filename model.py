from zipfile import ZipFile
import zipfile

def lazy_ascii_fix(fo):
    w = fo.write
    def nw(data):
        if type(data)==str:
            w(data.encode('ascii'))
        else:
            w(data)
    fo.write = nw

class model():
    def __init__(self,dims=[200,200,200]):
        self.dims=dims
        self.data=[]
        for z in range(dims[2]):
            self.data.append({})

    def set_pixel(self,coord,color):
        z=coord[2]
        y=coord[1]
        x=coord[0]
        self.data[z][(x,y)]=color

    def get_pixel(self,coord):
        z=coord[2]
        y=coord[1]
        x=coord[0]
        return self.data[z][(x,y)]

    

    def save(self,filename):
        zf = ZipFile(filename,'w',zipfile.ZIP_LZMA)
        meta = zf.open('meta.txt','w')
        lazy_ascii_fix(meta)
        meta.write('Version 0.1\n'.encode('ascii'))
        meta.write('x {}\n'.format(self.dims[0]))
        meta.write('y {}\n'.format(self.dims[1]))
        meta.write('z {}\n'.format(self.dims[2]))
        meta.close()
        for z in range(self.dims[2]):
            l = zf.open('layer{}.txt'.format(z),'w')
            lazy_ascii_fix(l)
            for y in range(self.dims[1]):
                for x in range(self.dims[0]):
                    try:
                        p = self.get_pixel((x,y,z))
                        l.write(str(p))
                    except:
                        l.write(str([0,0,0,0]))
                    l.write('\n')
            l.close()
        zf.close()

    def load(self,filename):
        zf = ZipFile(filename,'r',zipfile.ZIP_LZMA)
        meta = zf.open('meta.txt','r')
        

if __name__ == '__main__':
    m = model()
    m.save('test.mdl')
