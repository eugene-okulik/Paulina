import argparse
import os
import re
import json


def parse_args():
    parser = argparse.ArgumentParser(description='Log Analyzer Tool')
    parser.add_argument('directory', type=str, help='Directory containing log files')
    parser.add_argument('--text', type=str, help='Text to search in log files')
    return parser.parse_args()


def extract_json_and_prefix(line):
    match = re.search(r'({.*})', line)
    if match:
        json_part = match.group(1)
        prefix = line[:match.start()].strip()
        return prefix, json_part
    return line, None


def process_json(json_part, search_text):
    try:
        data = json.loads(json_part)
        flat_data = ' '.join(flatten_json(data))
        words = flat_data.split()
        if search_text in words:
            index = words.index(search_text)
            start = max(0, index - 5)
            end = min(len(words), index + 6)
            context = ' '.join(words[start:end])
            return context
    except json.JSONDecodeError as e:
        print(f"Error reading JSON data: {e}")

    return None


def flatten_json(y):
    out = []

    def flatten(x):
        if type(x) is dict:
            for a in x:
                flatten(x[a])
        elif type(x) is list:
            for a in x:
                flatten(a)
        else:
            out.append(str(x))

    flatten(y)
    return out


def print_context(line_number, line, search_text):
    prefix, json_part = extract_json_and_prefix(line)
    if json_part:
        context = process_json(json_part, search_text)
        if context:
            print(f"Found at line {line_number}: {prefix} ... {context}")
    else:
        pass


def main():
    args = parse_args()
    directory = args.directory
    search_text = args.text

    if not os.path.isdir(directory):
        print("The specified directory does not exist.")
        return

    for filename in os.listdir(directory):
        if filename.endswith('.log'):
            full_path = os.path.join(directory, filename)
            print(f"Searching in file: {filename}")
            try:
                with open(full_path, 'r', encoding='utf-8', errors='ignore') as file:
                    for line_number, line in enumerate(file, 1):
                        print_context(line_number, line, search_text)
            except Exception as e:
                print(f"Error reading file {filename}: {e}")


if __name__ == '__main__':
    main()
# C:\Users\Paulina\Documents\first_repository\Paulina\homework\eugene_okulik\data\logs --text 69.907289405
# C:\Users\Paulina\Documents\first_repository\Paulina\homework\eugene_okulik\data\logs --text Polygon
