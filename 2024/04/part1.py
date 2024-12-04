solution_answer = 18

def process_input(input: list[str]) -> int:
    count = 0
    for r in range(len(input)):
        for c in range(len(input[r])):
            if input[r][c] == "X":
                #print(r, c)
                for direction in [(1, 0), (1, 1), (0, 1), (-1, 0), (-1, -1), (-1, 1), (1, -1), (0, -1)]:
                    proper = True
                    letters = "XMAS"
                    for i in range(len(letters)):
                        if (r + i*direction[0] >= 0 and r + i*direction[0] < len(input)) \
                            and (c + i*direction[1] >= 0 and c + i*direction[1] < len(input[r+i*direction[0]])) \
                            and input[r+i*direction[0]][c+i*direction[1]] == letters[i]:
                            pass#print(input[r+i*direction[0]][c+i*direction[1]], r+i*direction[0], c+i*direction[1])
                        else:
                            proper = False
                            #print(r, c, i, direction, "fail")
                            break
                    if proper:
                        #print(r, c, direction)
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