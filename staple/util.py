""" Utility functions """

import subprocess


def day_count(start_date, end_date):
    return (end_date - start_date).days + 1


def run_shell(*args):
    output = subprocess.run(args, stdout=subprocess.PIPE).stdout.decode('ascii').rstrip()
    return output


def run_raw_shell(*args):
    output = subprocess.run(args, stdout=subprocess.PIPE, shell=True).stdout.decode('ascii').rstrip()
    return output

