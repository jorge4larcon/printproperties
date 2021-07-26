#!/usr/bin/env python

"""printproperties: A CLI to print properties from gradle.properties files
"""

import argparse
import os
import sys

from dotenv import dotenv_values


def run(args):
    if not os.path.isfile(args.properties_file):
        sys.exit(f'The file "{args.properties_file}" does not exist')

    properties = dotenv_values(args.properties_file)
    try:
        print(properties[args.property], end="")
    except KeyError:
        sys.exit(
            f'The property "{args.property}" doesn not exist in '
            f'"{args.properties_file}"'
        )


def parse_args():
    parser = argparse.ArgumentParser(
        description="This is a CLI to print the value of properties inside "
        "gradle.properties files.",
        prog="printproperties",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )
    parser.add_argument(
        "-f", "--file",
        metavar="FILE",
        type=str,
        default="gradle.properties",
        help="the path of the gradle.properties file",
        dest="properties_file"
    )
    parser.add_argument(
        "-p", "--property",
        metavar="PROPERTY",
        type=str,
        help="the name of the property in the gradle.properties file you "
        "want to print",
        dest="property",
        required=True
    )
    parser.add_argument(
        "--version",
        action="version",
        version="%(prog)s 0.0.1"
    )
    return parser.parse_args()


def main():
    args = parse_args()
    run(args)


if __name__ == "__main__":
    main()
