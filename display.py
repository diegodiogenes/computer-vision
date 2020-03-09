import cv2
import numpy as np
import argparse

# função para ler a imagem passada pelo argumento
def read_image(image):
    return cv2.imread(image)


# função para separar apenas o canal vermelho
# setamos o azul e o verde para 0
def channel_r(image):
    r = image.copy()
    r[:, :, 0] = 0
    r[:, :, 1] = 0
    return r

# função para separar apenas o canal verde
# setamos o azul e o vermelho para 0
def channel_g(image):
    g = image.copy()
    g[:, :, 0] = 0
    g[:, :, 2] = 0
    return g

# função para separar apenas o canal azul
# setamos o vermelho e o verde para 0
def channel_b(image):
    b = image.copy()
    b[:, :, 1] = 0
    b[:, :, 2] = 0
    return b

# podemos também utilizar o método split do próprio opencv
def split_channels(image):
    b, g, r = cv2.split(image)
    return r, g, b

# invertendo imagem horizontalmente
def horizontal_inv(image):
    return img[:, ::-1]

# aplicando o blend entre as imagens
def blend_images(image1, image2):
    res_img = cv2.resize(image1, (300, 300))
    res_img1 = cv2.resize(image2, (300, 300))
    blend = np.multiply(0.5, res_img) + np.multiply(0.5, res_img1)

    return blend.astype('uint8')


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("-i", "--image", required=True, help="Diretório/Nome da imagem")
    args = vars(ap.parse_args())

    # lendo as duas imagens
    img = read_image(args["image"])
    img2 = cv2.imread("teste2.jpg")

    # separando cada canal
    r, g, b = split_channels(img)

    # invertendo horizontalmente
    inv = horizontal_inv(img)

    # realizando o blend
    blend = blend_images(img, img2)

    cv2.imshow("imagem", blend)

    cv2.waitKey(0)
