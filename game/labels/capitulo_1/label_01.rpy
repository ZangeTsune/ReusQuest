init python:
    itemsEscena_C01L01 = None

label cap_01_lab_01:
    python:
        if itemsEscena_C01L01 is None:
            itemsEscena_C01L01 = ItemEscenaContainer()
            itemsEscena_C01L01.setItems(ItemEscena(Dialogo(personaje, ["He encontrado algo"], ["He encontrado algo", "solo la primera vez"])).setClickListener(0, 0 , 50, 50), ItemEscena(Dialogo(personaje, ["¡Funciona!"]), False).setClickListener(200, 200 , 50, 50, "img/b_derecha.png", None))

        else:
            if itemsEscena_C01L01.getItem(0).isEncontrado():
                itemsEscena_C01L01.getItem(1).activar()
                renpy.jump("cap_01_lab_01_posible_1")
            else:
                itemsEscena_C01L01.getItem(1).setEncontrado(False)
                renpy.jump("cap_01_lab_01_posible_2")

label cap_01_lab_01_posible_1:

    $itemsEscena_C01L01.setDebugMode()
    $itemsEscena_C01L01.activeListeners()

    jump cap_01_lab_01

label cap_01_lab_01_posible_2:

    $itemsEscena_C01L01.activeListeners()

    jump cap_01_lab_01