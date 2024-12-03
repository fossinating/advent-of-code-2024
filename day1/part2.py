solution_answer = "31"

def process_input(inputs: list[str]) -> str:
    left_list: list[str] = []
    right_count: map = {}

    for line in inputs:
        split_input = line.split("   ")
        left_list.append(split_input[0])
        right_count[split_input[1].strip()] = right_count.get(split_input[1].strip(), 0) + 1

    value = 0

    for item in left_list:
        value += int(item) * right_count.get(item, 0)

    return str(value)
    

if __name__ == "__main__":
    sample_answer = ""
    with open("sample_input.txt", "r") as input_file:
        sample_answer = process_input(input_file.readlines())
        print(f"Solution to sample: `{sample_answer}` (expected `{solution_answer}`)")
    
    if sample_answer == solution_answer:
        with open("input.txt", "r") as input_file:
            print(f"Solution to puzzle: {process_input(input_file.readlines())}")