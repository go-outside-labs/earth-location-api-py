#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
# api/main.py

import argparse
from .methods import get_location


def run_menu() -> argparse.ArgumentParser:

    parser = argparse.ArgumentParser(description='🌏✨ location api ✨🌏')
    parser.add_argument('-l', dest='location', nargs=1,
                        help="Find the latitude and longitude of a city. \
                        Example: loc -l <city>")
    return parser


def run() -> None:
    """Entry point for this module."""

    parser = run_menu()
    args = parser.parse_args()

    if args.location:
        data = get_location(args.location[0])
        for key, value in data.items():
            print(f'{key}: {value}')

    else:
        parser.print_help()


if __name__ == "__main__":

    run()
