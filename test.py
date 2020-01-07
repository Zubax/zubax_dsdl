#!/usr/bin/env python3
# TODO: https://github.com/UAVCAN/public_regulated_data_types/issues/68

import sys
import time
import string
import pydsdl
from functools import partial


MAX_LINE_LENGTH = 120
ALLOWED_CHARACTERS = set(string.digits + string.ascii_letters + string.punctuation + ' ')


def die_at(ty, line_index, *text):
    prefix = '%s:%d:' % (ty.source_file_path, line_index + 1)
    print(prefix, *text, file=sys.stderr)
    sys.exit(1)


def on_print(file_path, line, value):
    print('%s:%d: %s' % (file_path, line, value), file=sys.stderr)


output = []
for ns in ['zubax', 'zubax_internet']:
    output += pydsdl.read_namespace(
        ns,
        [
            'public_regulated_data_types/uavcan',
        ],
        print_output_handler=on_print
    )

for t in output:
    print(t)
    text = open(t.source_file_path).read()
    for index, line in enumerate(text.split('\n')):
        line = line.strip('\r\n')
        abort = partial(die_at, t, index)

        # Check header comment
        if index == 0 and not line.startswith('# '):
            abort('Every data type definition shall have a header comment')

        # Check trailing comment placement
        # TODO: this test breaks on string literals containing "#"
        if not line.startswith('#') and '#' in line and '  #' not in line:
            abort('Trailing line comments shall be separated from the preceding text with at least two spaces')

        if line != '#' and '#' in line and '# ' not in line:
            abort('The text of a comment shall be separated from the comment character with a single space')

        if line.endswith(' '):
            abort('Trailing spaces are not permitted')

        # Check line length limit
        if len(line) > MAX_LINE_LENGTH:
            abort('Line is too long:', len(line), '>', MAX_LINE_LENGTH, 'chars')

        # Make sure we're not using any weird characters such as tabs or non-ASCII-printable
        for char_index, char in enumerate(line):
            if char not in ALLOWED_CHARACTERS:
                abort('Disallowed character', repr(char), 'code', ord(char), 'at column', char_index + 1)

    if not text.endswith('\n') or text.endswith('\n' * 2):
        abort('A file shall contain exactly one blank line at the end')
