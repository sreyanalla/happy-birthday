def on_button_pressed_a():
    basic.show_leds("""
        . . . . .
        . # . # .
        . . . . .
        # . . . #
        . # # # .
        """)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_ab():
    music.start_melody(music.built_in_melody(Melodies.BIRTHDAY), MelodyOptions.ONCE)
    basic.show_string("Happy Birthday!")
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    basic.show_leds("""
        . . . . .
        . # . # .
        . . . . .
        . # # # .
        # . . . #
        """)
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_forever():
    pass
basic.forever(on_forever)
