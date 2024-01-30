PASSWORD = "admin"
LIMITE = 5
def verificar_contra():
    intentos = 0
    while intentos < LIMITE:
        contra = input("Ingrese la contraseña: ") 
        if contra == PASSWORD:
            print("Contraseña correcta")
            break
        intentos += 1
        print("Contraseña incorrecta")
 
    if LIMITE == intentos:
        print ("Demasiados intentos seguidos, vuelva a intentarlo mas tarde.")
        
verificar_contra()