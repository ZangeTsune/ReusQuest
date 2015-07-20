init python:
    escena_C01S04 = None

label cap01_escena04:

    if globales.otraEscena :
        scene home01_01
        with fade
        $globales.otraEscena = False

    python:

        if escena_C01S04 is None:
            escena_C01S04 = ItemEscenaContainer()
            escena_C01S04.setItems( Flecha(Flecha.IZQUIERDA,"cap01_escena02", 0.05,0.8,50,50),
                                    Recoger(Jump("cap01_escena01"), 0.41,0.29,270,175),
                                    MostrarTexto(None, ["Pio"], 0.69, 0.6, 50, 50, ["Pio Pio"]))

        if escena_C01S04.getStatus() == 0:
            siguienteEscena = "cap01_escena04_init"

        if escena_C01S04.getStatus() == 1:
            siguienteEscena = "cap01_escena04_paso01"

        if escena_C01S04.getStatus() == 2:
            siguienteEscena = "cap01_escena04"

        renpy.jump(siguienteEscena)



label cap01_escena04_init:
    # Muestra Escritorio

    $escena_C01S04.setDebugMode()
    $escena_C01S04.activeListeners()

    #$escena_C01S04.avanza()

    jump cap01_escena04

label cap01_escena04_paso01:
    # Muestra Habitacion 1

    $escena_C01S04.setDebugMode()
    $escena_C01S04.activeListeners()

    #$escena_C01S04.avanza()
    jump cap01_escena04

