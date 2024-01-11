"""
print the following after every ten lines or the input
    - the files's total size.
    - Count of read status codes up to that point.
"""


def print_stats(size, status_codes):
    """amount of printed metrics.

    Args:
        size (int): the total amout of the read file size.
        status_codes (dict): the number of status code gathered.
    """





    101-stats.py
#!/usr/bin/python3
"""
print the following after every ten lines or the input of ctrl D
    - the files's total size.
    - Count of read status codes up to that point.
"""


def print_stats(size, status_codes):
     """amount of printed metrics.

    Args:
        size (int): the total amout of the read file size.
        status_codes (dict): the number of status code gathered.
    """
    print("File size: {}".format(size))
    for key in sorted(status_codes):
        print("{}: {}".format(key, status_codes[key]))


if __name__ == "__main__":
    import sys

    size = 0
    status_codes = {}
    valid_codes = ['200', '301', '400', '401', '403', '404', '405', '500']
    count = 0

    try:
        for line in sys.stdin:
            if count == 10:
                print_stats(size, status_codes)
                count = 1
            else:
                count += 1

            line = line.split()

            try:
                size += int(line[-1])
            except (IndexError, ValueError):
                pass

            try:
                if line[-2] in valid_codes:
                    if status_codes.get(line[-2], -1) == -1:
                        status_codes[line[-2]] = 1
                    else:
                        status_codes[line[-2]] += 1
            except IndexError:
                pass

        print_stats(size, status_codes)

    except KeyboardInterrupt:
        print_stats(size, status_codes)
        raise
