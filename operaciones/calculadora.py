def sumar(numero1, numero2):
    try:
        resultado = int (numero1) + int (numero2)
    except:
        print ("ingrese solo nùmeros")
    else:
        return resultado
            
  

def restar(numero1, numero2):
    try:
        resultado = int (numero1) - int (numero2)
    except:
        print ("ingrese solo nùmeros")
    else:
        return resultado

def multiplicar(numero1, numero2):
    try:
        resultado = int (numero1) * int (numero2)
    except:
        print ("ingrese solo nùmeros")
    else:
        return resultado

def dividir (numero1, numero2):
    try:
        resultado = int (numero1) / int (numero2)
    except ValueError:
        print ("ingrese solo nùmeros")
    except ZeroDivisionError:
        print("El nùmero no puede ser divisible entre 0")
    else:
        return resultado
