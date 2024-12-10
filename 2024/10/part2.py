import copy


solution_answer = 81

def process_input(input: list[str]) -> int:
    total_score = 0
    for r in range(len(input)):
        for c in range(len(input[r])):
            if input[r][c] == "0":
                total_score += score_trailhead(r, c, input)


    return total_score

                
    
def score_trailhead(r, c, input):
    return score_path(r, c, copy.deepcopy(input))

def score_path(r, c, input):
    if input[r][c] == "9":
        input[r][c] = "."
        return 1
    score = 0
    for [i, j] in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
        if r + i < 0 or r + i >= len(input) or c + j < 0 or c + j >= len(input[r+i]):
            continue
        if i == 0 and j == 0:
            continue
        if input[r+i][c+j] == ".":
            continue
        if int(input[r+i][c+j]) == int(input[r][c]) + 1:
            score += score_path(r+i, c+j, copy.deepcopy(input))
    return score


if __name__ == "__main__":
    sample_answer = ""
    with open("sample_input.txt", "r") as input_file:
        sample_answer = process_input([list(line.strip()) for line in input_file.readlines()])
        print(f"Solution to sample: `{sample_answer}` (expected `{solution_answer}`)")
    
    if sample_answer == solution_answer:
        with open("input.txt", "r") as input_file:
            print(f"Solution to puzzle: {process_input([list(line.strip()) for line in input_file.readlines()])}")