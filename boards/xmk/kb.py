# Copyright 2023 Manna Harbour
# github.com/manna-harbour/xmk

from kmk.kmk_keyboard import KMKKeyboard as _KMKKeyboard
from kmk.modules.xmk_shell import xMKShell
from kmk.scanners.xmk_scanner import xMKScanner


class KMKKeyboard(_KMKKeyboard):
    def __init__(self, key_count=128):
        self.matrix = [xMKScanner(key_count)]
        self.modules.append(xMKShell())
