class somaMaiorCinquenta(Exception):
    pass

try:
    a = int(input("a = "))
    b = int(input("b = "))
    
    c = a + b
    
    if not c <= 50:
        raise somaMaiorCinquenta
    
except somaMaiorCinquenta:
    print("\nErro: Soma maior que 50!")
    
else:
    print("\nsoma =", c)