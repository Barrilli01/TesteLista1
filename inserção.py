import random
import string

lista = [''.join(random.choices(string.ascii_letters + string.digits, k=5)) for _ in range(500)]

print(len(lista))
print(f"Lista antes da alteração posição 0: {lista[0]}")
print(f"Lista antes da alteração posição 1: {lista[1]}")
lista.insert(0, "primeiro")
print(len(lista))
print(f"Lista após a inserção posição 0: {lista[0]}")
print(f"Lista após a inserção posição 1: {lista[1]}")

print(f"Lista antes da alteração posição 249: {lista[249]}")
print(f"Lista antes da alteração posição 250: {lista[250]}")
lista.insert(249, "meio")
print(len(lista))
print(f"Lista após a inserção posição 249: {lista[249]}")
print(f"Lista após a inserção posição 250: {lista[250]}")

print(f"Lista antes da alteração posição 499: {lista[499]}")
print(f"Lista antes da alteração posição 500: {lista[500]}")
lista.insert(499, "último")
print(len(lista))
print(f"Lista após a inserção posição 499: {lista[499]}")
print(f"Lista após a inserção posição 500: {lista[500]}")
