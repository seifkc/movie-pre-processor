"""Clean movie description text files and write the parsed output."""

import argparse
from pathlib import Path

import text_parsing_functions as tpf


DEFAULT_NAME_SET = {
    'suan',
    'seongkyeong',
    'yonsuk',
    'seokwoo',
    'ingil',
    'yonghuk',
    'jinhee',
}


def read_cleaned_lines(filepath, stopwords, names, replacement='person'):
    """Read a text file line by line, clean each line, and return the results."""
    cleaned_lines = []
    with open(filepath, 'r', encoding='utf-8') as file:
        for line in file:
            cleaned_line = tpf.line_cleaning_pipeline(
                line,
                stopwords,
                names,
                replacement,
            )
            cleaned_lines.append(cleaned_line)
    return cleaned_lines


def write_lines_to_file(filepath, lines):
    """Write a list of cleaned lines to a text file, one line per element."""
    output_path = Path(filepath)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with output_path.open('w', encoding='utf-8') as file:
        if lines:
            file.write('\n'.join(lines))
            file.write('\n')


def parse_args():
    """Parse command-line arguments for input and output file paths."""
    parser = argparse.ArgumentParser(
        description='Clean a movie description text file.'
    )
    parser.add_argument('-i', '--input', required=True, help='Input text file to parse')
    parser.add_argument('-o', '--output', required=True, help='Output file for cleaned text')
    return parser.parse_args()


def main():
    """Run the description cleaning pipeline from the command line."""
    args = parse_args()
    project_root = Path(__file__).resolve().parent.parent

    input_path = Path(args.input)
    if not input_path.is_absolute():
        input_path = project_root / input_path

    output_path = Path(args.output)
    if not output_path.is_absolute():
        output_path = project_root / output_path

    stopwords = tpf.load_stopwords(project_root / 'data' / 'stopwords.txt')
    cleaned_lines = read_cleaned_lines(input_path, stopwords, DEFAULT_NAME_SET)
    write_lines_to_file(output_path, cleaned_lines)

    print(f'Parsed {input_path} -> {output_path}')


if __name__ == '__main__':
    main()

