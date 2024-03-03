from math import pi
raio = float(input('Digite o número do raio: '))
def circulo(raio):
	area = pi * raio**2
	return area

print('A área do círculo com raio é', round(circulo(raio), 2))#O número aqui seria o input