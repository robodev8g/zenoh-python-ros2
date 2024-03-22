import zenoh

from dataclasses import dataclass
from pycdr2 import IdlStruct
from pycdr2.types import int64, float64

import time

@dataclass
class String(IdlStruct):
   data: str

@dataclass
class Special(IdlStruct):
   a: int64
   b: float64
   c: str

session = zenoh.open()

# s = String(data="hi").serialize()
s = Special(a=6,b=7.5,c="lol").serialize()

while True:
    # session.put('information', s)
    session.put('special_for_all', s)
    time.sleep(1)
