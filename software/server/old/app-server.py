#!/usr/bin/env python3

    # "python.analysis.diagnosticSeverityOverrides": {
    #     "reportMissingImports": "none"
    # }

import selectors

import libserver

sel = selectors.DefaultSelector()

message = libserver.Message(sel, conn, addr)
sel.register(conn, selectors.EVENT_READ, data=message)

def accept_wrapper(sock):
    conn, addr = sock.accept()  # Should be ready to read
    print('accepted connection from', addr)
    conn.setblocking(False)
    message = libserver.Message(sel, conn, addr)
    sel.register(conn, selectors.EVENT_READ, data=message)

while True:
    events = sel.select(timeout=None)
    for key, mask in events:
        # ...
        message = key.data
        message.process_events(mask)



