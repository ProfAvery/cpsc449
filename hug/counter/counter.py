import os
import pprint
import socket
import threading
import time

import hug

COUNTER = 0


def counter():
    global COUNTER
    while True:
        COUNTER += 1
        time.sleep(1)


@hug.get("/count")
def count(request):
    pprint.pprint(request)
    global COUNTER
    return {"counter": COUNTER}


@hug.post("/reset")
def reset():
    global COUNTER
    COUNTER = 0
    hug.redirect.to("/count")


@hug.startup()
def setup_thread(api):
    print(os.environ["PORT"], socket.getfqdn())
    t = threading.Thread(target=counter, daemon=True)
    t.start()


def post_worker_init(worker):
    __hug__._ensure_started()
