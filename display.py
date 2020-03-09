import cv2
import numpy as np
import argparse

#função para ler a imagem passada pelo argumento
def read_image(image):
    return cv2.imread(image)

# função para separar apenas o canal vermelho
# setamos o azul e o verde para 0
def channel_r(image):
    r = image.copy()
    r[:, :, 0] = 0
    r[:, :, 1] = 0
    return r

def channel_g(image):
    g = image.copy()
    g[:, :, 0] = 0
    g[:, :, 2] = 0
    return g

def channel_b(image):
    b = image.copy()
    b[:, :, 1] = 0
    b[:, :, 2] = 0
    return b

#podemos também utilizar o método split do próprio opencv
def split_channels(image):
    b, g, r = cv2.split(image)
    return r, g , b

def horizontal_inv(image):
    return img[:,::-1]

def blend_images(image1, image2):
    res_img = cv2.resize(image1, (300,300))
    res_img1 = cv2.resize(image2, (300,300))
    dst = cv2.addWeighted(res_img, 0.5, res_img1, 0.5, 0.0)

    # save the output image
    cv2.imwrite('image.png', dst)
    cv2.imshow('image.png', np.multiply(0.5, res_img))
    return np.multiply(0.5, res_img)

if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("-i", "--image", required=True, help="Diretório/Nome da imagem")
    args = vars(ap.parse_args())

    img = read_image(args["image"])
    img2 = cv2.imread("teste2.jpg")
    
    blend = blend_images(img, img2)

    r, g, b = split_channels(img)
    
    bl = channel_b(img)
    
    inv = horizontal_inv(img)
    
    # cv2.imshow("imagem", np.multiply(0.5, img2))

    cv2.waitKey(0)