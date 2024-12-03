solution_answer = "11"

def process_input(inputs: list[str]) -> str:
    left_list: list[int] = []
    right_list: list[int] = []

    for line in inputs:
        split_input = line.split("   ")
        left_list.append(int(split_input[0]))
        right_list.append(int(split_input[1]))
    
    left_list.sort()
    right_list.sort()

    distance = 0

    for i in range(len(left_list)):
        distance += abs(left_list[i] - right_list[i])

    return str(distance)
    

if __name__ == "__main__":
    sample_answer = ""
    with open("sample_input.txt", "r") as input_file:
        sample_answer = process_input(input_file.readlines())
        print(f"Solution to sample: `{sample_answer}` (expected `{solution_answer}`)")
    
    if sample_answer == solution_answer:
        with open("input.txt", "r") as input_file:
            print(f"Solution to puzzle: {process_input(input_file.readlines())}")