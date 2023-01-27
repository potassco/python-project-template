__all__ = ["main"]

import sys
from .utils.parser import get_parser
from .utils.logger import setup_logger_str

def main():
    '''
    Runs the main function
    '''
    parser= get_parser()
    args = parser.parse_args()
    log = setup_logger_str(args.log)
    log.debug(args)

    print("Project template!")

    sys.exit()