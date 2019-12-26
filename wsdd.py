import os
import sys
import math
import json
from glob import glob
import codecs

# call wsd for an entire directory, put output files in a subfolder

def parse_args():
    '''
    Parse and return command line arguments.
    '''
    ruletypes = get_rule_types()
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('directory', type=str,  #this is what is changed from the other arg parse
        help='directory of files',)
    parser.add_argument('rules', type=str, nargs='*',
        help = 'rule type followed by arguments required by this type\n' +
        'available types of rules are: ' + ', '.join(ruletypes))
    #parser.add_argument('--info', type=str, metavar='RULETYPE',
    #    help='show number of arguments and docstrings of a specific rule type')
    export = parser.add_argument_group('export')
    html_group = parser.add_argument_group('html')
    json_group = parser.add_argument_group('json')
    export.add_argument('-o', '--outfile', action='store',
        help='output file name')
    export.add_argument('-f', '--output-format',
        default='html', choices=('json', 'html'),
        help='output file format')
    export.add_argument('-e', '--include-empty', action='store_true',
        help='Include empty rules to output')
    html_group.add_argument('-nec', '--no-embed-css', action='store_true',
        help="don't embed style.css into generated html file")
    json_group.add_argument('-r', '--reftext', action='store_true',
        help='insert a reference to the text file into the output \
        json file instead of the list of matching lines')
    json_group.add_argument('-a', '--abspath', action='store_true',
        help='insert absolute path to the text file into the output \
        json file instead of the path passed to command line')
    json_group.add_argument('-i', '--indent',
        type=int, action='store', default=4,
        help='json indent size')
    try:
        args = parser.parse_args()
    except Exception as exc:
        LOG.error(exc)
        sys.exit(1)
    if args.indent == 0:
        args.indent = None
    return args

if __name__ == '__main__':
    print(parse_args())
    sys.exit(main(parse_args()))
