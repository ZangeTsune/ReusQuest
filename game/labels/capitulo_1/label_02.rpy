init python:
    itemsEscena_C01L01 = None

init:
    image habitacionKeiishi_escritorio = "labels/capitulo_1/img/home_0.png"
    image habitacionKeiishi_0 = "labels/capitulo_1/img/home_1.png"

label cap_01_escena_01:

    python:
        if itemsEscena_C01L01 is None:
            escenaActual = "cap_01_lab_01_posible_1"
            itemsEscena_C01L01 = ItemEscenaContainer()
            itemsEscena_C01L01.setItems(ItemEscena(Dialogo(protagonista, ["He encontrado algo"], ["He encontrado algo", "solo la primera vez"])).setClickListener(0, 0 , 50, 50), ItemEscena(Jump("cap_01_lab_01_posible_2"), False).setClickListener(200, 200 , 50, 50, "img/b_derecha.png", None))

        else:
            if  itemsEscena_C01L01.getItem(0).isEncontrado():
                itemsEscena_C01L01.getItem(1).activar()

        renpy.jump(escenaActual)


label cap_01_lab_01_posible_1:
    # Muestra Escritorio
    $escenaActual = "cap_01_lab_01_posible_1"
    scene habitacionKeiishi_escritorio


    $itemsEscena_C01L01.setDebugMode()
    $itemsEscena_C01L01.activeListeners()

    jump cap_01_lab_01

label cap_01_lab_01_posible_2:
    # Muestra Habitacion 1
    $escenaActual = "cap_01_lab_01_posible_2"
    scene habitacionKeiishi_0

    $itemsEscena_C01L01.activeListeners()

    jump cap_01_lab_01