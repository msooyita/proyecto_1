#Inicio del ciclo while
while True: 
    print("Seleccionar una opción") #Inicio del menú
    print("1. Sumar") #Sumar
    print("2. Restar") #Restar
    print("3. Multiplicar") #Multiplicar
    print("4. Dividir") #Dividir
    print("6. Fin") #Finalizar

    opcion = input("Ingresar un número de la opción: ") #Ingresar un número de las opciones

    if opcion == "1":
            print("Sumar")
            a = float(input("Ingrese un número: "))
            b = float(input("Ingrese un número: "))
            def sumar(a, b):
                    resultado = a + b
                    return resultado
            print(sumar(a,b))

    elif opcion == "2":
            print("Restar")
            a = float(input("Ingrese un número: "))
            b = float(input("Ingrese un número: "))
            def sumar(a, b):
                    resultado = a - b
                    return resultado
            print(sumar(a,b))

    elif opcion == "3": 
            print("Multiplicar")
            a = float(input("Ingrese un número: "))
            b = float(input("Ingrese un número: "))
            def sumar(a, b):
                    resultado = a * b
                    return resultado
            print(sumar(a,b))


    elif opcion == "4":
        print("Dividir")
        a = float(input("Ingrese un número: "))
        b = float(input("Ingrese un número: "))        
        def dividir(a, b):
            if b != 0:
                resultado = a / b
                return resultado                                 
            else:
                return "Error: división por cero"
        print(dividir(a,b))    

    elif opcion =="6": 
        break
    else:
        print("Opción inválida")
   