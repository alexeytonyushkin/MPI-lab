#!/usr/bin/env python

import twinleaf
import argparse


def interact(url: str = 'tcp://localhost'):
    parser = argparse.ArgumentParser(prog='itl',
                                     description='Interactive Twinleaf I/O.')

    parser.add_argument("url",
                        nargs='?',
                        default='tcp://localhost',
                        help='URL: tcp://localhost')
    parser.add_argument("-s",
                        default='',
                        help='Routing: /0/1...')
    args = parser.parse_args()

    dev = twinleaf.Device("COM7")
    dev._interact()


if __name__ == "__main__":
    interact()