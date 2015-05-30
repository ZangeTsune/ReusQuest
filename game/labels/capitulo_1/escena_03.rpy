init python:
    from game.labels.capitulo_1 import Inicializaciones
    escena_C01S03 = None


label cap01_escena03:

    if globales.otraEscena :
        if escena_C01S03 is not None and escena_C01S03.getStatus() > 1:
            scene home01_01
            with fade
        else:
            scene home01
            with fade
        $globales.otraEscena = False

    python:

        if escena_C01S03 is None:
            escena_C01S03 = ItemEscenaContainer()
            escena_C01S03.setItems( Flecha(Flecha.ARRIBA, "cap01_escena04", 0.6,0.8), Flecha(Flecha.IZQUIERDA,"cap01_escena02", 0.05,0.85),
                                    MostrarTexto(protagonista, ["en este armario, hay cosas", ", posiblemente cosas maravillosas e impactantes...", "pero si lo abro ahora seguramente provoque una avalancha", ", o sea que mejor paso"], 0,0,190,170,
                                    MostrarTexto(protagonista, ["diversos objetos de decoración", " cuya unica utilidad real es acumular polvo.."], 0,0.3,190,180),
                                    MostrarTexto(protagonista, ["me gusta ese poster",", claro que si no me gustase no estaría aquí.."], 0.25,0.1,180,280),
                                    MostrarTexto(protagonista, ["cartel de las '1as Jornades de manga i cultura japonesa de Reus' por la associación juvenil Irasshai (TM)","no vayais a ir ahora, fueron en navidades del 2008"], 0.3,0.6,90,70),
                                    MostrarTexto(protagonista, ["Esa SI es una buena película de animación, de las me7jores que he visto"], 0.545,0.03,150,100),
                                    MostrarTexto(protagonista, ["Aqui iria un texto con un menu (ver original)"], 0.95,0.2,50,150),
                                    Recoger(Inicializaciones().getEquipable(Inicializaciones.EQUIPABLE_SHINAI)), 0.42, 0.58, 25, 240))

        if escena_C01S03.getStatus() == 0:
            siguienteEscena = "cap01_escena03_init"

        if escena_C01S03.getStatus() == 1:
            siguienteEscena = "cap01_escena03_paso01"

        if escena_C01S03.getStatus() == 2:
            siguienteEscena = "cap01_escena04"

        renpy.jump(siguienteEscena)



label cap01_escena03_init:
    $ renpy.play('sound/wilhem.mp3')
    narrador "..."
    protagonista "Vaya, parece que los vecinos estan de fiesta, OTRA VEZ..."

    $escena_C01S03.avanza()

    jump cap01_escena03

label cap01_escena03_paso01:
    # espada no recogible.

    $escena_C01S03.setDebugMode()
    $escena_C01S03.activeListeners()

    protagonista "esto es una prueba "
    extend "He estado MUCHO rato con esto"
    protagonista "coger ESPADA"


    $escena_C01S03.avanza()
    jump cap01_escena03