#!/usr/bin/env python

"""printproperties: A CLI to retrieve properties from gradle.properties files
"""

import argparse
import sys

from dotenv import dotenv_values


def run(args):
    properties = dotenv_values(args.properties_file)
    try:
        print(properties[args.property])
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
        "-g", "--gradle-properties",
        metavar="GRADLE_PROPERTIES",
        type=str,
        default="gradle.properties",
        help="this is the path to the gradle.properties file",
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
        version="%(prog)s 1.0"
    )
    return parser.parse_args()


def main():
    args = parse_args()
    run(args)


if __name__ == "__main__":
    main()
