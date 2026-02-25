def cajero_automatico():
    saldo = 1000.0

    print("Bienvenido al Cajero Automático ")
    
    try:
        total_ops = int(input("¿Cuántas operaciones desea realizar hoy? "))
    except ValueError:
        print("Entrada inválida. Se asumirá 1 operación.")
        total_ops = 1

    for i in range(total_ops):
        print(f"\n Operación {i+1} de {total_ops} ")
        print("1 → Consultar saldo")
        print("2 → Retirar dinero")
        print("3 → Depositar dinero")
        
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            print(f"Su saldo actual es: ${saldo}")

        elif opcion == "2":
            monto_retirar = -1
            while monto_retirar < 0:
                try:
                    monto_retirar = float(input("Ingrese el monto a retirar: "))
                    if monto_retirar < 0:
                        print("El monto no puede ser negativo. Intente de nuevo.")
                except ValueError:
                    print("Por favor, ingrese un número válido.")
            
            if monto_retirar > saldo:
                print("Fondos insuficientes.")
            else:
                saldo -= monto_retirar
                print(f"Retiro exitoso. Su nuevo saldo es: ${saldo}")

        elif opcion == "3":
            monto_depositar = -1
            while monto_depositar < 0:
                try:
                    monto_depositar = float(input("Ingrese el monto a depositar: "))
                    if monto_depositar < 0:
                        print("El monto no puede ser negativo. Intente de nuevo.")
                except ValueError:
                    print("Por favor, ingrese un número válido.")
            
            saldo += monto_depositar
            print(f"Depósito exitoso. Su nuevo saldo es: ${saldo}")

        else:
            print("Opción inválida.")

    print("\nGracias por usar el cajero automático. ¡Que tenga un buen día!")

if __name__ == "__main__":
    cajero_automatico()
