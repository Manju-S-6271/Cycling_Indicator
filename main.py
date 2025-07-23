A = 0

def on_gesture_eight_g():
    pass
input.on_gesture(Gesture.EIGHT_G, on_gesture_eight_g)

def on_button_pressed_a():
    global A
    A = 0
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_every_interval():
    pass
loops.every_interval(500, on_every_interval)

def on_forever():
    pins.digital_write_pin(DigitalPin.P1, 1)
basic.forever(on_forever)
