import random
import string

lista = [''.join(random.choices(string.ascii_letters + string.digits, k = 5)) for _ in range(500)]

print(f"Lista antes da alteração {lista[0]}")

lista[0] = "primeiro"
print(f"Lista após a alteração {lista[0]}")

print(f"Lista antes da alteração {lista[249]}")

lista[249] = "meio"
print(f"Lista após a alteração {lista[249]}")

print(f"Lista antes da alteração {lista[499]}")

lista[499] = "último"
print(f"Lista após a alteração {lista[499]}")