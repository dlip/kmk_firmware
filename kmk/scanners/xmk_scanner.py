# Copyright 2023 Manna Harbour
# github.com/manna-harbour/xmk

import keypad

from kmk.scanners import Scanner


class xMKScanner(Scanner):
    def __init__(self, key_count):
        self.queue = []
        self._key_count = key_count

    def xmk_key(self, key, press):
        self.queue.append((key, press))

    def scan_for_changes(self):
        if self.queue:
            (key, press) = self.queue.pop(0)
            return keypad.Event(key, press)

    @property
    def key_count(self):
        return self._key_count
