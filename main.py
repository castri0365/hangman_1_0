import random
from palabras import palabras
from monigote import dibujos

while True:
    palabra = random.choice(palabras) .upper()   
    oculta = ["_"] * len(palabra)       
    usadas = []                         
    vidas = 6

    print("\n=== JUEGO DE AHORCADO ===")

    
    while vidas > 0 and "_" in oculta:
        print("\nPalabra a adivinar:", " ".join(oculta))
        print("Letras ya usadas:  ", ", ".join(usadas))
        print("Vidas restantes:   ", vidas)

        letra = input("Escribe UNA letra: ").strip().upper()

       
        if len(letra) != 1:
            print("-> debe ingresar solo 1 letra.")
            continue

        
        if letra < "A" or letra > "Z":
            print("-> debe ingresar una letra entre A y Z.")
            continue

        
        if letra in usadas:
            print("-> ya ha utilizado la letra.")
            continue

        
        usadas.append(letra)

        
        if letra in palabra:
            print(f"-> ¡Bien! La letra '{letra}' sí está.")
           
            for posicion in range(len(palabra)):
                if palabra[posicion] == letra:
                    oculta[posicion] = letra
        else:
            vidas -= 1
            print(f"-> Fallaste. La letra '{letra}' no está. Te quedan {vidas} vidas.")
            print(dibujos[vidas])

   
    if "_" not in oculta:
        print("\nPalabra completa:", " ".join(oculta))
        print("¡GANASTE!")
    else:
        print("\nContador de vidas: 0")
        print(dibujos[0])
        print("¡PERDISTE! La palabra oculta era:", palabra)

    
    opcion = input("\n¿Quieres jugar de nuevo? (1 = Sí / 2 = Finalizar): ").strip()
    if opcion != "1":
        print("Juego terminado.")
        break