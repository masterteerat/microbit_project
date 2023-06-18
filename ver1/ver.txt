ans = 0
ascii2 = randint(48, 57)
#ascii2 = 255

weight = 7
basic.show_string(String.from_char_code(ascii2))

while True:
    if input.button_is_pressed(Button.A):
        music.play(music.string_playable("C5 C5 B B C5 - - - ", 1500),
            music.PlaybackMode.IN_BACKGROUND)
        ans = ans + (2 ** weight)
        weight += -1
    if input.button_is_pressed(Button.B):
        music.play(music.string_playable("E E F F G - - - ", 1500),
            music.PlaybackMode.IN_BACKGROUND)
        weight += -1
    if weight == 0:
        if ans == ascii2:
            basic.show_icon(IconNames.YES)
            break
        if ans != ascii2:
            basic.show_icon(IconNames.NO)
            break
    basic.pause(300)
           