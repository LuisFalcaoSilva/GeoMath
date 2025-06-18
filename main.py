# Bibliotecas usadas
import time
import random
from datetime import datetime
import math

# Estética
print('{:=^40}'.format('Desafio 42'))
print('{:80}'.format(40 * '='))

# Interação inicial
input('')  # Pausa inicial
nome = input('Olaaaa!!!!! Eu me chamo ASCE, como é seu nome? ').strip().upper()

# Correção no nome
if nome in ['LUIS', 'LUÍS']:
    print('É bom te ver de novo carinha')
elif nome in ['KAROL', 'ANE']:
    print('Fala guria!')
else:
    print('É um prazer te conhecer!!!!')

# Listas de frases
frases_feliz = [
    'Se você está bem, eu estou bem!',
    'Que sua felicidade contagie a todos como me contagiou ;D',
    'Eu estou feliz por você estar feliz.',
    'Que bom que você está bem!'
]

frases_triste = [
    "Não desista, você é capaz de tudo!",
    "Cada desafio é uma oportunidade para crescer.",
    "Acredite em você, pois você tem muito potencial!",
    "Continue lutando, o sucesso está perto!"
]

# Pergunta sobre estado emocional
emocao = input('Você está bem? [Sim/Não] ').strip().upper()

while emocao not in ['SIM', 'NÃO']:
    emocao = input('Eu sou meio binário, vai ter que escolher entre SIM e NÃO :D ').strip().upper()

if emocao == 'SIM':
    print(random.choice(frases_feliz))
else:
    print(random.choice(frases_triste))

time.sleep(2)

# Função para calcular ângulos
def calcular_angulo(a, b, c):
    return math.degrees(math.acos((b**2 + c**2 - a**2) / (2 * b * c)))

# Loop principal do programa
while True:
    # Pergunta se quer ver a classificação dos triângulos
    duvida = input('\nAprendi uma nova utilidade. Agora consigo classificar triângulos. Quer ver? [Sim/Não] ').strip().upper()

    # Validação da resposta
    while duvida not in ['SIM', 'NÃO', 'QUERO']:
        duvida = input('Eu sou meio binário, vai ter que escolher entre SIM e NÃO :D ').strip().upper()

    if duvida in ['NÃO']:
        print('Ok, outro dia então...')
        break
    
    print('\nVamos nessa!!!!')
    time.sleep(1)
    
    # Entrada dos segmentos
    while True:
        try:
            r1 = float(input('\nDigite a medida do primeiro segmento: '))
            if r1 <= 0:
                print("⚠️ O valor deve ser positivo!")
                continue
            break
        except ValueError:
            print('⚠️ Isso não parece com um número! Digite apenas números.')

    while True:
        try:
            r2 = float(input('Digite a medida do segundo segmento: '))
            if r2 <= 0:
                print("⚠️ O valor deve ser positivo!")
                continue
            break
        except ValueError:
            print('⚠️ Isso não parece com um número! Digite apenas números.')

    while True:
        try:
            r3 = float(input('Digite a medida do terceiro segmento: '))
            if r3 <= 0:
                print("⚠️ O valor deve ser positivo!")
                continue
            break
        except ValueError:
            print('⚠️ Isso não parece com um número! Digite apenas números.')

    # Verificação e classificação do triângulo
    if (r1 + r2 > r3) and (r1 + r3 > r2) and (r2 + r3 > r1):
        # Classificação do triângulo
        if r1 == r2 == r3:
            print("\nOs seguimentos formam um triângulo equilátero (todos os lados iguais).")
        elif r1 == r2 or r1 == r3 or r2 == r3:
            print("\nOs seguimentos formam um triângulo isósceles (dois lados iguais).")
        else:
            print("\nOs seguimentos formam um triângulo escaleno (todos os lados diferentes).")
        
        # Cálculo dos ângulos
        angulo_A = calcular_angulo(r1, r2, r3)
        angulo_B = calcular_angulo(r2, r1, r3)
        angulo_C = 180 - angulo_A - angulo_B
        
        print("\nÂngulos do triângulo:")
        print(f"• Ângulo oposto ao 1º lado: {angulo_A:.2f}°")
        print(f"• Ângulo oposto ao 2º lado: {angulo_B:.2f}°")
        print(f"• Ângulo oposto ao 3º lado: {angulo_C:.2f}°")
        
        # Cálculo da área (Fórmula de Heron)
        s = (r1 + r2 + r3) / 2
        area = math.sqrt(s * (s - r1) * (s - r2) * (s - r3))
        print(f"\nÁrea do triângulo: {area:.2f} unidades quadradas")
    
    else:
        print("\nOs segmentos NÃO PODEM formar um triângulo!")
    
    # Pergunta se deseja repetir
    replay = input('\nGostaria de tentar de novo? [Sim/Não]: ').strip().upper()

    while replay not in ['SIM', 'NÃO']:
        replay = input('Por favor, escolha entre Sim ou Não: ').strip().upper()

    if replay == 'NÃO':
        print('\nEspero ter sido útil a você! Até a próxima :D')
        print('{:=^80}'.format(''))
        break

    print('\nReiniciando o código...\n')
    time.sleep(2)