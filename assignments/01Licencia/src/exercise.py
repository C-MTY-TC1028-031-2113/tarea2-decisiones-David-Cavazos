
def main():
    edad = int(input("Ingresa tu edad: "))
    if(edad<0):
        print("Respuesta incorrecta")
    if(edad<18 ):
        print("No cumples requisitos")
    else: 
        identificacion = input("¿Tienes identificación oficial? (s/n): ")


        if((identificacion != "s" and identificacion !="n") or (edad<0)):
            print("Respuesta incorrecta")
        
        

        elif(edad>=18 and identificacion=="s"):
            print("Trámite de licencia concedido")
        elif(identificacion =="n"):
            print("No cumples requisitos")

    


if __name__ == '__main__':
    main()
