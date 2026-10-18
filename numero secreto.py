import random
import time

def adivinar_numero_secreto():
    # El número que la computadora debe adivinar
    numero_secreto = random.randint(1, 100)
    intentos = 0
    
    minimo = 1
    maximo = 100
    
    print("=" * 50)
    print("La IA intentará adivinar un número secreto entre 1 y 100.")
    print(f"(Número secreto oculto: {numero_secreto})")
    print("=" * 50 + "\n")
    
    while minimo <= maximo:
        intentos += 1
        
        print(f"Rango válido actual: [ {minimo} hasta {maximo} ]")
        
        # La IA calcula su intento usando el punto medio (Búsqueda Binaria)
        intento = (minimo + maximo) // 2
        print(f"La IA propone el número: {intento}")
        
        # Pausa breve de 0.8 segundos para visualizar el proceso paso a paso
        time.sleep(0.8)
        
        if intento < numero_secreto:
            print("-> El número secreto es MAYOR.\n")
            minimo = intento + 1
            
        elif intento > numero_secreto:
            print("-> El número secreto es MENOR.\n")
            maximo = intento - 1
            
        else:
            print("=" * 50)
            print(f"¡La IA adivino el número secreto ({numero_secreto})!")
            print(f"Número total de intentos: {intentos}")
            print("=" * 50)
            break

if __name__ == "__main__":
    adivinar_numero_secreto()