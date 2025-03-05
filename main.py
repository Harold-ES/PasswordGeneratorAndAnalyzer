# main.py
from password_analyzer import calcular_entropia, clasificar_seguridad, generar_recomendaciones, detectar_patrones
from password_generator import generar_contraseña, generar_contraseña_moviles, generar_contraseña_hash, generar_contraseña_segura, generar_contraseña_personalizada

def main():
    while True:
        print("\n \n Analizador y generador de contraseñas seguras")
        print("\n1. Analizar contraseña")
        print("2. Generar contraseña segura")
        print("3. Salir")
        choice = input("\nSeleccione una opción: ")

        if choice == "1":
            password = input("\nIngrese la contraseña a analizar: ")
            entropia = calcular_entropia(password)
            nivel = clasificar_seguridad(entropia)
            recomendaciones = generar_recomendaciones(password, entropia)
            patrones_detectados = detectar_patrones(password)
            print(f"\nEntropía: {entropia:.2f} bits")
            print(f"Nivel de seguridad: {nivel}")

            if patrones_detectados:
                print("\n Se detectaron los siguientes problemas:")
                for alerta in patrones_detectados:
                    print(f" - {alerta}")
            elif entropia <= 100:
                print("\n Recomendaciones para mejorar su contraseña:")
                for rec in recomendaciones:
                    print(f" - {rec}")
            else:
                print("¡Excelente contraseña! Asegúrese de recordarla o use un gestor de contraseñas.")

        elif choice == "2":
            print("\nOpciones de generación de contraseña:")
            print("1. Contraseña estándar")
            print("2. Contraseña fácil para móviles")
            print("3. Contraseña basada en frase secreta (hashing)")
            print("4. Contraseña altamente segura")
            print("5. Contraseña personalizada")

            opcion = input("\n Seleccione una alternativa: ")

            if opcion == "1":
                print("\nContraseña generada:", generar_contraseña(16))
            elif opcion == "2":
                print("\nContraseña para móviles:", generar_contraseña_moviles(16))
            elif opcion == "3":
                frase = input("Introduzca una frase secreta: ")
                print("\nContraseña basada en hashing:", generar_contraseña_hash(frase))
            elif opcion == "4":
                print("\nContraseña segura generada:", generar_contraseña_segura(20))
            elif opcion == "5":
                longitud = int(input("\nIngrese la longitud de la contraseña: "))
                incluir_mayus = input("¿Incluir mayúsculas? (y/n): ").lower() == 'y'
                incluir_minus = input("¿Incluir minúsculas? (y/n): ").lower() == 'y'
                incluir_numeros = input("¿Incluir números? (y/n): ").lower() == 'y'
                incluir_simbolos = input("¿Incluir caracteres especiales? (y/n): ").lower() == 'y'
                excluir = input("¿Caracteres a excluir? (dejelo vacío si no hay): ")

                contraseña = generar_contraseña_personalizada(longitud, incluir_mayus, incluir_minus, incluir_numeros, incluir_simbolos, excluir)
                
                if contraseña:
                    print("\nContraseña personalizada generada:", contraseña)
                else:
                    print("\nNo se pudo generar una contraseña segura con esos parámetros. Intenta con una combinación diferente.")
            else:
                print("\nOpción inválida.")
        elif choice == "3":
            break
        else:
            print("\nOpción no válida.")

if __name__ == "__main__":
    main()
