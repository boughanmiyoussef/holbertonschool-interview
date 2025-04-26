#!/usr/bin/python3
"""Log parser that prints stats every 10 lines or on interrupt."""

import sys
import select


total_size = 0
status_counts = {}
valid_codes = ['200', '301', '400', '401', '403', '404', '405', '500']
line_num = 0


def print_stats():
    print("File size: {}".format(total_size))
    for code in sorted(status_counts.keys()):
        print("{}: {}".format(code, status_counts[code]))


try:
    # Check if there's data to read from stdin
    if select.select([sys.stdin], [], [], 0.1)[0]:
        for line in sys.stdin:
            parts = line.strip().split()
            if len(parts) < 7:
                continue

            status = parts[-2]
            size = parts[-1]

            if status in valid_codes:
                status_counts[status] = status_counts.get(status, 0) + 1

            try:
                total_size += int(size)
            except ValueError:
                continue

            line_num += 1
            if line_num % 10 == 0:
                print_stats()

except KeyboardInterrupt:
    print_stats()
    raise

print_stats()
