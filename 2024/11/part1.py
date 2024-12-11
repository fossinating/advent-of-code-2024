solution_answer = 55312

def process_input(input: list[str]) -> int:
    real_input = input[0]

    numbers = real_input.split()

    for i in range(25):

        new_numbers = []

        for number in numbers:
            if number == "0":
                new_numbers.append("1")
            elif len(number) % 2 == 0:
                new_numbers.append(f"{int(number[:(int(len(number)/2))])}")
                new_numbers.append(f"{int(number[(int(len(number)/2)):])}")
            else:
                new_numbers.append(f"{int(number)*2024}")
        numbers = new_numbers
    
    return len(numbers)
  
    

if __name__ == "__main__":
    sample_answer = ""
    with open("sample_input.txt", "r") as input_file:
        sample_answer = process_input([line.strip() for line in input_file.readlines()])
        print(f"Solution to sample: `{sample_answer}` (expected `{solution_answer}`)")
    
    if sample_answer == solution_answer:
        with open("input.txt", "r") as input_file:
            solution = process_input([line.strip() for line in input_file.readlines()])
            print(f"Solution to puzzle: {solution}")