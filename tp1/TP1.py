import PIL
import numpy as np
from PIL import Image



image1 = Image.open("spider.png")
image2 = Image.open("cat.png")
print(image1.mode)
#image = image.convert('L')
print(image2.getpixel((0,0))[0])
#image.size[2]

F = [[1/9, 1/9, 1/9], [1/9, 1/9, 1/9], [1/9, 1/9, 1/9]]

def MatConvolution(_image, _filtre):
    if _image.mode == 'L':
        tailleF = len(_filtre[0])
        posF = [0, 0]
        long = _image.size[0]
        larg = _image.size[1]
        somme = 0

        conv = np.zeros((long - tailleF + 1, larg - tailleF + 1))
        while posF[0] != long - tailleF and larg != _image.size[1] - tailleF:
            for k in range(long - tailleF):
                for l in range(larg - tailleF):
                    somme = 0
                    for m in range(tailleF):
                        for n in range(tailleF):
                            somme = somme + _image.getpixel((l+m, k+n)) * _filtre[m][n]
                    conv[k][l] = somme
                    posF[1] = posF[1] + 1
                posF[0] = posF[0] + 1
                posF[1] = 0
        return Image.fromarray(conv)
    elif _image.mode == 'RGBA':
        tailleF = len(_filtre[0])
        posF = [0, 0]
        long = _image.size[0]
        larg = _image.size[1]
        sommeR = 0
        sommeG = 0
        sommeB = 0
        alpha  = 0
        conv = np.zeros((long - tailleF + 1, larg - tailleF + 1))
        while posF[0] != long - tailleF and larg != _image.size[1] - tailleF:
            for k in range(long - tailleF):
                for l in range(larg - tailleF):
                    sommeR = 0
                    sommeG = 0
                    sommeB = 0
                    for m in range(tailleF):
                        for n in range(tailleF):
                            sommeR = sommeR + _image.getpixel((l+m, k+n))[0] * _filtre[m][n]
                            sommeG = sommeG + _image.getpixel((l+m, k+n))[1] * _filtre[m][n]
                            sommeB = sommeB + _image.getpixel((l+m, k+n))[2] * _filtre[m][n]
                            alpha  = alpha  + _image.getpixel((l+m, k+n))[3] * _filtre[m][n]
                         
                    conv[k][l] = [sommeR, sommeG, sommeB, alpha]
                    posF[1] = posF[1] + 1
                posF[0] = posF[0] + 1
                posF[1] = 0
        return Image.fromarray(conv)




newImage = MatConvolution(image2, F)
newImage.show()






