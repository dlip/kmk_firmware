<!-- Copyright 2023 Manna Harbour -->
<!-- github.com/manna-harbour/xmk -->

# xmk

![𝑥MK](https://github.com/manna-harbour/xmk/blob/main/docs/images/xmk-banner.jpg)

[𝑥MK](https://github.com/manna-harbour/xmk) facilitates the use of programmable keyboard firmware with any keyboard.

This keyboard definition enables [use of 𝑥MK with KMK](https://github.com/manna-harbour/xmk#kmk).

## Required Modules

### xMKShell

The [xMKShell](/kmk/modules/xmk_shell.py) module reads keymap key position press and release commands via usb_cdc and registers the events with xMKScanner.

### xMKScanner

The [xMKScanner](/kmk/scanners/xmk_scanner.py) scanner receives events from xMKShell and passes on the corresponding state changes.

## Microcontroller Support
Supports any KMK-compatible MCU board. No modification to `kb.py` is required.

