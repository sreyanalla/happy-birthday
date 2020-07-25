input.onButtonPressed(Button.A, function on_button_pressed_a() {
    basic.showLeds(`
        . . . . .
        . # . # .
        . . . . .
        # . . . #
        . # # # .
        `)
})
input.onButtonPressed(Button.AB, function on_button_pressed_ab() {
    music.startMelody(music.builtInMelody(Melodies.Birthday), MelodyOptions.Once)
    basic.showString("Happy Birthday!")
})
input.onButtonPressed(Button.B, function on_button_pressed_b() {
    basic.showLeds(`
        . . . . .
        . # . # .
        . . . . .
        . # # # .
        # . . . #
        `)
})
basic.forever(function on_forever() {
    
})
