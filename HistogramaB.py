import numpy as np
import matplotlib.pyplot as plt

imagem = 'c:/Users/jukal/Desktop/HistogramaPDI/EntradaRGB.ppm'

with open(imagem, 'r') as arquivo:
    for _ in range(3):
        next(arquivo)
    
    dados = np.array([int(valor) for valor in arquivo.read().split()])

num_pixels = len(dados)

largura = 800 
altura = 800
num_canais = 3 

dados = dados.reshape((altura, largura, num_canais))

plt.figure(figsize=(12, 4))

plt.subplot(1, 3, 1)
plt.hist(dados[..., 0].ravel(), bins=256, color='red', alpha=0.7, edgecolor='black')
plt.title("Histograma RED")
plt.xlabel("Número do pixel")
plt.ylabel("Frequência")

plt.subplot(1, 3, 2)
plt.hist(dados[..., 1].ravel(), bins=256, color='green', alpha=0.7, edgecolor='black')
plt.title("Histograma GREEN")
plt.xlabel("Número do pixel")
plt.ylabel("Frequência")

plt.subplot(1, 3, 3)
plt.hist(dados[..., 2].ravel(), bins=256, color='blue', alpha=0.7, edgecolor='black')
plt.title("Histograma BLUE")
plt.xlabel("Número do pixel")
plt.ylabel("Frequência")

plt.tight_layout()
plt.show()
