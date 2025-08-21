temp = 0
choix = 0
choix2 = 0
langue = 0
quitter = 0
continuer = True

#-Variables-

while continuer:

    if langue == 2:
        while True:
            try:
                temp = int(input("Entre la température que tu souhaites convertir (seulement le chiffre/nombre): "))
                print()
                break
            except ValueError:
                print("Veuillez Entrer un nombre")
                print()
                

        while choix not in [1, 2, 3]:
            try:
                choix = int(input("Si ce sont des degrès Celcius, entre 1, 2 pour Fahrenheit et 3 pour les Kelvins: "))
                print()

                if choix == 1:
                    print()
                    print("Tu as choisis les degrès Celcius (",temp,"°C)")
                    print()
                elif choix == 2:
                    print()
                    print("Tu as choisis les degrès Fahrenheit(",temp,"°F)")
                    print()
                else:
                    print()
                    print("Tu as choisis les degrès Kelvins(",temp,"K)")
                    print()
            except ValueError:
                print()
                print("Veuillez Entrer un nombre")
                print()
                
        while choix2 not in [1, 2, 3]:
            try:
                choix2 = int(input("En quoi veux-tu convertir ? Entre 1 pour des degrès Celcius, 2 pour Fahrenheit et 3 pour les Kelvins: "))

                if choix2 == 1:
                    print()
                    print("Tu as choisis les degrès Celcius")
                    print()
                elif choix2 == 2:
                    print()
                    print("Tu as choisis les degrès Fahrenheit")
                    print()
                else:
                    print()
                    print("Tu as choisis les degrès Kelvins")
                    print()
            except ValueError:
                print()
                print("Veuillez Entrer un nombre")
                print()
                

        if choix == 1 and choix2 == 1:
            print(f"{temp}°C donne {temp}°C !")

        if choix == 1 and choix2 == 2:
            print(f"{temp}°C donne", (temp * 9 / 5) + 32, "°F !")
            
        if choix == 1 and choix2 == 3:
            print(f"{temp}°C donne", temp + 273.15,"K !")

        if choix == 2 and choix2 == 1:
            print(f"{temp}°F donne", (temp - 32) * 5 / 9,"°C !")

        if choix == 2 and choix2 == 2:
            print(f"{temp}°F donne {temp}°F !")
            
        if choix == 2 and choix2 == 3:
            print(f"{temp}°F donne", (temp - 32) / 1.8 + 273.15,"K !")
            
        if choix == 3 and choix2 == 1:
            print(f"{temp}K donne", temp - 273.15,"°C !")

        if choix == 3 and choix2 == 2:
            print(f"{temp}K donne", (temp - 273.15) * 9 / 5 + 32, "°F !")
            
        if choix == 3 and choix2 == 3:
            print(f"{temp}°K donne {temp}K !")
            
        print()
        
        while quitter not in [1, 2]:
            try:
                print()
                quitter = int(input("Entre 1 pour quitter ou 2 pour refaire une conversion: "))
                
                if quitter == 1:
                    print()
                    print("Merci d'avoir utilisé Temp_Conversion !")
                    continuer = False
                    
            except ValueError:
                print("Entre 1 ou 2")
                