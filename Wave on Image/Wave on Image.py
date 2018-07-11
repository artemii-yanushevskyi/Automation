# pip3 install Pillow
from math import pi, sin, cos, sqrt
from PIL import Image

class Pixel:
    def __init__(self, t):
        self.p = {"r": t[0], "g": t[1], "b": t[2]}
    def __str__(self):
        return str(self.p)
    def __mul__(self, value):
        for color in self.p.keys():
            self.p[color] *= value 
    def to_tuple(self):
        res = ( round(val) for val in (self.p['r'], self.p['g'], self.p['b']) )
        tupled = tuple(res)
        return tupled

def wave_centered(i, j, freq, epicenter):
    distance_from_epicenter = sqrt((i-epicenter[0])**2 + (j-epicenter[1])**2)
    value_at_point = cos(freq*distance_from_epicenter)
    tune_coeficient = (value_at_point+1.7)/2
    return tune_coeficient
    
def wave_linear(i, j, freq, fi):
    rotation = i*cos(fi)+j*sin(fi)
    value_at_point = cos(freq*rotation)
    tune_coeficient = (value_at_point+1.5)/2
    return tune_coeficient
    

    
if __name__ == '__main__':
    
    fi = pi/6
    freq = 1/5

    img = Image.open('original.png')
    pixels = img.load() # create the pixel map

    width, height = img.size[0], img.size[1]

    for i in range(width): # for every pixel:
        for j in range(height):
            px = Pixel(pixels[i,j])
            px*wave_linear(i,j, freq, fi)
            pixels[i,j] = px.to_tuple()
    
    img.save('Images with Waves/linear wave {} and angle {}.png'.format(freq, round(fi,2)))

    img = Image.open('original.png')
    pixels = img.load() # create the pixel map

    for i in range(width): # for every pixel:
        for j in range(height):
            px = Pixel(pixels[i,j])
            center = [width*3/4, height*3/4]
            px*wave_centered(i,j, freq, center)
            pixels[i,j] = px.to_tuple()
    
    img.save('Images with Waves/centered wave at {}.png'.format([round(c) for c in center]))
    
    img = Image.open('original.png')
    pixels = img.load() # create the pixel map

    for i in range(width): # for every pixel:
        for j in range(height):
            px = Pixel(pixels[i,j])
            center = [width*3/4, height*3/4]
            px*wave_centered(i,j, freq, center)
            center = [width*1/4, height*1/4]
            px*wave_centered(i,j, freq, center)
            pixels[i,j] = px.to_tuple()
    
    img.save('Images with Waves/two centered waves.png'.format([round(c) for c in center]))
    
    img = Image.open('original.png')
    pixels = img.load() # create the pixel map

    for i in range(width): # for every pixel:
        for j in range(height):
            px = Pixel(pixels[i,j])
            center = [width*3/4, height*3/4]
            px*wave_centered(i,j, freq, center)
            px*wave_linear(i,j, freq, fi)
            pixels[i,j] = px.to_tuple()
    
    img.save('Images with Waves/centered and linear waves.png'.format([round(c) for c in center]))