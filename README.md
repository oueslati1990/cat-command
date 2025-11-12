# ccat - Python Cat Command Implementation

A Python implementation of the Unix `cat` command, built as part of the [Coding Challenges](https://codingchallenges.fyi/challenges/challenge-cat/) series.

## About

This project implements a command-line utility that reads files sequentially and writes them to standard output, mimicking the behavior of the Unix `cat` command. The tool handles both file input and stdin, with support for multiple files and various formatting options.

## Challenge Progress

Following the [Build Your Own cat Tool](https://codingchallenges.fyi/challenges/challenge-cat/) challenge:

- ✅ **Step 0**: Setup project structure
- ✅ **Step 1**: Basic file reading - read and output a single file
- ✅ **Step 2**: Standard input - read from stdin when no file is provided
- ✅ **Step 3**: Multiple files - concatenate multiple files to output
- ⬜ **Step 4**: Line numbering - implement `-n` flag to number all lines
- ⬜ **Step 5**: Selective numbering - implement `-b` flag to number non-blank lines

## Features

### Currently Implemented

- Read and display contents of single or multiple files
- Read from standard input when no files are specified
- Binary mode reading (preserves all file encodings)
- Proper error handling for:
  - Non-existent files
  - Permission errors
  - I/O errors
- Unix-style error messages

### Upcoming Features

- `-n` flag: Number all output lines
- `-b` flag: Number only non-blank lines

## Installation

### Development Installation

```bash
# Clone the repository
cd cat-command

# Install in development mode
pip install -e .
```

This will make the `ccat` command available in your terminal.

### Requirements

- Python >= 3.7
- No external dependencies (uses only standard library)

## Usage

### Basic Usage

```bash
# Display a single file
ccat test.txt

# Concatenate multiple files
ccat test.txt test2.txt

# Read from stdin
echo "Hello World" | ccat
head -n1 test.txt | ccat
```

### Examples

```bash
# Output file content
ccat test.txt

# Chain multiple files
ccat file1.txt file2.txt file3.txt

# Use with pipes
cat somefile.txt | ccat
```

## Testing

The project includes a comprehensive test suite:

```bash
# Run all tests
python test_ccat.py
```

### Test Coverage

- ✓ Reading valid files
- ✓ Handling non-existent files
- ✓ Reading from stdin
- ✓ Empty file handling
- ✓ Multiple line files
- ✓ Multiple file concatenation

## Project Structure

```
cat-command/
├── ccat.py              # Main implementation
├── test_ccat.py         # Test suite
├── pyproject.toml       # Package configuration
├── README.md            # Documentation
├── LICENSE              # MIT License
├── test.txt             # Test data file
└── test2.txt            # Test data file
```

## Implementation Details

- **Binary Mode**: Files are read in binary mode (`rb`) to handle all encodings correctly
- **Argument Parsing**: Uses `argparse` for command-line argument handling
- **Error Handling**: Comprehensive exception handling with informative error messages
- **Testing**: Subprocess-based testing to verify actual CLI behavior

## Author

Mohamed Oueslati

## License

MIT License - See LICENSE file for details

## Resources

- [Coding Challenges - Build Your Own cat](https://codingchallenges.fyi/challenges/challenge-cat/)
- [Unix cat command manual](https://man7.org/linux/man-pages/man1/cat.1.html)