solution_answer = 11387

def process_input(input: list[str]) -> int:
    value = 0

    for line in input:
        answer = int(line.split(": ")[0])
        numbers = [int(bit) for bit in line.split(": ")[1].split(" ")]

        if foo(answer, numbers[0], numbers[1:]):
            value += answer

    return value
            
def foo(goal: int, total: int, remaining: int) -> bool:
    if len(remaining) == 1:
        return total + remaining[0] == goal or total * remaining[0] == goal or int(f"{total}{remaining[0]}") == goal
    else:
        return foo(goal, total*remaining[0], remaining[1:]) or foo(goal, total+remaining[0], remaining[1:]) or foo(goal, int(f"{total}{remaining[0]}"), remaining[1:])

    
if __name__ == "__main__":
    sample_answer = ""
    with open("sample_input.txt", "r") as input_file:
        sample_answer = process_input([line.strip() for line in input_file.readlines()])
        print(f"Solution to sample: `{sample_answer}` (expected `{solution_answer}`)")
    
    if sample_answer == solution_answer:
        with open("input.txt", "r") as input_file:
            print(f"Solution to puzzle: {process_input([line.strip() for line in input_file.readlines()])}")