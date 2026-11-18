import random
import time

titulo = input("    ΔΡÁΚΩΝ\nEscrito por Axel.\nIcono recortado de la obra de Friedrich Justin Bertuch.\n[Presione Enter para comenzar]\n")
salud = 255
print ("Navegando perdido por la mazmorra, encuentras dos cuevas.")
time.sleep(1)
print ("Ambas se ven oscuras y escalofriantes.")
time.sleep(2)
drago = random.randint(1,2)
cueva = int(input("¿Cuál elegirás? (1 o 2)"))
print ("Te vas acercando lentamente a la cueva...")
time.sleep(2)
print ("Se ve oscura y escalofriante...")
time.sleep(2)
print ("¡De repente, un enorme dragón aparece en frente tuyo! Comienza a abrir su boca y...")
time.sleep(3)
if drago == cueva:
    print ("...¡Este grita de la emoción!")
    time.sleep(2)
    print ('-"¡NO PUEDE SER! ¡UNA PERSONA! ¡NO HE VISTO A ALGUIEN PASARSE POR AQUÍ EN UN LARGO TIEMPO! ¡VEN AQUÍ Y QUEDATE UN RATO, POR FAVOR!"')
    time.sleep(3)
    rato = input("¿Te quedarás un rato con el dragón? (si o no)")
    if rato == 'si' or rato == 'sí' or rato == 'Sí' or rato == 'Si' or rato == 'SI' or rato == 'SÍ':
        print ("El dragón te lleva a una mesa y te sirve una ensalada de cucarachas y una sopa de murciélago y ratas. ¿A que no se ve muy apetitoso? ¿Qué harás? (Responder con la letra correspondiente)")
        time.sleep(3)
        comida = input('a) Comer.\nb) Botar la comida mientras no mira.\nc) Decirle que no puedes comer de esto.\nd) Preguntar por la comida (tono calmado).\ne) Preguntar por la comida (tono agresivo).')
        if comida == 'a':
            print ("Decides comer. Esperemos que esas cosas hayan estado bien cocinadas; no creo que viviendo en una cueva uno pueda aprender gastronomía...")
            time.sleep(3)
            print ("El dragón te pregunta cómo está la comida y le respondes que está bien. Este se alegra al escuchar eso.")
        elif comida == 'b':
            print ("El dragón va a por su plato. En estos 10 segundos, intentas botar toda la comida, pero el dragón te pilla y empieza a llorar.")
            time.sleep(3)
            print ('-(Llorando) "¿No te gusta mi comida? ¡¡BUAAAAAAAAAAAAAAAAA!!"')
            time.sleep(2)
            print ("Entre todo el llanto, este accidentalmente expulsa fuego y te quema.")
            quemado = random.randint(1,2)
            if quemado == 1:
                salud = 0
                muerte = input("Has muerto incinerado.")
            else: print ("El dragón se da cuenta e inmediatamente trae agua de cueva para extinguir el fuego. Después de un rato se calma y pide disculpas (tú lo perdonas porque no quiero hacerlo llorar de nuevo).")
        elif comida == 'c':
            print ('-"Ah, así que no puedes comer de esto. Vale, entonces simplemente te traeré agua."')
            time.sleep(2)
            print ("El dragón te trae un vaso de agua. Con mucho gusto lo aceptas.")
        elif comida == 'd':
            print ('-"Es lo que yo como todos los días. No tiene el mejor sabor pero es lo único que tenemos aquí."')
        elif comida == 'e':
            print ('-(Intentando contener el llanto) "¡¡BUAAAAAAAAAAAAAAAAA!!"')
            time.sleep(2)
            print ("Entre todo el llanto, este accidentalmente expulsa fuego y te quema.")
            quemado = random.randint(1,2)
            if quemado == 1:
                salud = 0
                muerte = input("Has muerto incinerado.")
            else: print ("El dragón se da cuenta e inmediatamente trae agua de cueva para extinguir el fuego. Después de un rato se calma y pide disculpas (tú lo perdonas porque no quiero hacerlo llorar de nuevo).")
        if salud > 0:
            time.sleep(2)
            print ('-"¡Ah, se me ha olvidado saludarte apropiadamente y preguntarte tu nombre!"')
            time.sleep(2)
            nombre = input("Escribe tu nombre aquí: ")
            print ('-"Ah, así que te llamas', nombre, '. Yo me llamo Thrinax. Es un gusto conocerte. ¿Qué cuentas?"')
            tema1 = input('a) Preguntar por el motivo por el que vive en este lugar.\nb) Preguntar por el motivo por el cual no te ataca.')
            if tema1 == 'a':
                print ('-"Yo vivo aquí por elección propia. Me gusta ser visitado, pero no puedo salir afuera porque todos se asustarán como tú lo hiciste cuando entraste aquí hace unos minutos... La razón por la que se asustan al verme es por culpa de mi hermano: Pandereta. Pandereta vive en la cueva de al lado, es un dragón despiadado que disfruta de torturar y matar a los viajeros que se encuentren con él. Será mejor que no te metas con él a menos de que estés listo para matarlo, lo cual ya no me importa, pues Pandereta es un terrible dragón y ha hecho sufrir a tanta gente que ya no se merece disfrutar de su vida torturando y matando viajeros, pero solía ser incluso peor 5 siglos atrás: salía de la mazmorra y masacraba pueblos enteros, hasta que un día usé un hechizo para sellarlo en su cueva. ¡De todas maneras no es tan malo vivir aquí! ¡Este lugar conecta con un mundo paralelo donde no me tienen miedo!"')
                continue1 = input("                                                         [Presiona Enter para continuar]")
                respuesta1 = input('a) "Mundo paralelo... No puede ser, eso es imposible..."\nb) "Pandereta es un nombre muy raro, especialmente para una criatura como vosotros, pues una pandereta es un instrumento..."')
                if respuesta1 == 'a':
                    print ('-"Sí, un mundo paralelo, y dejame decirte que es extraño, bizarro y todo lo que te puedas imaginar, parece sacado de un sueño. Hay todo tipo de criaturas raras que parecen sacadas de alguien que estaba profundamente dormido y la sociedad es tan perfecta que es demasiado fantasiosa para ser real... ¡A veces, cuando entro, me pregunto si acaso estoy soñando, consumí algo raro que encontré en la cueva por supervivencia o si me he vuelto loco! ¡Ja, ja, ja!"')
                    time.sleep(3)
                    respuesta2 = input ('a) "Ver para creer..."\nb) Preguntar por el aspecto y paisaje de ese supuesto mundo paralelo.')
                    if respuesta2 == 'a':
                        print ('-"¡Si no me crees entonces métete tú a ese armario!"')
                        time.sleep(2)
                        print ("-No, gracias; no quiero ir a Narnia- dices tú, seguido por un burlón jajajá.")
                        time.sleep(2)
                    if respuesta2 == 'b':
                        print ('-"Es una gran isla en medio de la nada. Tiene muchísima gente viviendo en diferentes pueblos y aldeas separadas las unas de las otras por bosques, desiertos y muchos otros tipos de biomas."')
                        time.sleep(3)
                if respuesta1 == 'b':
                    print ('-"No puedo negar eso..."')
            if tema1 == 'b':
                print ('-"¡¿Qué?! ¡Yo nunca haría tal cosa! Aunque Pandereta sí..."')
                time.sleep(2)
            print ('-¿Y tú por qué estás aquí?- te pregunta Thrinax.')
            time.sleep(2)
            print ("-Vine a esta mazmorra con la única motivación de encontrar tesoros; pero, ahora que veo lo peligroso que es este lugar, creo que preferiría regresar a casa- dices tú.")
            time.sleep(3)
            print ('-"¡Ah! ¡Yo te puedo ayudar a salir de aquí! ¡Tengo varios mapas de la mazmorra; podría darte uno para que encuentres la salida!"')
            time.sleep(3)
            print ("Thrinax se dirige inmediatamente a un cofre solitario, y, de este, saca un mapa y unos 5.000 kilos de oro. Thrinax regresa a la mesa y te da el mapa y 5.000 kilos de oro.")
            time.sleep(3)
            Enter1 = input("Has obtenido MAPA DE LA MAZMORRA.\n                                [Enter]")
            Enter2 = input("Has obtenido 5.000(kg) de oro.\n                            [Enter]")
            print ("Te emocionas e inmediatamente te preparas para regresar a casa, pero...")
            time.sleep(2)
            print ('-(Con un nudo en la garganta) "Fue divertido conversar contigo, pero ahora te tienes que ir... Te extrañaré,', nombre, '...')
            time.sleep(3)
            futuro = input('a) "Igualmente. Y ahora me despido, Thrinax..."\nb) "Tal vez pueda arriesgarme para visitarte una vez anualmente para que no te sientas tan solo..."\nc) "..."')
            if futuro == 'a':
                print ("-(Llorando silenciosamente)")
            if futuro == 'b':
                print ("Apenas escuchar eso, Thrinax pega un salto de emoción y exclama:")
                time.sleep(2)
                print ('-"¡¿DE VERAS?!"')
                time.sleep(2)
                regreso = input('a) "De veras."\nb) Reir a carcajadas y exclamar "No cuentes con ello".')
                if regreso == 'a':
                    print ("Thrinax sonríe. Parece haber quedado satisfecho con esa respuesta.")
                    time.sleep(2)
                if regreso == 'b':
                    print ("-(Llorando silenciosamente)")
                    time.sleep(2)
            print ("Te vas con tu nuevo mapa, con el objetivo de regresar a casa. ¿Cómo te despedirás?")
            despedida = input('a) Exclamar "Nos vemos".\nb) Exclamar "Hasta pronto".\nc) Exclamar "Hasta luego".\nd) Exclamar "Chao".\ne) No decir nada.')
            print ("FIN")
    elif rato == 'no' or rato == 'NO' or rato == 'No':
        print ("Te alejas y continúas con tu camino por la mazmorra.")
        time.sleep(2)
        print ("FIN")
else:
    Pandereta = 255
    print ("¡Pandereta el dragón te corta el paso!")
    time.sleep(2)
    while True:
        print ("\nTus PS:", salud, "\nPS de Pandereta:", Pandereta)
        print ("\nElige tu movimiento escribiendo el nro. correspondiente:")
        turno = input("1.- Mordisco\n2.- Patada\n3.- Estocada (con arma blanca)\n4.- Disparo (arco y flecha)")
        resta = random.randint(10,40)
        time.sleep(1)
        Pandereta = Pandereta - resta
        if Pandereta < 1:
            break
            Enter3 = input("¡Has derrotado a Pandereta!")
        ataque = random.randint(1,4)
        if ataque == 1:
            print ("\nPandereta usa su aliento de fuego contra ti.")
        elif ataque == 2:
            print ("\nPandereta se acerca a ti con rapidez y te da un potente mordisco.")
        elif ataque == 3:
            print ("\nPandereta velozmente te hace una gran arpadura en la costilla.")
        elif ataque == 4:
            print ("\nPandereta carga contra ti con todo su cuerpo.")
        resta = random.randint(10,40)
        salud = salud - resta
        time.sleep(2)
        if salud < 1:
            break
    if salud < 1:
        print ("¡Has caído debilitado!")
        time.sleep(2)
        print ("El dragón se acerca a tu debilitado cuerpo, abre su inmensa boca en frente de ti y...")
        time.sleep(3)
        print ("Has muerto engullido.")
    elif Pandereta < 1:
        print ("¡Has derrotado a Pandereta!")
        time.sleep(2)
        print ("Descubres montones de oro y demás tesoros.")
        time.sleep(2)
        Enter3 = input ("Has obtenido 5.000(kg) de oro.\n                           [Enter]")
        Enter4 = input ("Has obtenido ANTIGUA TABLA DE PIEDRA.\n                                [Enter]")
        Enter5 = input ("Has obtenido CHEETO CON FORMA DE CHEETO.\n                                     [Enter]")
        Enter6 = input ("Has obtenido DIARIO.\n                 [Enter]")
        FIN = input("Mmm..., la portada parece tener texto griego como título: ΔΡÁΚΩΝ. Qué interesante...")
