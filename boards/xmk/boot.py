# Copyright 2023 Manna Harbour
# github.com/manna-harbour/xmk

import supervisor

import usb_cdc

supervisor.set_next_stack_limit(4096 + 4096)
usb_cdc.enable(data=True)
