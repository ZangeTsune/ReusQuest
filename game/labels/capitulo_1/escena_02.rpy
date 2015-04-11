init python:
    escena_C01S02 = None

label cap01_escena02:

    python:
        escena_C01S02 = ItemEscenaContainer()
        itemsEscena_C01L01.setItems(ItemEscena(Dialogo(protagonista, ["He encontrado algo"], ["He encontrado algo", "solo la primera vez"])).setClickListener(0, 0 , 50, 50), ItemEscena(Jump("cap_01_lab_01_posible_2"), False).setClickListener(200, 200 , 50, 50, "img/b_derecha.png", None))

        if escena_C01S02.getStatus() == 0:
            siguienteEscena = "cap01_escena02_init"

        if escena_C01S02.getStatus() == 1:
            siguienteEscena = "cap01_escena02_paso01"

        if escena_C01S02.getStatus() == 2:
            siguienteEscena = "cap01_escena03"

        renpy.jump(siguienteEscena)



label cap01_escena02_init:
    # Muestra Escritorio


    scene escritorio
    with fade

    protagonista "Uff... "
    extend "He estado MUCHO rato con esto"
    protagonista "Me duele tanto la cabeza que no recuerdo ni MI NOMBRE"

    $itemsEscena_C01L01.setDebugMode()
    $itemsEscena_C01L01.activeListeners()

    $escena_C01S02.avanza()

    jump cap01_escena02

label cap01_escena02_paso01:
    # Muestra Habitacion 1


    $itemsEscena_C01L01.activeListeners()

    $escena_C01S02.avanza()
    jump cap01_escena02