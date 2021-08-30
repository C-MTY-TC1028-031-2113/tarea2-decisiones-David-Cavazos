
def main():
    edad =0
    try:
        edad = int(input("Ingresa tu edad: "))
        correcto = True
        # Escribe el código adecuado para completar el programa
        # Puara pedir el dato de la idetificación oficial emplea este mensaje:
        # "¿Tienes identificación oficial? (s/n): "
    except ValueError:
        correcto = False

    if(correcto==False or edad<0):
        print("No cumples requisitos")
    elif(edad<18 ):
        print("No cumples requisitos")
    else: 
        identificacion = input("¿Tienes identificación oficial? (s/n): ")
        if(identificacion !="s" and identificacion !="n"):
            print("Respuesta incorrecta")
        
        elif(identificacion =="n"):
            print("No cumples requisitos")

        elif(edad>=18 and identificacion=="s"):
            print("Trámite de licencia concedido")
        

    


if __name__ == '__main__':
    main()
