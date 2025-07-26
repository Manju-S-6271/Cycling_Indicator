let A = 0
function Turn_Right() {
    basic.showLeds(`
        . . . . .
        . . . . .
        . . . . .
        . . . . .
        . . . . .
        `)
    basic.pause(10)
    basic.showLeds(`
        # # # # #
        # # # # #
        # # # # #
        . . . . .
        . . . . .
        `)
    basic.pause(10)
    basic.showLeds(`
        . . . . .
        . . . . .
        . . . . .
        . . . . .
        . . . . .
        `)
    basic.pause(10)
    basic.showArrow(ArrowNames.North)
    basic.pause(10)
}

input.onGesture(Gesture.EightG, function on_gesture_eight_g() {
    
})
input.onButtonPressed(Button.A, function on_button_pressed_a() {
    
    A = 0
})
input.onGesture(Gesture.LogoUp, function on_gesture_logo_up() {
    Turn_Left()
})
function Turn_Left() {
    basic.showLeds(`
        . . . . .
        . . . . .
        . . . . .
        . . . . .
        . . . . .
        `)
    basic.pause(10)
    basic.showLeds(`
        # # # . .
        # # # . .
        # # # . .
        # # # . .
        # # # . .
        `)
    basic.pause(10)
    basic.showLeds(`
        . . . . .
        . . . . .
        . . . . .
        . . . . .
        . . . . .
        `)
    basic.pause(10)
    basic.showArrow(ArrowNames.West)
    basic.pause(10)
}

input.onGesture(Gesture.TiltRight, function on_gesture_tilt_right() {
    Turn_Right()
})
loops.everyInterval(500, function on_every_interval() {
    
})
basic.forever(function on_forever() {
    
})
basic.forever(function on_forever2() {
    
})
