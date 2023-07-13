#!/usr/bin/env python3

"""sftg SOTA FLE template generator
"""

import argparse
import datetime

if __name__ == '__main__':

    DEFAULT_MYCALL = 'WU7H'
    DEFAULT_DATE = datetime.date.isoformat(datetime.date.today())

    parser = argparse.ArgumentParser(description='SOTA FLE template generator')
    parser.add_argument(
        'mysota',
        type=str,
        help='my SOTA summit reference')
    parser.add_argument(
        'date',
        type=str,
        default=DEFAULT_DATE,
        nargs='?',
        help=f'date (YYYY-MM-DD) (default:  today, {DEFAULT_DATE})')
    args = parser.parse_args()

    print(f'mycall {DEFAULT_MYCALL}')
    print(f'date {args.date}')
    print(f'mysota {args.mysota.upper()}')
