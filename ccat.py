"""
ccat - A Python implementation of the Unix cat command
"""

import argparse
import sys

def read_file(filename):
    """
    Read file content in binary mode.

    Args:
        filename: path to the file to read

    Returns:
        bytes: file content as bytes
    """
    with open(filename, 'rb') as f:
        f.read()


def main():
    """
    Main function to parse arguments and execute the appropriate counting operation.
    """
    parser = argparse.ArgumentParser(
        description="ccat command"
    ) 

    parser.add_argument('filename', nargs='?', default=None,
                        help='file to analyze (if not provided, reads from stdin)')
    
    args = parser.parse_args()

    try:
        if args.filename:
            content = read_file(args.filename)
        else:
            content = sys.stdin.buffer.read()
    except FileNotFoundError:
        print(f"ccat: {args.filename}: No such file or directory", file=sys.stderr)
        exit(1)
    except PermissionError:
        print(f"You don't have permission to read this file", file=sys.stderr)
        exit(1)
    except IOError as e:
        print(f"Unexpected IO error : {e}", file=sys.stderr)
        exit(1)

    print(content, file=sys.stdout)

if __name__== '__main__':
    main()