blink = 0
reset_flag = 0
def Turn_Right():
    basic.clear_screen()
    for index in range(4):
        Turn_Right_Anime()
    for index2 in range(2):
        basic.show_arrow(ArrowNames.NORTH)
        basic.pause(10)
        basic.clear_screen()
        basic.pause(500)

def on_button_pressed_a():
    global blink
    basic.clear_screen()
    blink = 0
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_gesture_logo_up():
    global reset_flag, blink
    reset_flag = 1
    blink = 1
    while not (input.is_gesture(Gesture.SCREEN_UP)):
        Turn_Left()
    reset_flag = 0
    blink = 0
    basic.clear_screen()
input.on_gesture(Gesture.LOGO_UP, on_gesture_logo_up)

def on_gesture_screen_up():
    basic.clear_screen()
    if reset_flag:
        control.reset()
input.on_gesture(Gesture.SCREEN_UP, on_gesture_screen_up)

def Turn_Left_Anime():
    Toggle_all_of_column(4, False)
    Toggle_all_of_column(3, False)
    Toggle_all_of_column(2, False)
    Toggle_all_of_column(1, False)
    Toggle_all_of_column(0, True)
    Toggle_all_of_column(4, True)
    Toggle_all_of_column(3, True)
    Toggle_all_of_column(2, True)
    Toggle_all_of_column(1, True)
    Toggle_all_of_column(0, True)
    basic.pause(100)
def Turn_Right_Anime():
    Toggle_all_of_row(4, False)
    Toggle_all_of_row(3, False)
    Toggle_all_of_row(2, False)
    Toggle_all_of_row(1, False)
    Toggle_all_of_row(0, True)
    Toggle_all_of_row(4, True)
    Toggle_all_of_row(3, True)
    Toggle_all_of_row(2, True)
    Toggle_all_of_row(1, True)
    Toggle_all_of_row(0, True)
    basic.pause(100)

def on_gesture_tilt_right():
    global reset_flag, blink
    reset_flag = 1
    blink = 1
    while not (input.is_gesture(Gesture.SCREEN_UP)):
        Turn_Right()
    reset_flag = 0
    blink = 0
    basic.clear_screen()
input.on_gesture(Gesture.TILT_RIGHT, on_gesture_tilt_right)

def Turn_Left():
    basic.clear_screen()
    for index3 in range(4):
        Turn_Left_Anime()
    for index4 in range(2):
        basic.show_arrow(ArrowNames.WEST)
        basic.pause(10)
        basic.clear_screen()
        basic.pause(500)
def Toggle_all_of_column(column: number, WithPause: bool):
    for i in range(5):
        led.toggle(column, i)
    if WithPause:
        basic.pause(100)
def Toggle_all_of_row(Row: number, WithPause2: bool):
    for j in range(5):
        led.toggle(j, Row)
    if WithPause2:
        basic.pause(50)

def on_every_interval():
    pass
loops.every_interval(500, on_every_interval)

def on_forever():
    pass
basic.forever(on_forever)

def on_forever2():
    if blink:
        pins.digital_write_pin(DigitalPin.P1, 1)
        basic.pause(300)
        pins.digital_write_pin(DigitalPin.P1, 0)
        basic.pause(300)
basic.forever(on_forever2)
