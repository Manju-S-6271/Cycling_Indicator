A = 0
def Turn_Right():
    basic.show_leds("""
        . . . . .
        . . . . .
        . . . . .
        . . . . .
        . . . . .
        """)
    basic.pause(10)
    basic.show_leds("""
        # # # # #
        # # # # #
        # # # # #
        . . . . .
        . . . . .
        """)
    basic.pause(10)
    basic.show_leds("""
        . . . . .
        . . . . .
        . . . . .
        . . . . .
        . . . . .
        """)
    basic.pause(10)
    basic.show_arrow(ArrowNames.NORTH)
    basic.pause(10)

def on_gesture_eight_g():
    pass
input.on_gesture(Gesture.EIGHT_G, on_gesture_eight_g)

def on_button_pressed_a():
    global A
    A = 0
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_gesture_logo_up():
    Turn_Left()
input.on_gesture(Gesture.LOGO_UP, on_gesture_logo_up)

def Turn_Left():
    basic.show_leds("""
        . . . . .
        . . . . .
        . . . . .
        . . . . .
        . . . . .
        """)
    basic.pause(10)
    basic.show_leds("""
        # # # . .
        # # # . .
        # # # . .
        # # # . .
        # # # . .
        """)
    basic.pause(10)
    basic.show_leds("""
        . . . . .
        . . . . .
        . . . . .
        . . . . .
        . . . . .
        """)
    basic.pause(10)
    basic.show_arrow(ArrowNames.WEST)
    basic.pause(10)

def on_gesture_tilt_right():
    Turn_Right()
input.on_gesture(Gesture.TILT_RIGHT, on_gesture_tilt_right)

def on_every_interval():
    pass
loops.every_interval(500, on_every_interval)

def on_forever():
    pass
basic.forever(on_forever)

def on_forever2():
    pass
basic.forever(on_forever2)
