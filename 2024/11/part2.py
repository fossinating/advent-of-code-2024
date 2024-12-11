from util import Memoize


solution_answer = 55312

def process_input(input: list[str]) -> int:
    real_input = input[0]

    numbers = real_input.split()

    total_score = 0
    for number in numbers:
        total_score += score(number)
    
    return total_score


scores = {}
def memoed_score(number: str, steps=25) -> int:
    if number == "0":
        return 1
    if (number, steps) not in scores:
        scores[(number, steps)] = score(number, steps)
        print((number, steps), scores[(number, steps)])
    return scores[(number, steps)]
    
#@Memoize
def score(number: str, steps=75) -> int:
    if steps <= 0:
        return 1
    if number == "0":
        return score("1", steps - 1)
    elif len(number) % 2 == 0:
        return score(f"{int(number[:(int(len(number)/2))])}", steps - 1) + score(f"{int(number[(int(len(number)/2)):])}", steps - 1)
    else:
        return score(f"{int(number)*2024}", steps - 1)
    
    

if __name__ == "__main__":
    #sample_answer = None
    #with open("sample_input.txt", "r") as input_file:
    #    sample_answer = process_input([line.strip() for line in input_file.readlines()])
    #    print(f"Solution to sample: `{sample_answer}` (expected `{solution_answer}`)")
    
    #if sample_answer == solution_answer:
    with open("input.txt", "r") as input_file:
        solution = process_input([line.strip() for line in input_file.readlines()])
        print(f"Solution to puzzle: {solution}")