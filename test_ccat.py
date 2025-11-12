#!/usr/bin/env python3
"""
Tests for ccat command implementation
"""

import subprocess
import os
import tempfile


def run_ccat(args, input_data=None):
    """
    Helper function to run ccat command with given arguments

    Args:
        args: list of command-line arguments
        input_data: optional string to pass as stdin

    Returns:
        tuple: (stdout, stderr, return_code)
    """
    cmd = ['ccat'] + args
    result = subprocess.run(
        cmd,
        capture_output=True,
        text=True,
        input=input_data
    )

    return result.stdout, result.stderr.strip(), result.returncode


def test_read_valid_file():
    """Test reading a valid file"""
    print("\n[Test 1] Reading valid file (test.txt)...")
    stdout, stderr, returncode = run_ccat(['test.txt'])
    assert returncode == 0, f"Expected return code 0, got {returncode}"
    assert stderr == "", f"Expected no stderr, got: {stderr}"
    assert len(stdout) > 0, "Expected output, got empty string"
    assert "ocean" in stdout, "Expected content from test.txt"
    print("✓ Test 1 passed: Successfully read test.txt")


def test_nonexistent_file():
    """Test handling of non-existent file"""
    print("\n[Test 2] Handling non-existent file...")
    stdout, stderr, returncode = run_ccat(['nonexistent_file.txt'])
    assert returncode == 1, f"Expected return code 1, got {returncode}"
    assert "No such file or directory" in stderr, f"Expected error message, got: {stderr}"
    print("✓ Test 2 passed: Correctly handled non-existent file")


def test_read_from_stdin():
    """Test reading from stdin"""
    print("\n[Test 3] Reading from stdin...")
    test_input = "Hello from stdin!\nLine 2\n"
    stdout, stderr, returncode = run_ccat([], input_data=test_input)
    assert returncode == 0, f"Expected return code 0, got {returncode}"
    assert stdout == test_input, f"Expected '{test_input}', got '{stdout}'"
    assert stderr == "", f"Expected no stderr, got: {stderr}"
    print("✓ Test 3 passed: Successfully read from stdin")


def test_empty_file():
    """Test reading an empty file"""
    print("\n[Test 4] Reading empty file...")
    with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.txt') as f:
        temp_file = f.name
    try:
        stdout, stderr, returncode = run_ccat([temp_file])
        assert returncode == 0, f"Expected return code 0, got {returncode}"
        assert stdout == "", f"Expected empty output, got: {stdout}"
        assert stderr == "", f"Expected no stderr, got: {stderr}"
        print("✓ Test 4 passed: Successfully handled empty file")
    finally:
        os.unlink(temp_file)


def test_multiple_lines():
    """Test reading a file with multiple lines"""
    print("\n[Test 5] Reading file with multiple lines...")
    stdout, stderr, returncode = run_ccat(['test.txt'])
    lines = stdout.strip().split('\n')
    assert len(lines) >= 10, f"Expected at least 10 lines, got {len(lines)}"
    print(f"✓ Test 5 passed: Read {len(lines)} lines correctly")


def test_second_test_file():
    """Test reading test2.txt if it exists"""
    print("\n[Test 6] Reading second test file (test2.txt)...")
    if os.path.exists('test2.txt'):
        stdout, stderr, returncode = run_ccat(['test2.txt'])
        assert returncode == 0, f"Expected return code 0, got {returncode}"
        assert len(stdout) > 0, "Expected output from test2.txt"
        print("✓ Test 6 passed: Successfully read test2.txt")
    else:
        print("⊘ Test 6 skipped: test2.txt not found")


def test_multiple_files():
    """Test concatenating multiple files"""
    print("\n[Test 7] Concatenating multiple files...")

    # First, get individual file contents
    stdout1, _, returncode1 = run_ccat(['test.txt'])
    stdout2, _, returncode2 = run_ccat(['test2.txt'])

    assert returncode1 == 0 and returncode2 == 0, "Could not read individual files"

    # Now test concatenation
    stdout, stderr, returncode = run_ccat(['test.txt', 'test2.txt'])

    assert returncode == 0, f"Expected return code 0, got {returncode}"
    assert stderr == "", f"Expected no stderr, got: {stderr}"

    # Verify output contains both files' content
    expected_output = stdout1 + stdout2
    assert stdout == expected_output, "Concatenated output doesn't match expected"

    # Verify content from both files is present
    assert "ocean" in stdout, "Expected content from test.txt"
    assert len(stdout) > len(stdout1), "Expected output longer than single file"

    print("✓ Test 7 passed: Successfully concatenated multiple files")


if __name__ == '__main__':
    print("=" * 50)
    print("Testing ccat")
    print("=" * 50)

    try:
        test_read_valid_file()
        test_nonexistent_file()
        test_read_from_stdin()
        test_empty_file()
        test_multiple_lines()
        test_second_test_file()
        test_multiple_files()

        print("\n" + "=" * 50)
        print("✓ All tests passed!")
        print("=" * 50)
    except AssertionError as e:
        print(f"\n✗ Test failed: {e}")
        exit(1)
    except Exception as e:
        print(f"\n✗ Error: {e}")
        exit(1)
