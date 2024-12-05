solution_answer = 143

def process_input(input: list[str]) -> int:
    reading_rules = True
    value = 0

    rules = {}
    for line in input:
        if reading_rules:
            if len(line) == 0:
                reading_rules = False
                continue

            rules[line.split("|")[0]] = [*rules.get(line.split("|")[0], []), line.split("|")[1]]
        else:
            pages = []
            valid = True
            for page in line.split(","):
                for rule in rules.get(page, []):
                    if rule in pages:
                        valid = False
                        break
                if not valid:
                    break
                pages.append(page)
            
            if valid:
                value += int(pages[int(len(pages)/2)])
    return value


    

if __name__ == "__main__":
    sample_answer = ""
    with open("sample_input.txt", "r") as input_file:
        sample_answer = process_input([line.strip() for line in input_file.readlines()])
        print(f"Solution to sample: `{sample_answer}` (expected `{solution_answer}`)")
    
    if sample_answer == solution_answer:
        with open("input.txt", "r") as input_file:
            print(f"Solution to puzzle: {process_input([line.strip() for line in input_file.readlines()])}")