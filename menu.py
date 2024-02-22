import time
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
while True:
    clear()
    print("*****************************")
    print("  Bienvenidos al programa  ")
    print("*****************************")
    print("1.)")
    print("2.)")
    print("3.)")
    print("4.)")
    print("0.)Salir")
    try:
        opc = int(input("\nIngresa una opcion: "))
    except ValueError:
        print("\n***ingresa una opcion correcta***")
        time.sleep(2)
        continue
    if opc == 1:
    elif opc == 2:
    elif opc == 3:
    elif opc == 4:
    elif opc == 0:   