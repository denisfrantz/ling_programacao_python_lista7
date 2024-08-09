try:
    a = int(input("1o número: "))
    b = int(input("2o número: "))
    
    d = a / b
    
    print ("\n", round(d, 2))
    
    if b < 0:
        raise ValueError

except ZeroDivisionError:
    print ("\nNão é possível dividir um número por 0!")
    
except ValueError:
    print ("\nO 2o número não pode ser menor que 0!")