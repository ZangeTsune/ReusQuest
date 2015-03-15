screen BotonesFrame(fondo, items):

    frame:
        xpos 0
        ypos 0
        xfill True
        yfill True
        background "#0000"

        for item in items:
            python:
                if item[4] is None:
                    item[4] = fondo

            button xpos item[0] ypos item[1] xmaximum item[2] ymaximum item[3] background item[4] action Return (items.index(item))