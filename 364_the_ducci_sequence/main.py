# -*- coding: utf-8 -*-
import argparse
import sys
from itertools import tee


def pairwise(iterable):
    "s -> (s0,s1), (s1,s2), (s2, s3), ..."
    a, b = tee(iterable)
    next(b, None)
    return zip(a, b)


def print_ducci(integer_list: list):
    print('[%s]' % '; '.join([str(i) for i in integer_list]))


def ducci_sequence(integer_list: list, steps: int, seen: list):
    '''Print the Ducci Sequence from a list of integers.'''
    if sum(integer_list) == 0:
        print(f'{steps} steps')
        return

    tmp_integer_list = integer_list.copy()
    tmp_integer_list.append(integer_list[0])
    parcels = pairwise(tmp_integer_list)
    new_list = [abs(p[0] - p[1]) for p in parcels]
    
    if new_list in seen:
        print(f'{steps + 1} steps')
        return
    
    print_ducci(integer_list)
    new_seen = seen.copy()
    new_seen.append(new_list)
    ducci_sequence(new_list, steps + 1, new_seen)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='/r/dailyprogrammer challenge #364 - The Ducci Sequence.')
    parser.add_argument('tuple', metavar='tuple', type=str, help='Comma-separated list of integers to build a tuple.')
    args = parser.parse_args()
    
    try:
        integer_list = [int(i) for i in args.tuple.split(',')]
        if len(integer_list) < 2:
            raise ValueError('Needs at least 2 integers.')
        
        ducci_sequence(integer_list, 1, [])
    except ValueError:
        print('Invalid tuple - should be a list with a minimum of two comma-separated integers.')
        sys.exit(-1)
