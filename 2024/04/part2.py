solution_answer = 9

def process_input(input: list[str]) -> int:
    count = 0
    for r in range(len(input)):
        for c in range(len(input[r])):
            if input[r][c] == "A":
                matches = 0
                for direction in [(1, 1), (-1, 1), (1, -1), (-1, -1)]:
                    proper = True
                    letters = "MAS"
                    for i in range(len(letters)):
                        i -= 1
                        if (r + i*direction[0] >= 0 and r + i*direction[0] < len(input)) \
                            and (c + i*direction[1] >= 0 and c + i*direction[1] < len(input[r+i*direction[0]])) \
                            and input[r+i*direction[0]][c+i*direction[1]] == letters[i+1]:
                            print(input[r+i*direction[0]][c+i*direction[1]], r+i*direction[0], c+i*direction[1])
                        else:
                            proper = False
                            #print(r, c, i, direction, "fail")
                            break
                    if proper:
                        #print(r, c, direction)
                        matches += 1
                if matches == 2:
                    count += 1
                    
    
    return count
    
    

if __name__ == "__main__":
    sample_answer = ""
    with open("sample_input.txt", "r") as input_file:
        sample_answer = process_input([line.strip() for line in input_file.readlines()])
        print(f"Solution to sample: `{sample_answer}` (expected `{solution_answer}`)")
    
    if sample_answer == solution_answer:
        with open("input.txt", "r") as input_file:
            print(f"Solution to puzzle: {process_input([line.strip() for line in input_file.readlines()])}")