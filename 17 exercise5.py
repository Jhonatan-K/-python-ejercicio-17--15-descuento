# Ejercicio 5 Descuento del 15% de una tienda

'''
Todos los productos tienen un 15%
de descuento
'''


precio = float(input("Digite precio del producto:"))

descuento = (precio *15) / 100

precio_final = precio - descuento

print(f"El precio final a pagar es de ${precio_final:.0f}")