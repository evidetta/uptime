#!/usr/bin/env python

import re
import subprocess
import sys

from datetime import datetime, timedelta

DAYS_DURATION_REGEX = '([0-9]+)\+([0-1][0-9]|2[0-3]):([0-5][0-9])'
HOURS_DURATION_REGEX = '([0-1][0-9]|2[0-3]):([0-5][0-9])'


def parse_start_time(start_time: str) -> datetime:
    dt = datetime.strptime(start_time, '%a %b %d %H:%M:%S %Y')
    return dt


def parse_duration(duration: str) -> timedelta:
    mo = re.match(DAYS_DURATION_REGEX, duration)
    if mo:
        tuple = mo.groups()
        return timedelta(
            days=int(tuple[0]),
            hours=int(tuple[1]),
            minutes=int(tuple[2])
        )
    mo = re.match(HOURS_DURATION_REGEX, duration)
    if mo:
        tuple = mo.groups()
        return timedelta(
            hours=int(tuple[0]),
            minutes=int(tuple[1])
        )
    raise Exception


def print_log(start_time: str, duration: str):
    print('\"{st}\",\"{duration}\"'.format(
        st=parse_start_time(start_time).strftime("%Y-%m-%d %H:%M"),
        duration=parse_duration(duration)
    ))


def main():
    cmd = ['last', 'reboot', '--fulltimes']
    proc = subprocess.Popen(
        cmd,
        stdout=subprocess.PIPE
    )

    lines = proc.stdout.readlines()
    lines = lines[1:-1]

    for line in lines:
        if line == b'\n':
            break

        clean_line = line.\
            decode().\
            split()

        start_time = ' '.join([
            x for x in clean_line[4:9]
        ])

        duration = clean_line[-1].\
            replace('(', '').\
            replace(')', '')

        print_log(start_time, duration)


if __name__ == "__main__":
    sys.exit(main())
