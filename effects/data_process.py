import cv2
import numpy as np
import random



def add_noise(origin_img):
    if random.randint(0,1):
        return addSaltAndPepperNoise(origin_img, percentage=random.uniform(0, 0.05))
    else:
        return addGaussianNoise(origin_img, percentage=random.uniform(0.01, 0.1))


def addSaltAndPepperNoise(src, percentage):
    SP_NoiseImg = src
    SP_NoiseNum = int(percentage * src.shape[0] * src.shape[1])
    for i in range(SP_NoiseNum):
        randX = random.randint(0, src.shape[0] - 1)
        randY = random.randint(0, src.shape[1] - 1)
        if random.randint(0, 1) == 0:
            SP_NoiseImg[randX, randY] = 0
        else:
            SP_NoiseImg[randX, randY] = 255
    return SP_NoiseImg

def addGaussianNoise(image,percentage):
    G_Noiseimg = image
    G_NoiseNum=int(percentage*image.shape[0]*image.shape[1])
    for i in range(G_NoiseNum):
        temp_x = np.random.randint(0,image.shape[0]-1)
        temp_y = np.random.randint(0,image.shape[1]-1)
        G_Noiseimg[temp_x][temp_y] = 255
    return G_Noiseimg


# ------------------------------------------------------



def erode_process(origin_img, ksize=(3,3)):
    dist = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, ksize)
    output_img = cv2.erode(origin_img, dist)
    return output_img

def dilate_process(origin_img, ksize=(3, 3)):
    dist = cv2.getStructuringElement(cv2.MORPH_RECT, ksize)
    dilation = cv2.dilate(origin_img, dist)
    return dilation

def blur_process(origin_img, ksize=(5, 5)):
    blur_img = cv2.blur(origin_img, ksize)
    return blur_img

