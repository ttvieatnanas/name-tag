def on_button_pressed_a():
    soundExpression.twinkle.play_until_done()
    basic.show_leds("""
        . # . # .
        # # # # #
        . # # # .
        . . # . .
        . . . . .
        """)
input.on_button_pressed(Button.A, on_button_pressed_a)
