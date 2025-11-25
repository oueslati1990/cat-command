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
        return f.read()


def main():
    """
    Main function to parse arguments and execute the appropriate counting operation.
    """
    parser = argparse.ArgumentParser(
        description="ccat command"
    ) 

    parser.add_argument('filenames', nargs='*', default=None,
                        help='file(s) to analyze (if not provided, reads from stdin)')
    parser.add_argument('-n', '--number', action="store_true",
                        help="number the lines")
    parser.add_argument('-b', '--blank', action="store_true",
                        help="excluding blank lines from input")
    
    args = parser.parse_args()

    try:
        content = b''
        if args.filenames:
            for filename in args.filenames:
                content += read_file(filename)
        else:
            content = sys.stdin.buffer.read()
    except FileNotFoundError:
        print(f"ccat: {filename}: No such file or directory", file=sys.stderr)
        exit(1)
    except PermissionError:
        print(f"You don't have permission to read this file", file=sys.stderr)
        exit(1)
    except IOError as e:
        print(f"Unexpected IO error : {e}", file=sys.stderr)
        exit(1)

    lines_numbered = ''
    index = 0
    lines = content.decode('utf-8').split('\n')
    for i, line in enumerate(lines):
        if args.number:
            lines_numbered += f"{index+1} {line}\n"
            index+=1
        elif args.blank:
            if line:
                lines_numbered += f"{index+1} {line}\n"
                index+=1
        else:
            # Add newline except for the last line if it's empty
            if i < len(lines) - 1:
                lines_numbered += f"{line}\n"
            elif line:  # Last line is not empty, add it with newline
                lines_numbered += f"{line}\n"
            # If last line is empty, don't add anything

    print(lines_numbered, file=sys.stdout, end='')

if __name__ == '__main__':
    main()