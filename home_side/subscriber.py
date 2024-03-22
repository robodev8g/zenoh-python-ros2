import zenoh
from zenoh.session import Reliability, Sample

import argparse
import time

from dataclasses import dataclass
from pycdr2 import IdlStruct
from pycdr2.types import int64, float64

@dataclass
class String(IdlStruct):
   data: str

@dataclass
class Special(IdlStruct):
   a: int64
   b: float64
   c: str

def create_parser():
    parser = argparse.ArgumentParser(
    prog='z_sub',
    description='zenoh sub example')
    parser.add_argument('--key', '-k', dest='key',
                    default='demo/example/**',
                    type=str,
                    help='The key expression to subscribe to.')
    return parser


def main():
    parser = create_parser()
    args = parser.parse_args()
    session = zenoh.open()
    # sub = session.declare_subscriber(args.key, word_callback,  reliability=Reliability.BEST_EFFORT())
    sub = session.declare_subscriber("special_only", special_message_callback,  reliability=Reliability.BEST_EFFORT())
    
    while True:
        time.sleep(1)
    

def word_callback(sample: Sample):
    message = String.deserialize(sample.payload)
    print(f">> [Subscriber] Received {message.data}")
    

def special_message_callback(sample: Sample):
    message = Special.deserialize(sample.payload)
    print(f">> [Subscriber] Received {message.a}, {message.b}, {message.c}")



if __name__ == "__main__":
    main()