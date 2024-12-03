import re

solution_answer = 161

def process_input(input: str) -> int:
    total = 0
    for match in re.findall(r'mul\(([0-9]+),([0-9]+)\)', input):
        total += int(match[0])*int(match[1])

    return total
    
    

if __name__ == "__main__":
    sample_answer = ""
    with open("sample_input.txt", "r") as input_file:
        sample_answer = process_input(input_file.read())
        print(f"Solution to sample: `{sample_answer}` (expected `{solution_answer}`)")
    
    if sample_answer == solution_answer:
        with open("input.txt", "r") as input_file:
            print(f"Solution to puzzle: {process_input(input_file.read())}")