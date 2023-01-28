# Copyright 2023 Manna Harbour
# github.com/manna-harbour/xmk

from kb import KMKKeyboard

from kmk.keys import KC

keyboard = KMKKeyboard()

# fmt: off
keyboard.keymap = [
    [KC.Q],    [KC.W],    [KC.F],    [KC.P],    [KC.B],             [KC.J],    [KC.L],    [KC.U],    [KC.Y],    [KC.QUOT],
    [KC.A],    [KC.R],    [KC.S],    [KC.T],    [KC.G],             [KC.M],    [KC.N],    [KC.E],    [KC.I],    [KC.O],
    [KC.Z],    [KC.X],    [KC.C],    [KC.D],    [KC.V],             [KC.K],    [KC.H],    [KC.COMM], [KC.DOT],  [KC.SLSH],
                          [KC.ESC],  [KC.SPC],  [KC.TAB],           [KC.ENT],  [KC.BSPC], [KC.DEL]
]
# fmt: on

if __name__ == '__main__':
    print('starting xmk')
    keyboard.go()
