let blink = 0
let reset_flag = 0
function Turn_Right() {
    basic.clearScreen()
    for (let index = 0; index < 4; index++) {
        Turn_Right_Anime()
    }
    for (let index2 = 0; index2 < 2; index2++) {
        basic.showArrow(ArrowNames.North)
        basic.pause(10)
        basic.clearScreen()
        basic.pause(500)
    }
}

input.onButtonPressed(Button.A, function on_button_pressed_a() {
    
    basic.clearScreen()
    blink = 0
})
input.onGesture(Gesture.LogoUp, function on_gesture_logo_up() {
    
    reset_flag = 1
    blink = 1
    while (!input.isGesture(Gesture.ScreenUp)) {
        Turn_Left()
    }
    reset_flag = 0
    blink = 0
    basic.clearScreen()
})
input.onGesture(Gesture.ScreenUp, function on_gesture_screen_up() {
    basic.clearScreen()
    if (reset_flag) {
        control.reset()
    }
    
})
function Turn_Left_Anime() {
    Toggle_all_of_column(4, false)
    Toggle_all_of_column(3, false)
    Toggle_all_of_column(2, false)
    Toggle_all_of_column(1, false)
    Toggle_all_of_column(0, true)
    Toggle_all_of_column(4, true)
    Toggle_all_of_column(3, true)
    Toggle_all_of_column(2, true)
    Toggle_all_of_column(1, true)
    Toggle_all_of_column(0, true)
    basic.pause(100)
}

function Turn_Right_Anime() {
    Toggle_all_of_row(4, false)
    Toggle_all_of_row(3, false)
    Toggle_all_of_row(2, false)
    Toggle_all_of_row(1, false)
    Toggle_all_of_row(0, true)
    Toggle_all_of_row(4, true)
    Toggle_all_of_row(3, true)
    Toggle_all_of_row(2, true)
    Toggle_all_of_row(1, true)
    Toggle_all_of_row(0, true)
    basic.pause(100)
}

input.onGesture(Gesture.TiltRight, function on_gesture_tilt_right() {
    
    reset_flag = 1
    blink = 1
    while (!input.isGesture(Gesture.ScreenUp)) {
        Turn_Right()
    }
    reset_flag = 0
    blink = 0
    basic.clearScreen()
})
function Turn_Left() {
    basic.clearScreen()
    for (let index3 = 0; index3 < 4; index3++) {
        Turn_Left_Anime()
    }
    for (let index4 = 0; index4 < 2; index4++) {
        basic.showArrow(ArrowNames.West)
        basic.pause(10)
        basic.clearScreen()
        basic.pause(500)
    }
}

function Toggle_all_of_column(column: number, WithPause: boolean) {
    for (let i = 0; i < 5; i++) {
        led.toggle(column, i)
    }
    if (WithPause) {
        basic.pause(100)
    }
    
}

function Toggle_all_of_row(Row: number, WithPause2: boolean) {
    for (let j = 0; j < 5; j++) {
        led.toggle(j, Row)
    }
    if (WithPause2) {
        basic.pause(50)
    }
    
}

loops.everyInterval(500, function on_every_interval() {
    
})
basic.forever(function on_forever() {
    
})
basic.forever(function on_forever2() {
    if (blink) {
        pins.digitalWritePin(DigitalPin.P1, 1)
        basic.pause(300)
        pins.digitalWritePin(DigitalPin.P1, 0)
        basic.pause(300)
    }
    
})
