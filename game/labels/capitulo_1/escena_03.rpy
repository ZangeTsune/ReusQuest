init python:
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
            #escena_C01S03.setItems( Flecha(Flecha.IZQUIERDA,"cap01_escena02", 0.05,0.8,50,50), Recoger(Equipable( , ) ,0.41,0.29,270,175),
            #                       ItemEscena(Dialogo(None, ["Pio"], ["Pio Pio"])).setClickListener(0.69,0.6,50,50))

        if escena_C01S03.getStatus() == 0:
            siguienteEscena = "cap01_escena03_init"

        if escena_C01S03.getStatus() == 1:
            siguienteEscena = "cap01_escena03_paso01"

        if escena_C01S03.getStatus() == 2:
            siguienteEscena = "cap01_escena04"

        renpy.jump(siguienteEscena)



label cap01_escena03_init:
    # Muestra Escritorio

    protagonista "esto es una prueba "
    extend "He estado MUCHO rato con esto"
    protagonista "coger ESPADA"

    show newitem:
        ypos .3  xpos .3
    $ renpy.play('sound/item.wav')
    show item_shinai:
        ypos .35  xpos .35
    narrador "Consigues un Shinai ( espada de Bambú )"

    $escena_C01S03.setDebugMode()
    $escena_C01S03.activeListeners()

    #$escena_C01S03.avanza()

    jump cap01_escena03

label cap01_escena03_paso01:
    # Muestra Habitacion 1

    $escena_C01S03.setDebugMode()
    $escena_C01S03.activeListeners()

    #$escena_C01S02.avanza()
    jump cap01_escena02