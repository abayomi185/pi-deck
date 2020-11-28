#!/usr/bin/env python3


message = libserver.Message(sel, conn, addr)
sel.register(conn, selectors.EVENT_READ, data=message)

while True:
    events = sel.select(timeout=None)
    for key, mask in events:
        # ...
        message = key.data
        message.process_events(mask)


def process_events(self, mask):
    if mask & selectors.EVENT_READ:
        self.read()
    if mask & selectors.EVENT_WRITE:
        self.write()