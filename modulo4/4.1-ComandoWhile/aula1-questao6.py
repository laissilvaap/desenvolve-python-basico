n = int(input("Digite a quantidade de experimentos: "))
C = int(input("Digite a quantidade de coelhos: "))
R = int(input("Digite a quantidade de ratos: "))
S = int(input("Digite a quantidade de sapos: "))

while n <= 0:
    print("O número total de cobaias deve ser maior que zero.")
    n = int(input("Digite novamente a quantidade de cobaias: "))

percent_coelhos = (C / n) * 100
percent_ratos = (R / n) * 100
percent_sapos = (S / n) * 100

print(f"Total de cobaias: {n}")
print(f"Total de sapos: {S}")
print(f"Total de ratos: {R}")
print(f"Total de coelhos: {C}")
print(f"Percentual de sapos: {percent_sapos:.2f} %")
print(f"Percentual de ratos: {percent_ratos:.2f} %")
print(f"Percentual de coelhos: {percent_coelhos:.2f} %")

