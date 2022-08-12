puzzle_input = open('input.txt', 'r')

Lines = puzzle_input.readlines()

has_two_pairs = False # has two instances of the same pair, like "xcxc" or "xcbjxc" not including "zzz" (zz and zz  overlapped)
has_sandwich = False # Sandwich being instances like "aba" or "qfq"

nice_string_count = 0


for line in Lines:
    
    last_letter = "1"
    second_last_letter = "1"

    for i in range(0, len(line)):

        if second_last_letter == line[i]:
            has_sandwich = True


        if i < len(line):
            try:      
                x = line.index(last_letter + line[i])
                if i - x > 2:
                    has_two_pairs = True
                    print("String " + line.strip() + " repeats " + last_letter + line[i])
            except ValueError:
                pass
            

        second_last_letter = last_letter
        last_letter = line[i]

    if has_two_pairs and has_sandwich:
        nice_string_count += 1

    has_two_pairs = False
    has_sandwich = False

    print(nice_string_count)