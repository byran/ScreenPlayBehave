#!/usr/bin/env python3
import sys
import json
import pathlib
from os import path
from jinja2 import Template


my_path = pathlib.Path(__file__).parent.absolute()


def read_datafile(filename: str):
    filepath = path.join(my_path, filename)
    if not path.exists(filepath):
        print('Unable to find {filename}\n'.format(filename=filename))
        exit(2)

    with open(filepath) as file:
        return json.load(file)


def read_template():
    filepath = path.join(my_path, 'metrics.template')
    if not path.exists(filepath):
        print('Unable to find template\n')
        exit(2)

    with open(filepath) as file:
        return file.read()


def non_class_complexity(file):
    count = 0
    for item in file:
        if item['type'] != "class":
            count = count + 1
    return count


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print('Invalid arguments:\n{cmd} <output file>\n'.format(cmd=sys.argv[0]))
        exit(1)

    mi = read_datafile('mi.json')
    cc = read_datafile('cc.json')
    raw = read_datafile('raw.json')
    template = read_template()

    context = {
        "mi": mi,
        "cc": cc,
        "raw": raw,
        "non_class_complexity": non_class_complexity
    }

    with open(sys.argv[1], 'wt') as file:
        file.write(Template(template).render(**context))
