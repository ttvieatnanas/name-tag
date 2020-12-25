input.onButtonPressed(Button.A, function () {
    soundExpression.twinkle.playUntilDone()
    basic.showLeds(`
        . # . # .
        # # # # #
        . # # # .
        . . # . .
        . . . . .
        `)
})
