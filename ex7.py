class diaError(Exception):
    pass

class mesError(Exception):
    pass

class anoError(Exception):
    pass

try:
    dia = int(input("dia: "))
    
    if not dia <= 31 and dia > 0:
        raise diaError
    
except ValueError:
    print ("\nO dia deve ser um numero inteiro!")
    
except diaError:
    print ("\nValor inválido para o dia!")

try:
    mes = int(input("mês: "))
    
    if not mes <= 12 and mes > 0:
        raise mesError
    
except ValueError:
    print ("\nO mês deve ser um numero inteiro!")

except mesError:
    print ("\nValor inválido para o mês!")

try:
    ano = int(input("ano: "))
    
    if not ano > 0:
        raise anoError
    
except ValueError:
    print ("\nO ano deve ser um numero inteiro!")
    
except anoError:
    print ("\nValor inválido para o ano!")