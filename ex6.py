class ValorAbaixoException(Exception):
    pass
class ValorAltoException(Exception):
    pass
class ValorMuitoAltoException(Exception):
    pass

try:
    a = int(input("Número: "))
    
    if not 0 < a:
        raise ValorAbaixoException
    
    if not 100 >= a and a < 1000:
        raise ValorAltoException
    
    if not a <= 1000:
        raise ValorMuitoAltoException
    
except TypeError:
    print ("O programa só aceita valores inteiros")
    
except ValorAbaixoException:
    print ("\nValorAbaixoException")
    
except ValorAltoException:
    print ("\nValorAltoException")
    
except ValorMuitoAltoException:
    print ("\nValorMuitoAltoException")
    
else:
    print("\nValor aceito")