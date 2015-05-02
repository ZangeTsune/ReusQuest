init python:
    escena_C01S02 = None

label cap01_escena02:

    if globales.otraEscena :
        scene escritorio
        with fade
        $globales.otraEscena = False

    python:

        if escena_C01S02 is None:
            escena_C01S02 = ItemEscenaContainer()
            escena_C01S02.setItems(Flecha(Flecha.IZQUIERDA,"cap01_escena03", 0.05,0.8), Flecha(Flecha.TRANSPARENTE, "cap01_escena01", 0.41,0.29,270,175)),
                                   MostrarTexto(None, ["Pio"], 0.69,0.6,50,50, ["Pio Pio"], "sound/pollo.mp3")))

            # [ ["izquierda","home1",0.05,0.8]
            #     ],[
            #     [0.41,0.29,270,175,"Pantalla"],
            #     [0.05,0.38,260,150,"Pantalla"],
            #     [0,0,270,210,"Recuerdos"],
            #     [0.6,0.1,130,100,"Soge"],
            #     [0.88,0,50,100,"Konata"],
            #     [0.78,0.2,400,300,"Vicio"],
            #     [0.69,0.6,50,50,"Pollito"]
            #     ]

        if escena_C01S02.getStatus() == 0:
            siguienteEscena = "cap01_escena02_init"

        if escena_C01S02.getStatus() == 1:
            siguienteEscena = "cap01_escena02_paso01"

        if escena_C01S02.getStatus() == 2:
            siguienteEscena = "cap01_escena03"

        renpy.jump(siguienteEscena)



label cap01_escena02_init:
    # Muestra Escritorio


    protagonista "Uff... "
    extend "He estado MUCHO rato con esto"
    protagonista "Me duele tanto la cabeza que no recuerdo ni MI NOMBRE"

    $continuar = False
    while not continuar:
        $nombre = renpy.input("Como me llamaba?") or "Rétard"
        if len(nombre) > 12:
            protagonista "creo que mi nombre no era tan largo...."
        else :
            $continuar=True

    $nombreProtagonista = nombre
    $protagonista.setNombre(nombreProtagonista)

    protagonista "si si... me llamo [protagonista.nombre].."
    protagonista "sera mejor que me tome un descanso"
    protagonista "creo iré a la cocina a tomar algo.."
    antagonista "pues yo creo que no"
    $antagonista.setNombre("Random")
    antagonista "mi cerebroooo "

    $escena_C01S02.avanza()

    jump cap01_escena02

label cap01_escena02_paso01:
    # Muestra Habitacion 1


    $escena_C01S02.setDebugMode()
    $escena_C01S02.activeListeners()

    #$escena_C01S02.avanza()
    jump cap01_escena02