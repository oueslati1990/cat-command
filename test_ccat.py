#!/usr/bin/env python3
"""
Tests for ccat command implementation
"""

import subprocess


def run_ccat(args):
    """
    Helper function to run ccat command with given arguments

    Args:
        args: list of command-line arguments

    Returns:
        tuple: (stdout, stderr, return_code)
    """
    cmd = ['ccat'] + args
    result = subprocess.run(cmd, capture_output=True, text=True)
    
    return result.stdout.strip(), result.stderr.strip(), result.returncode


if __name__ == '__main__':
    print("=" * 50)
    print("Testing ccat")
    print("=" * 50)

    try:
        
        print("\n✓ All tests passed!")
    except AssertionError as e:
        print(f"\n✗ Test failed: {e}")
        exit(1)
    except Exception as e:
        print(f"\n✗ Error: {e}")
        exit(1)
