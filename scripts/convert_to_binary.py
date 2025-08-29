import json
import sys

def to_binary(word: str) -> str:
    return ' '.join(format(ord(c), '08b') for c in word)

def convert_json(input_json):
    output_json = {}
    for key, value in input_json.items():
        if isinstance(value, str):
            output_json[key] = {"word": value, "binary": to_binary(value)}
        elif isinstance(value, list):
            output_json[key] = [{"word": v, "binary": to_binary(v)} for v in value]
        else:
            output_json[key] = value
    return output_json

if __name__ == "__main__":
    data = json.load(sys.stdin)
    print(json.dumps(convert_json(data), indent=2))
