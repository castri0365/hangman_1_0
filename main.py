import random
from palabras import palabras
from monigote import dibujos

while True:
    palabra = random.choice(palabras)
    oculta = ["_"] * len(palabra)
    usadas = []
    vidas = 6

    print("\n--- JUEGO DEL AHORCADO ---")

    while vidas > 0 and "_" in oculta:
        print("\nPalabra:", " ".join(oculta))
        print("Vidas:", vidas)
        letra = input("Ingresa una letra: ").upper()

        
        if len(letra) != 1:
            print("Debe ingresar solo 1 letra")
            continue
        if letra < "A" or letra > "Z":
            print("Debe ser una letra entre A y Z")
            continue
        if letra in usadas:
            print("Ya ha utilizado la letra")
            continue

        usadas.append(letra)

    
        if letra in palabra:
            for i in range(len(palabra)):
                if palabra[i] == letra:
                    oculta[i] = letra
        else:
            vidas -= 1
            print("Letra incorrecta. Vidas:", vidas)
            print(dibujos[vidas])

    
    if "_" not in oculta:
        print("\n¡GANASTE! La palabra era:", palabra)
    else:
        print("\nContador de vidas: 0")
        print(dibujos[0])
        print("¡PERDISTE! La palabra oculta era:", palabra)

    
    opcion = input("\n¿Quieres jugar de nuevo? (1 = Sí / 2 = Finalizar): ")
    if opcion != "1":
        print("Programa finalizado.")
        break