import argparse
import textwrap
import pkg_resources

__all__ = ["get_parser"]

try:
    VERSION = pkg_resources.require("fillname")[0].version
except pkg_resources.DistributionNotFound:
    VERSION = '0.0.0'

def get_parser():
    """
    Get the parser for the command line
    """
    # pylint: disable=anomalous-backslash-in-string
    parser = argparse.ArgumentParser(description=textwrap.dedent("""
    fillname
    filldescription
    """),
    formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument('-log', default="warning",
                choices=['debug', 'info', 'error', 'warning'],
                help=textwrap.dedent('''\
                    Provide logging level.
                    {debug|info|error|warning}
                        (default: %(default)s)'''),
                type=str,
                metavar='')
    parser.add_argument('--version','-v', action='version',
                version=f'%(prog)s {VERSION}')
    return parser
