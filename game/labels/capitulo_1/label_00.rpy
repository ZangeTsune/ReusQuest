init python:
    itemsEscena_C01L00 = None

label cap_01_escena_00:

    scene black
    with fade

    $ renpy.play('labels/capitulo_1/sound/teclado.mp3')
    narrador "*ruido teclas de ordenador"
    narrador "...."
    $ renpy.play('sound/teclado.mp3')
    narrador "*MÁS ruido de teclas "
    protagonista "Aahahhhhrrggggggg !!"
    narrador "*APORREANDO LAS TECLAS"
    $ renpy.play('sound/golpes1.mp3')
    narrador "APORREANDO EL ORDENADOR"
    protagonista "...."
    protagonista "malditos trastos...."

    jump cap_01_escena_01