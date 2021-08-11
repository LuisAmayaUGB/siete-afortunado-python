import random
while True:



    i = 1

    print("Siete Afortunado")
    print()
    print("Seleccione Opción")
    print()
    print("1------Principiante")
    print("2------Intermedio")
    print("3------Avanzado")
    print()
    opcion=int(input("Ingrese opción"))
    print()


    while i < 4:

        if(opcion==1):
            limite_superior=7


        if(opcion==2):
            limite_superior=10


        if(opcion==3):
            limite_superior=20
    
        a=random.randint(1, limite_superior)
        b=random.randint(1, limite_superior)
        c=random.randint(1, limite_superior)

        print("juego # ",i)

        if(a==7)and (b==7)and (c==7):
            print("Ganaste!!!")
        else:
            print("Perdiste!!!")

        print()
        print()
       # print(f"limite_superior {limite_superior}, opcion {opcion}  // {a}  {b}   {c}")

        i += 1



    
        print()
    continuar = input('Desea continuar? S / N :')

    if continuar.lower() in "s si y yes":
        continue

    else:
        break
