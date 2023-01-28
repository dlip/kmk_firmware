# Copyright 2023 Manna Harbour
# github.com/manna-harbour/xmk

# Based on https://github.com/KMKfw/kmk_firmware/blob/1935f05ccb52e04012eca6976d85cd328c3b5c68/kmk/modules/serialace.py

from usb_cdc import data

from kmk.modules import Module
from kmk.utils import Debug

debug = Debug(__name__)


class xMKShell(Module):
    buffer = bytearray()

    def during_bootup(self, keyboard):
        try:
            data.timeout = 0
        except AttributeError:
            pass

    def before_matrix_scan(self, keyboard):
        pass

    def after_matrix_scan(self, keyboard):
        pass

    def process_key(self, keyboard, key, is_pressed, int_coord):
        return key

    def before_hid_send(self, keyboard):
        # Serial.data isn't initialized.
        if not data:
            return

        # Nothing to parse.
        if data.in_waiting == 0:
            return

        self.buffer.extend(data.read())
        idx = self.buffer.find(b'\n')

        # No full command yet.
        if idx == -1:
            return

        line = (self.buffer[:idx]).decode('utf-8')
        self.buffer = self.buffer[idx + 1 :]
        split = line.split()
        if split[0] == 'key':
            if split[1] == 'press':
                keyboard.matrix[0].xmk_key(int(split[2]), True)
            elif split[1] == 'release':
                keyboard.matrix[0].xmk_key(int(split[2]), False)

    def after_hid_send(self, keyboard):
        pass

    def on_powersave_enable(self, keyboard):
        pass

    def on_powersave_disable(self, keyboard):
        pass
