#from game.script import narrador

init python:
    escena_C01S01 = None

init:
    image tutorial = "labels/capitulo_1/img/home_00.png"
    image escritorio = "labels/capitulo_1/img/home_0.png"

label cap01_escena01:

    python:
        if escena_C01S01 is None:
            escena_C01S01 = ItemEscenaContainer()

        if escena_C01S01.getStatus() == 0:
            siguienteEscena = "cap01_escena01_init"

        if escena_C01S01.getStatus() == 1:
            siguienteEscena = "cap01_escena01_tutorial"

        renpy.jump(siguienteEscena)

label cap01_escena01_init:

    scene escritorio:
        parallel:
            linear 1 zoom 4
        parallel:
            align( 0.65, 0.4)

    with None

    scene tutorial
    with fade

    #$musica ("music/tutorial.mp3")

    narrador "mostrar imagen"
    narrador "¡ Bienvenido a Reus Quest !"
    narrador "En este juego el objetivo es resolver el misterio que baña esta entrañable ciudad del sud de Europa"
    narrador "Para ello tendras que explorar el entorno, "
    narrador "hablar con misteriosos personajes, "
    narrador "y ¡¡¡¡ Peleaar !!!!"
    narrador "Si, parece que por alguna extraña razón los habitantes de Reus se han vuelto algo violentos"
    narrador "no dudes en usar los recursos a tu alcanze para derribarlos"
    narrador " ( de forma no letal, claro)..."
    narrador "no tengas miedo, y ¡ a por ello !"
    narrador "¡ Buena suerte !"

    $escena_C01S01.avanza()
    jump cap01_escena01


label cap01_escena01_tutorial:

    scene tutorial
    with fade

    menu:
        "Exploración":
            narrador "mostrar imagen"
            narrador "cualquiera de los objetos en pantalla puede ser una pista, "
            narrador "simplemente clica en aquello con lo que quieras interactuar"
            narrador "a veces el protagonista te dara una descripción, otras podras conseguir algún item y algunas veces no pasara nada"
            narrador "nunca se sabe, o sea que no olvides clicar TODO lo que se te ocurra"
        "Movimiento":
            narrador "usa las flechas amarillas para moverte por el entorno"
            narrador "mostrar imagen"
            narrador "una flecha roja significa que cambias de area, asegurate de estar preparado!"
            narrador "mostrar imagen"
            narrador "puede que encuentres una forma más rapida de moverte entre areas que ya hayas visitado.."
            narrador "no olvides mirar el mapa de vez en cuando para situarte !"
        "Combate":
            narrador "mostrar imagen"
            narrador "MATA"
        "Objetos":
            narrador "mostrar imagen"
            narrador "COME"
        "Inventario":
            narrador "mostrar imagen"
            narrador "haz clic con el botón secundario en cualquier momento para acceder al inventario del personaje"
            narrador "Aqui puedes consultar el mapa, que objetos tienes, los ataques que has aprendido, y el estado de tu personaje "
            narrador "Ademas desde esta pantalla puedes acceder a las opciones del juego, donde podras configurar el audio, la velocidad del Texto, gestionar las partigas guardadas, etc..."
        "Guardando la partida":
            narrador "mostrar imagen"
            narrador "Haz clic en el botón secundario en qualquier momento para acceder al inventario"
            narrador "Alli encontraras la opción 'Guardar / Cargar' "
            narrador "clica en ella para acceder al menú de gestión de partidas"
            narrador "mostrar imagen"
            narrador "¡ recuerda ir guardando de vez en cuando !"
            narrador "nunca se sabe lo que te puedes encontrar"
        "¡ YA SE JUGAR ! ¡ cierra esto ! ":
            #musica
            #$musica ("music/home_0.mp3")
            jump cap01_escena02

    jump cap01_escena01_tutorial