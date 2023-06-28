# Coloca en la terminal python Ahorcadooo.py

import random
hangman = [
    '''
    
       
          
          
          OK VAMOS A INTENTARLO :)
          
=======================
    ''',
    '''
    
          |
          |
          |
          |
          |
=======================
    ''',
    '''
    .-----.
          |
          |
          |
          |
          |
=======================
    ''',
    '''
    .-----.
    |     |
          |
          |
          |
          |
=======================
    ''',
    '''
    .-----.
    |     |
    0     |
          |
          |
          |
=======================
    ''',
    '''
    .-----.
    |     |
    0     |
    |     |
          |
          |
=======================
    ''',
    '''
    .-----.
    |     |
    0     |
    |\    |
          |
          |
=======================
    ''',
    '''
    .-----.
    |     |
    0     |
   /|\    |
          |
          |
=======================
    ''',   
    '''
    .-----.
    |     |
    0     |
   /|\    |
    |     |
          |
=======================
    ''',
    '''
    .-----.
    |     |
    0     |
   /|\    |
    |     |
     \    |
=======================
    ''',
    '''
    .-----.
    |     |
    0     |
   /|\    |
    |     |
   / \    |
=======================     
    ''',
    '''
    .-----.
    |     |
          |
          |
          |
  >->O    | PERDISTE :(
=======================
    ''',        
] # CREAMOS LOS DIBUJOS EN UNA LISTA PARA IR TOMANDO CADA VALOR

Idioma = input("\nSelecciona un idioma 'ESPAÑOL, INGLES, ALEMAN, FRANCES' (ESCRIBELO TAL CUAL APARECE) ") # EL ELEMENTO QUE RECIBE LA CONSOLA IDENTIFICARA EL TIPO DE IDIOMA QUE SELECCIONEMOS
if Idioma == "ESPAÑOL": # EN ESTE CASO COMO EL IDIOMA ES ESPAÑOL ENTONCES SI ES ESPAÑOL HAGA...
    Dificultad = input("\n Selecciona el grado de dificultad 'FACIL, MEDIO, DIFICIL' (ESCRIBELO TAL CUAL APARECE) ") # YA SALECCIONADO EL IDIOMA VAMOS A SELECCIONAR EL TIPO DE DIFICULTAD PARA EL JUEGO
    if Dificultad == "FACIL": #SI LA DIFICULTAD ES FACIL ENTONCES HAGA
        print("Seleccionaste el modo facil este modo tiene palabras cortas y cuenta con un total de 12 intentos ¿lo lograras?") # QUE IMPRIMA UN BREVE ENUNCIADO DEL JUEGO
        Letras_español_facil = ''' PYTHON ENTERO FUNCION TABLA LINUX SLACK GITHUB CLASE CODIGO LISTAS METODO VARIABLE PRUEBA FELIPE LIBRERIA ''' # AÑADIMOS LAS PALABRAS QUE QUEREMOS EN EL JUEGO EN UNA ORACION
        def palabra_aleatoria(): # DEFINIMOS UNA FUNCION PARA EXTRAER UNA PALABRA ALEATORIA DE LA ORACION QUE TENIAMOS ANTERIORMENTE
            palabra = Letras_español_facil.split() # CON LA FUNCION SPLIT CREAMOS UNA LISTA CON TODAS LAS PALABRAS DE LA LORACION LA LISTA SE LLAMARA PALABRA
            n = random.randint(0, len(palabra)-1) #n SERA EL VALOR QUE VAMOS A SIGNAR CON LA PALABRA RANDOM Y EL RANDINT NOS DEVUELVE UN NUMERO DEL RANDO ESPECIFICADO ALEATORIAMENTE
            return palabra[n] # NOS DEVUELVE UNA PALABRA ALEATORIA DE LA LISTA DE PALABRA

        def letras_palabra(): # DEFINIMOS LA FUNCION LETRAS PALABRAS COMO LA FUNCION PRINCIPAL
            palabra = palabra_aleatoria() #DEFINIMOS PALABRA CON LA PALABRA ALEATOREA QUE YA SELECCIONAMOS ANTERIORMENTE
            letras = [] # CREAMOS LISTAS VACIAS
            espacios = [] # CREAMOS LISTAS VACIAS
            for x in palabra: #PARA X IN PALABRAS
                letras.append(x) # SE AGREGA LA LETRA DE LA PALABRA EN LA LISTA DE LETRAS
                espacios.append('__') # EN LA LISTA DE ESPACIOS AGREGAMOS __ PARA IDENTIFICAR QUE AHI SE DEVERIAN DE COLOCAR LAS PALABRAS 
            intentos = 0 # DEFINIMOS INTENTOS PARA LA CANTIDAD DE INTENTOS EN EL JUEGO
            print(hangman[intentos]) # IMPIMIMOS EL ELEMENTO NUMERO 0 DE LA LISTA HANGMAN QUE SERIA EL MUÑEQUITO INICIAL DEL JUEGO
            print(','.join(espacios)) # CON JOIN UNIMOS TODOS LOS ELEMENTOS DE UNA LISTA EN UNA CADENA USANDO LA , COMO DEPARADOR
                    
            while True: # MIENTRAS QUE SEA VERDAD HAGA
                letra = input(' \n Escribe una letra ') # DEFINIMOS LETRA COMO LAS LETRAS QUE VAMOS A IR RECIVIENDO Y MIRAR SI ESTA EN LA PALABRA
                contador = -1 # DEFINIMOS CONTADOR PARA CONTAR LOS ESPACIOS QUE HAY ES DECIR, LOS ELEMENTOS DE LA LISTA ESPACIOS
                correcto = False # DEFINIMOS CORRECTO COMO FALSO MIENTRAS TANTO 
                for i in palabra: # PARA I EN PALABTRAS HAGA
                    contador += 1 # LE SUMAMOS UNO A CONTADOR ASI EMPIEZA A CONTAR DESDE 0
                    if letra == i: # SI LA LETRA QUE ESCRIBIMOS ES IGUAL A I ENTONCES HAGA
                        espacios[contador] = letra # EN LA LISTA ESPACIOS CON POCICION CONTADOR SE ALMACENA LA LETRA QUE HACE PARTE DE LA PALABRA 
                        correcto = True # DECIMOS QUE ES VERDADERO CUANDO ENCUENTRA UNA PALABRA
                if letras == espacios: # POR OTRO LADO SI LALISTA DE LETRAS ES IGUAL A LA LISTA DE ESPACIOS ENTONCES HAGA
                    print('\n ¡FELICITACIONEES :) :) COMPLETASTE LA PALABRA /' + str(palabra) + '\ HAS GANADO! \n') # IMPRIME EL RESULTADO CON ESPACIOS DE LINEA PARA MEJOR ESTETICA
                    break  # COLOCAMOS ESTE BREAK PARA QUE YA SALGAMOS DE EL WHILE INFINITO ESTE WHILE ES SOLO PARA CUANDO LA VARIABLE LETRA ESTA DENTRO DE LA PALABRA      
                if intentos >= 10 and correcto != True: # SI LA CANTIDAD DE INTENTOS ES MAYOR O IGUAL QUE 10 Y CORRECTO ES != DE TRUE SI ESTO ES CORRECTO ENTONCES... 
                    print(hangman[11]) # IMPRIMIMOS EL ULTIMO ELEMENTO DE LA LISTA HANGMAN QUE SERIA EL MUÑECO FINAL POR LO TANTO YA HABREMOS PERDIDO EL JUEGO
                    print('\n NOOOOO PERDISTE :( :( :(, LA PALABRA ES /' + str(palabra) + '\, VUELVE A INTENTARLO ') # IMPRIMIMOS LA PARTE EN LA QUE PERDEMOS 
                    break # AHORA COLOCAMOS OTRO BREAK INDICANDO QUE YA NO TIENE QUE RECORRER OTRA VEZ EL WHILE INFINITO PORQUE YA HEMOS PERDIDO
                elif correcto != True: # AHORA UTILIZAMOS UN ELIF INDICANDO QUE SI NO SE CUMPKLIO EL PRIMER IF ENTONCES HAGA LO SIGIENTE SI CORRECTO ES != TRUE ENTONCES HAGA...
                    intentos += 1 # SE LE SUME 1 A INTENTOS ASI SE VAN SUMANDO LA CANTIDAD DE INTENTOS HASTA LLEGAR AL LIMITE
                print(hangman[intentos]) # IMPRIMIMOS LA LISTA HANGMAN DEPENDIENTO DE LA POCICION INTENTOS
                print(','.join(espacios)) # CON JOIN UNIMOS TODOS LOS ELEMENTOS DE UNA LISTA EN UNA CADENA USANDO LA , COMO DEPARADOR
            if intentos <= 2: # AHORA VAMOS A USAR EL TIPO DE PUNTAJE, ES DECIR SI LA CANTIDAD DE INTENTOS SOBRE PASA AL 2 ES DECIR...
                print("\n Tines un total de 50 puntos :) \n") # IMPRIMIMOS 50 PUNTOS
            elif intentos <= 5: # ES DECIR SI LA CANTIDAD DE INTENTOS SOBRE PASA AL 5 ES DECIR...
                print("\n Tines un total de 40 puntos :) \n") # IMPRIMIMOS 40 PUNTOS
            elif intentos <= 8: # ES DECIR SI LA CANTIDAD DE INTENTOS SOBRE PASA AL 8 ES DECIR...
                    print("\n Tines un total de 30 puntos :) \n") # IMPRIMIMOS 30 PUNTOS
            elif intentos <= 10: # ES DECIR SI LA CANTIDAD DE INTENTOS SOBRE PASA AL 10 ES DECIR...
                    print("\n Tines un total de 20 puntos :) \n") # IMPRIMIMOS 20 PUNTOS
            else: # SI NUNGUNA DE LAS ANTERIORES CONDICIONES SE CUMPLE ENTONCES HAGA...
                    print("\n Tines un total de 5 puntos :) \n") # IMPRIMIMOS 5 PUNTOS

        letras_palabra() # AHORA LLAMAMOS LA FUNCION PARA QUE EL CODIGO FUNCIONE

    elif Dificultad == "MEDIO": # HACEMOS LO MISMO PERO CON UN GRADO DE DIFICULTAD MAYOR ES DECIR REDUCIMOS LA CANTIDAD DE INTENTOS Y COMPLICAMOS LAS PALABRAS
        print("\n Seleccionaste el modo medio este modo tiene palabras mas largas que el modo facil y cuenta con un total de 6 intentos ¿lo lograras?")
        Letras_español_medio = ''' ALGORITMOS INSTITUTO MARKDOWN ARGUMENTACION ACOPLAMIENTO DEFINICION IMPLEMENTACION COMENTARIOS DOCUMENTACION BIBLIOTECA PSEUDOCODIGO DICCIONARIO CODIFICACION LENGUAJE APLICACION '''
        def palabra_aleatoria():
            palabra = Letras_español_medio.split()
            n = random.randint(0, len(palabra)-1)
            return palabra[n]

        def letras_palabra():
            palabra = palabra_aleatoria()
            letras = []
            espacios = []
            for x in palabra:
                letras.append(x)
                espacios.append('__')
            intentos = 0
            print(hangman[intentos]) 
            print(','.join(espacios))
                    
            while True:
                letra = input(' \n Escribe una letra ')
                contador = -1
                correcto = False
                for i in palabra:
                    contador += 1
                    if letra == i:
                        espacios[contador] = letra
                        correcto = True
                if letras == espacios:
                    print('\n ¡FELICITACIONEES :) :) COMPLETASTE LA PALABRA /' + str(palabra) + '\ HAS GANADO! \n')
                    break        
                if intentos >= 10 and correcto != True:
                    print(hangman[11])
                    print('\n NOOOOO PERDISTE :( :( :(, LA PALABRA ES /' + str(palabra) + '\, VUELVE A INTENTARLO ')
                    break
                elif correcto != True:
                    intentos += 2 
                print(hangman[intentos]) 
                print(','.join(espacios))
            if intentos <= 2:
                print("\n Tines un total de 50 puntos :) \n")
            elif intentos <= 5:
                print("\n Tines un total de 40 puntos :) \n")
            elif intentos <= 8:
                print("\n Tines un total de 30 puntos :) \n")
            elif intentos <= 10:
                print("\n Tines un total de 20 puntos :) \n")
            else:
                print("\n Tines un total de 5 puntos :) \n")

        letras_palabra()
    elif Dificultad == "DIFICIL":
        print("\n Seleccionaste el modo dificil, en este modo tu tienes que insertar el lugar de los espacios con el simbolo '-' este modo tiene en total 6 intentos. ¿LO LOGRARAS? \n")
        Letras_español_dificil = ''' CICLO-MIENTRAS CICLO-PARA CICLO-HASTA PALABRA-CLAVE TIPO-DE-DATOS LENGUAJE-DE-PROGRAMACION CODIGO-FUENTE DIAGRAMA-DE_FLUJO OPERADORES-LOGICOS PROGRAMACION-ESTRUCTURADA SISTEMA-OPERATIVO BASE-DE-DATOS PROGRAMACION-DE-COMPUTADORES UNIVERSIDAD-NACIONAL-DE-COLOMBIA ELEMENTOS-ALMACENADOS'''
        def palabra_aleatoria():
            palabra = Letras_español_dificil.split()
            n = random.randint(0, len(palabra)-1)
            return palabra[n]

        def letras_palabra():
            palabra = palabra_aleatoria()
            letras = []
            espacios = []
            for x in palabra:
                letras.append(x)
                espacios.append('__')
            intentos = 0
            print(hangman[intentos]) 
            print(','.join(espacios))
                    
            while True:
                letra = input(' \n Escribe una letra ')
                contador = -1
                correcto = False
                for i in palabra:
                    contador += 1
                    if letra == i:
                        espacios[contador] = letra
                        correcto = True
                if letras == espacios:
                    print('\n ¡FELICITACIONEES :) :) COMPLETASTE LA PALABRA /' + str(palabra) + '\ HAS GANADO! \n')
                    break        
                if intentos >= 10 and correcto != True:
                    print(hangman[11])
                    print('\n NOOOOO PERDISTE :( :( :(, LA PALABRA ES /' + str(palabra) + '\, VUELVE A INTENTARLO ')
                    break
                elif correcto != True:
                    intentos += 2 
                print(hangman[intentos]) 
                print(','.join(espacios))
            if intentos <= 2:
                print("\n Tines un total de 50 puntos :) \n")
            elif intentos <= 5:
                print("\n Tines un total de 40 puntos :) \n")
            elif intentos <= 8:
                print("\n Tines un total de 30 puntos :) \n")
            elif intentos <= 10:
                print("\n Tines un total de 20 puntos :) \n")
            else:
                print("\n Tines un total de 5 puntos :) \n")

        letras_palabra()
elif Idioma == "INGLES": # YA TENIENDO LAS DIFICULTADES DE UN IDIOMA HACEMOS LO MISMO CON LAS DEMAS IDIOMAS ASIGNANODLES TAMBIEN UNA DIFICULTAD ESPECIFICA
    Dificultad = input("\n Selected the degree of difficulty 'EASY, MEDIUM, HARD' (WRITE IT AS IT APPEARS) ")
    if Dificultad == "EASY":
        print("\n You selected the easy mode, this mode has short words and has a total of 12 attempts, will you succeed?")
        Letters_ingles_facil = ''' PYTHON INTEGER FUNCTION TABLE LINUX SLACK GITHUB CLASS CODE LISTS METHOD VARIABLE TEST FELIPE LIBRARY '''
        def palabra_aleatoria():
            palabra = Letters_ingles_facil.split()
            n = random.randint(0, len(palabra)-1)
            return palabra[n]

        def letras_palabra():
            palabra = palabra_aleatoria()
            letras = []
            espacios = []
            for x in palabra:
                letras.append(x)
                espacios.append('__')
            intentos = 0
            print(hangman[intentos]) 
            print(','.join(espacios))
                    
            while True:
                letra = input(' \n write a letter')
                contador = -1
                correcto = False
                for i in palabra:
                    contador += 1
                    if letra == i:
                        espacios[contador] = letra
                        correcto = True
                if letras == espacios:
                    print('\n CONGRATULATIOOOOONS :) :) YOU COMPLETED THE WORD /' + str(palabra) + '\ YOU HAVE WON! \n')
                    break        
                if intentos >= 10 and correcto != True:
                    print(hangman[11])
                    print('\n NOOOOO YOU LOST :( :( :(, THE WORD IS /' + str(palabra) + '\, RETRY ')
                    break
                elif correcto != True:
                    intentos += 1 
                print(hangman[intentos]) 
                print(','.join(espacios))
            if intentos <= 2:
                print("\n You have a total of 50 points :) \n")
            elif intentos <= 5:
                print("\n You have a total of 40 points :) \n")
            elif intentos <= 8:
                print("\n You have a total of 30 points :) \n")
            elif intentos <= 10:
                print("\n You have a total of 20 points :) \n")
            else:
                print("\n You have a total of 50 points :) \n")

        letras_palabra()

    elif Dificultad == "MEDIUM":
        print("\n You selected the medium mode, this mode has longer words than the easy mode and has a total of 6 attempts, will you succeed?")
        Letters_ingles_medio = ''' ALGORITHMS INSTITUTE MARKDOWN ARGUMENTATION COUPLING DEFINITION IMPLEMENTATION COMMENTS DOCUMENTATION LIBRARY PSEUDOCODE DICTIONARY CODING LANGUAGE APPLICATION SPRACHE ANWENDUNG '''
        def palabra_aleatoria():
            palabra = Letters_ingles_medio.split()
            n = random.randint(0, len(palabra)-1)
            return palabra[n]

        def letras_palabra():
            palabra = palabra_aleatoria()
            letras = []
            espacios = []
            for x in palabra:
                letras.append(x)
                espacios.append('__')
            intentos = 0
            print(hangman[intentos]) 
            print(','.join(espacios))
                    
            while True:
                letra = input(' \n write a letter ')
                contador = -1
                correcto = False
                for i in palabra:
                    contador += 1
                    if letra == i:
                        espacios[contador] = letra
                        correcto = True
                if letras == espacios:
                    print('\n CONGRATULATIOOOOONS :) :) YOU COMPLETED THE WORD /' + str(palabra) + '\ YOU HAVE WON! \n')
                    break        
                if intentos >= 10 and correcto != True:
                    print(hangman[11])
                    print('\n NOOOOO YOU LOST :( :( :(, THE WORD IS /' + str(palabra) + '\, RETRY ')
                    break
                elif correcto != True:
                    intentos += 2 
                print(hangman[intentos]) 
                print(','.join(espacios))
            if intentos <= 2:
                print("\n You have a total of 50 points :) \n")
            elif intentos <= 5:
                print("\n You have a total of 40 points :) \n")
            elif intentos <= 8:
                print("\n You have a total of 30 points :) \n")
            elif intentos <= 10:
                print("\n You have a total of 20 points :) \n")
            else:
                print("\n You have a total of 50 points :) \n")


        letras_palabra()
            
    elif Dificultad == "HARD":
        print("\n You selected the hard mode, in this mode you have to insert the place of the spaces with the symbol '-' this mode has a total of 6 attempts. WILL YOU MAKE IT? \n")
        Letters_ingles_Hard = ''' CYCLE-WHILE CYCLE-FOR CYCLE-HUNTIL KEYWORD DATA-TYPE PROGRAMMING-LANGUAGE SOURCE-CODE FLOWCHART LOGIC-OPERATORS STRUCTURED-PROGRAMMING OPERATING-SYSTEM DATABASE COMPUTER-PROGRAMMING NATIONAL-UNIVERSITY-OF-COLOMBIA STORED-ITEMS '''                
        def palabra_aleatoria():
            palabra = Letters_ingles_Hard.split()
            n = random.randint(0, len(palabra)-1)
            return palabra[n]

        def letras_palabra():
            palabra = palabra_aleatoria()
            letras = []
            espacios = []
            for x in palabra:
                letras.append(x)
                espacios.append('__')
            intentos = 0
            print(hangman[intentos]) 
            print(','.join(espacios))
                    
            while True:
                letra = input(' \n write a letter ')
                contador = -1
                correcto = False
                for i in palabra:
                    contador += 1
                    if letra == i:
                        espacios[contador] = letra
                        correcto = True
                if letras == espacios:
                    print('\n CONGRATULATIOOOOONS :) :) YOU COMPLETED THE WORD /' + str(palabra) + '\ YOU HAVE WON! \n')
                    break        
                if intentos >= 10 and correcto != True:
                    print(hangman[11])
                    print('\n NOOOOO YOU LOST :( :( :(, THE WORD IS /' + str(palabra) + '\, RETRY ')
                    break
                elif correcto != True:
                    intentos += 2 
                print(hangman[intentos]) 
                print(','.join(espacios))
            if intentos <= 2:
                print("\n You have a total of 50 points :) \n")
            elif intentos <= 5:
                print("\n You have a total of 40 points :) \n")
            elif intentos <= 8:
                print("\n You have a total of 30 points :) \n")
            elif intentos <= 10:
                print("\n You have a total of 20 points :) \n")
            else:
                print("\n You have a total of 50 points :) \n")

        letras_palabra()

elif Idioma == "ALEMAN":
    Dificultad = input("\n Wählen Sie den Schwierigkeitsgrad 'EINFACH, MITTEL, SCHWER' (SCHREIBEN SIE ES WIE ES ERSCHEINT) ")
    if Dificultad == "EINFACH":
        print("\n Sie haben den einfachen Modus ausgewählt. Dieser Modus hat kurze Wörter und insgesamt 12 Versuche. Wird Ihnen das gelingen?")
        Buchstaben_aleman_facil = ''' PYTHON GANZ FUNKTION PLANKE LINUX SLACK GITHUB KLASSE CODE LISTEN METHODE VARIABLE NACHWEISEN PHILIP BUCHGESCHAFT '''
        def palabra_aleatoria():
            palabra = Buchstaben_aleman_facil.split()
            n = random.randint(0, len(palabra)-1)
            return palabra[n]

        def letras_palabra():
            palabra = palabra_aleatoria()
            letras = []
            espacios = []
            for x in palabra:
                letras.append(x)
                espacios.append('__')
            intentos = 0
            print(hangman[intentos]) 
            print(','.join(espacios))
                    
            while True:
                letra = input(' \n einen Brief schreiben ')
                contador = -1
                correcto = False
                for i in palabra:
                    contador += 1
                    if letra == i:
                        espacios[contador] = letra
                        correcto = True
                if letras == espacios:
                    print('\n HERZLICHEN GLÜCKWUNSCH :) :) Du hast das Wort vervollständigt /' + str(palabra) + '\DU HAST GEWONNEN! \n')
                    break        
                if intentos >= 10 and correcto != True:
                    print(hangman[11])
                    print('\n NEIN, DU HAST VERLOREN :( :( :(, DAS WORT IST /' + str(palabra) + '\, WIEDERHOLEN ')
                    break
                elif correcto != True:
                    intentos += 1 
                print(hangman[intentos]) 
                print(','.join(espacios))
            if intentos <= 2:
                print("\n Du hast insgesamt 50 Punkte :) \n")
            elif intentos <= 5:
                print("\n Du hast insgesamt 40 Punkte :) \n")
            elif intentos <= 8:
                print("\n Du hast insgesamt 30 Punkte :) \n")
            elif intentos <= 10:
                print("\n Du hast insgesamt 20 Punkte :) \n")
            else:
                print("\n Du hast insgesamt 5 Punkte :) \n")

        letras_palabra()

    elif Dificultad == "MITTEL":
        print("\n Sie haben den mittleren Modus ausgewählt. Dieser Modus hat längere Wörter als der einfache Modus und erfordert insgesamt 6 Versuche. Wird Ihnen das gelingen?")
        Buchstaben_aleman_medio = ''' ALGORITHMEN INSTITUT MARKDOWN ARGUMENTATION KUPPLUNG DEFINITION IMPLEMENTIERUNG KOMMENTARE DOKUMENTATION BIBLIOTHEK PSEUDOCODE WORTERBUCH CODIERUNG '''                
        def palabra_aleatoria():
            palabra = Buchstaben_aleman_medio.split()
            n = random.randint(0, len(palabra)-1)
            return palabra[n]

        def letras_palabra():
            palabra = palabra_aleatoria()
            letras = []
            espacios = []
            for x in palabra:
                letras.append(x)
                espacios.append('__')
            intentos = 0
            print(hangman[intentos]) 
            print(','.join(espacios))
                    
            while True:
                letra = input(' \n einen Brief schreiben ')
                contador = -1
                correcto = False
                for i in palabra:
                    contador += 1
                    if letra == i:
                        espacios[contador] = letra
                        correcto = True
                if letras == espacios:
                    print('\n HERZLICHEN GLÜCKWUNSCH :) :) Du hast das Wort vervollständigt /' + str(palabra) + '\DU HAST GEWONNEN! \n')
                    break        
                if intentos >= 10 and correcto != True:
                    print(hangman[11])
                    print('\n NEIN, DU HAST VERLOREN :( :( :(, DAS WORT IST /' + str(palabra) + '\, WIEDERHOLEN ')
                    break
                elif correcto != True:
                    intentos += 2 
                print(hangman[intentos]) 
                print(','.join(espacios))
            if intentos <= 2:
                print("\n Du hast insgesamt 50 Punkte :) \n")
            elif intentos <= 5:
                print("\n Du hast insgesamt 40 Punkte :) \n")
            elif intentos <= 8:
                print("\n Du hast insgesamt 30 Punkte :) \n")
            elif intentos <= 10:
                print("\n Du hast insgesamt 20 Punkte :) \n")
            else:
                print("\n Du hast insgesamt 5 Punkte :) \n")

        letras_palabra()
            
    elif Dificultad == "SCHWER":
        print("\n Sie haben den harten Modus ausgewählt. In diesem Modus müssen Sie die Stelle der Leerzeichen mit dem Symbol '-' einfügen. Dieser Modus hat insgesamt 6 Versuche. DU WIRST ES TUN? \n")
        Buchstaben_aleman_dificil = ''' WHILE-SCHLEIFE FOR-SCHLEIFE BIS-ZYKLUS STICHWORT ART-DER-DATEN PROGRAMMIERSPRACHE QUELLCODE FLUSSDIAGRAMM LOGISCHE-OPERATOREN STRUKTURIERTE-PROGRAMMIERUNG BETRIEBSSYSTEM DATENBANK COMPUTERPROGRAMMIERUNG NATIONAL-UNIVERSITY-OF-COLOMBIA STORED-ELEMENTS '''
        def palabra_aleatoria():
            palabra = Buchstaben_aleman_dificil.split()
            n = random.randint(0, len(palabra)-1)
            return palabra[n]

        def letras_palabra():
            palabra = palabra_aleatoria()
            letras = []
            espacios = []
            for x in palabra:
                letras.append(x)
                espacios.append('__')
            intentos = 0
            print(hangman[intentos]) 
            print(','.join(espacios))
                    
            while True:
                letra = input(' \n einen Brief schreiben ')
                contador = -1
                correcto = False
                for i in palabra:
                    contador += 1
                    if letra == i:
                        espacios[contador] = letra
                        correcto = True
                if letras == espacios:
                    print('\n HERZLICHEN GLÜCKWUNSCH :) :) Du hast das Wort vervollständigt /' + str(palabra) + '\DU HAST GEWONNEN! \n')
                    break        
                if intentos >= 10 and correcto != True:
                    print(hangman[11])
                    print('\n NEIN, DU HAST VERLOREN :( :( :(, DAS WORT IST /' + str(palabra) + '\, WIEDERHOLEN ')
                    break
                elif correcto != True:
                    intentos += 2 
                print(hangman[intentos]) 
                print(','.join(espacios))
            if intentos <= 2:
                print("\n Du hast insgesamt 50 Punkte :) \n")
            elif intentos <= 5:
                print("\n Du hast insgesamt 40 Punkte :) \n")
            elif intentos <= 8:
                print("\n Du hast insgesamt 30 Punkte :) \n")
            elif intentos <= 10:
                print("\n Du hast insgesamt 20 Punkte :) \n")
            else:
                print("\n Du hast insgesamt 5 Punkte :) \n")

        letras_palabra()

elif Idioma == "FRANCES":
    Dificultad = input("\n Sélectionnez le degré de difficulté 'FACILE, MOYEN, DIFFICILE' (ÉCRIVEZ-LE COMME IL APPARAÎT) ")
    if Dificultad == "FACILE":
        print("\n Vous avez sélectionné le mode facile, ce mode comporte des mots courts et compte 12 tentatives au total, réussirez-vous?")
        lettres_frances_facil = ''' PYTHON ENTIER FONCTION CONSEIL LINUX SLACK GITHUB CLASSE CODE LISTES METHODE VARIABLE TEST PHILIPPE LIBRAIRE '''
        def palabra_aleatoria():
            palabra = lettres_frances_facil.split()
            n = random.randint(0, len(palabra)-1)
            return palabra[n]

        def letras_palabra():
            palabra = palabra_aleatoria()
            letras = []
            espacios = []
            for x in palabra:
                letras.append(x)
                espacios.append('__')
            intentos = 0
            print(hangman[intentos]) 
            print(','.join(espacios))
                    
            while True:
                letra = input(' \n écrire une lettre ')
                contador = -1
                correcto = False
                for i in palabra:
                    contador += 1
                    if letra == i:
                        espacios[contador] = letra
                        correcto = True
                if letras == espacios:
                    print('\n FÉLICITATIONS :) :) VOUS AVEZ COMPLÉTÉ LE MOT /' + str(palabra) + '\ TU AS GAGNÉ! \n')
                    break        
                if intentos >= 10 and correcto != True:
                    print(hangman[11])
                    print('\n NOOOOOON VOUS AVEZ PERDU :( :( :(, LE MOT EST /' + str(palabra) + '\, RECOMMENCEZ ')
                    break
                elif correcto != True:
                    intentos += 1 
                print(hangman[intentos]) 
                print(','.join(espacios))
            if intentos <= 2:
                print("\n Vous avez un total de 50 points :) \n")
            elif intentos <= 5:
                print("\n Vous avez un total de 40 points :) \n")
            elif intentos <= 8:
                print("\n Vous avez un total de 30 points :) \n")
            elif intentos <= 10:
                print("\n Vous avez un total de 20 points :) \n")
            else:
                print("\n Vous avez un total de 5 points :) \n")

        letras_palabra()

    elif Dificultad == "MOYEN":
        print("\n Vous avez sélectionné le mode moyen, ce mode a des mots plus longs que le mode facile et a un total de 6 tentatives, réussirez-vous ?")
        lettres_frances_medio = ''' ALGORITHMES LYCÉE MARKDOWN ARGUMENTATION COUPLAGE DÉFINITION COMMENTAIRES DOCUMENTATION BIBLIOTHÈQUE PSEUDOCODE DICTIONNAIRE CODAGE LANGUE APPLICATION '''
        def palabra_aleatoria():
            palabra = lettres_frances_medio.split()
            n = random.randint(0, len(palabra)-1)
            return palabra[n]

        def letras_palabra():
            palabra = palabra_aleatoria()
            letras = []
            espacios = []
            for x in palabra:
                letras.append(x)
                espacios.append('__')
            intentos = 0
            print(hangman[intentos]) 
            print(','.join(espacios))
                    
            while True:
                letra = input(' \n écrire une lettre ')
                contador = -1
                correcto = False
                for i in palabra:
                    contador += 1
                    if letra == i:
                        espacios[contador] = letra
                        correcto = True
                if letras == espacios:
                    print('\n FÉLICITATIONS :) :) VOUS AVEZ COMPLÉTÉ LE MOT /' + str(palabra) + '\ TU AS GAGNÉ! \n')
                    break        
                if intentos >= 10 and correcto != True:
                    print(hangman[11])
                    print('\n NOOOOOON VOUS AVEZ PERDU :( :( :(, LE MOT EST /' + str(palabra) + '\, RECOMMENCEZ ')
                    break
                elif correcto != True:
                    intentos += 2 
                print(hangman[intentos]) 
                print(','.join(espacios))
            if intentos <= 2:
                print("\n Vous avez un total de 50 points :) \n")
            elif intentos <= 5:
                print("\n Vous avez un total de 40 points :) \n")
            elif intentos <= 8:
                print("\n Vous avez un total de 30 points :) \n")
            elif intentos <= 10:
                print("\n Vous avez un total de 20 points :) \n")
            else:
                print("\n Vous avez un total de 5 points :) \n")

        letras_palabra()
            
    elif Dificultad == "DIFFICILE":
        print("\n Vous avez sélectionné le mode difficile, dans ce mode vous devez insérer la place des espaces avec le symbole '-' ce mode a 6 tentatives au total. TU Y ARRIVERAS? \n")
        lettres_frances_DIFICIL = ''' BOUCLE-TANT-QUE BOUCLE-POUR JUSQUAU-CYCLE MOT-CLE TYPE-DE-DONNEES LANGAGE-DE-PROGRAMMATION CODE-SOURCE DIAGRAMME-DE-FLUX OPERATEURS-LOGIQUES PROGRAMMATION-STRUCTUREE SYSTEME-OPERATIF BASE-DE-DONNEES PROGRAMMATION-INFORMATIQUE UNIVERSITE-NATIONALE-DE-COLOMBIE ARTICLES-STOCKES '''
        def palabra_aleatoria():
            palabra = lettres_frances_DIFICIL.split()
            n = random.randint(0, len(palabra)-1)
            return palabra[n]

        def letras_palabra():
            palabra = palabra_aleatoria()
            letras = []
            espacios = []
            for x in palabra:
                letras.append(x)
                espacios.append('__')
            intentos = 0
            print(hangman[intentos]) 
            print(letras)
            print(','.join(espacios))
                    
            while True:
                letra = input(' \n écrire une lettre ')
                contador = -1
                correcto = False
                for i in palabra:
                    contador += 1
                    if letra == i:
                        espacios[contador] = letra
                        correcto = True
                if letras == espacios:
                    print('\n FÉLICITATIONS :) :) VOUS AVEZ COMPLÉTÉ LE MOT /' + str(palabra) + '\ TU AS GAGNÉ! \n')
                    break        
                if intentos >= 10 and correcto != True:
                    print(hangman[11])
                    print('\n NOOOOOON VOUS AVEZ PERDU :( :( :(, LE MOT EST /' + str(palabra) + '\, RECOMMENCEZ ')
                    break
                elif correcto != True:
                    intentos += 2 
                print(hangman[intentos]) 
                print(','.join(espacios))
            if intentos <= 2:
                print("\n Vous avez un total de 50 points :) \n")
            elif intentos <= 5:
                print("\n Vous avez un total de 40 points :) \n")
            elif intentos <= 8:
                print("\n Vous avez un total de 30 points :) \n")
            elif intentos <= 10:
                print("\n Vous avez un total de 20 points :) \n")
            else:
                print("\n Vous avez un total de 5 points :) \n")
        letras_palabra()

    

