import cv2
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

if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("-i", "--image", required=True, help="Diretório/Nome da imagem")
    args = vars(ap.parse_args())

    img = read_image(args["image"])

    r, g, b = split_channels(img)

    cv2.imshow("imagem", b)

    cv2.waitKey(0)