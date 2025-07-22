let A = 0
input.onGesture(Gesture.EightG, function on_gesture_eight_g() {
    
})
input.onButtonPressed(Button.A, function on_button_pressed_a() {
    
    A = 0
})
loops.everyInterval(500, function on_every_interval() {
    
})
basic.forever(function on_forever() {
    pins.digitalWritePin(DigitalPin.P1, 1)
})
