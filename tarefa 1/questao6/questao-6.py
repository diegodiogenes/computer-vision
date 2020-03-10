import numpy as np
import cv2 as cv

# lendo a primeira imagem
img = cv.imread('imagens/imagensComRuido/a1.jpg')

#computando a divisão por 9, realizando a media
img = img/9

# fazendo a soma de cada amostra dividido pela quantidade de amostras
for i in range(2, 10):
  img = img + cv.imread('imagens/imagensComRuido/a'+ str(i) +'.jpg')/9

# convertendo para o formato inteiro novamente
img = img.astype('uint8')

# exibindo a saída
cv.imshow('output', img)
cv.waitKey(0)