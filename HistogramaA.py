import numpy as np
import matplotlib.pyplot as plt

imagem = 'c:/Users/jukal/Desktop/HistogramaPDI/EntradaEscalaCinza.pgm'

with open(imagem, 'r') as arquivo:
    for _ in range(3):
        next(arquivo)
    
    dados = np.loadtxt(arquivo, dtype=int)

plt.hist(dados.ravel(), bins=256, color='gray', alpha=0.7, edgecolor='black')
plt.title("Histograma sobre a imagem escala de cinza")
plt.xlabel("Número do pixel")
plt.ylabel("Frequência")

plt.show()
