import re

solution_answer = 48

def process_input(input: str) -> int:
    do = True
    total = 0
    for match in re.findall(r'(mul)\(([0-9]+),([0-9]+)\)|(don\'t)\(\)|(do)\(\)', input):
        print(match)
        if match[4] == "do":
            do = True
        elif match[3] == "don't":
            do = False
        elif do and match[0] == "mul":
            total += int(match[1])*int(match[2])

    return total
    
    

if __name__ == "__main__":
    sample_answer = ""
    with open("part2_sample_input.txt", "r") as input_file:
        sample_answer = process_input(input_file.read())
        print(f"Solution to sample: `{sample_answer}` (expected `{solution_answer}`)")
    
    if sample_answer == solution_answer:
        with open("input.txt", "r") as input_file:
            print(f"Solution to puzzle: {process_input(input_file.read())}")