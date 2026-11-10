from math import sin, cos, tan, radians
angulo = float(input("Digite o ângulo em graus: "))
print("O seno do ângulo é: {:.2f}, o cosseno é: {:.2f}, a tangente é: {:.2f}".format(sin(radians(angulo)), cos(radians(angulo)), tan(radians(angulo))))