
def main():
    edad = int(input("Ingresa tu edad: "))
    # Escribe el código adecuado para completar el programa
    # Para pedir el dato de la idetificación oficial emplea este mensaje:
    # "¿Tienes identificación oficial? (s/n): "
    
    if(edad<0):
        print("Respuesta incorrecta")
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
