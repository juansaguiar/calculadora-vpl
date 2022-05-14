# VALORES

print("FAVOR UTILIZAR '.' INVÉS DE ',' ")
print("--------------------------------")
inv = float(input("INVESTIMENTO: "))
juros = int(input("JUROS/i: "))
print("---")
print(" ")
ano1 = int(input("ANO 1: "))
ano2 = int(input("ANO 2: "))
ano3 = int(input("ANO 3: "))

calc1 = juros / 100 + 1
calc2 = ano1 / calc1

calc3 = juros / 100 + 1
calc4 = ano2 / calc3

calc5 = juros / 100 + 1
calc6 = ano3 / calc5


# CÁLCULO SOBRE 10% + 1 = 1.1

print(" ") 
print("cálculo 10% + 1 = 1.1")
print("---------------------")
print("ANO 1:", round(calc2, 2))
print("ANO 2:", round(calc4, 2))
print("ANO 3:", round(calc6, 2))
print("---")
print(" ")

calc7 = calc2 + calc4 + calc6
calc8 = inv - calc7

# RESULTADO

print("-------------")
print(f"CÁLCULO DOS ANOS: ", round(calc7, 2))
print(f"                 - {inv}")
print("                --------------")
print(f"VPL:              ", round(calc8, 2))
