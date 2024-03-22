
import zenoh

from dataclasses import dataclass
from pycdr2 import IdlStruct
from pycdr2.types import int64, float64

import time

@dataclass
class MathServerRequest(IdlStruct):
   x: int64
   op: str
   y: int64


@dataclass
class MathServerResponse(IdlStruct):
   res: int64
   success: bool


def reply_callback(reply):
    try:
        message = MathServerResponse.deserialize(reply.ok.payload)
        print(f">> Received {message}")
    except:
        print(">> Received ERROR")

def main():

    session = zenoh.open()

    req = MathServerRequest(x=6,op="*",y=2).serialize()
    replies = session.get("calculator", handler=zenoh.Queue(), value=req)
    for reply in replies.receiver:
        reply_callback(reply)
        


    session.close()

main()