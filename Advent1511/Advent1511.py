# Things the password Requires

# abc, bcd, cde, def..
# cannot contain i, o, or l
# must have two pairs of letters that do not overlap (aaa doesn't count, but aaaa would)

password = ['h','x','b','x','x','y','z','z']
safe_letters = "abcdefghjkmnpqrstuvwxyz"
counted_up = False

bad_password = True

has_triple_run = False
has_double_pair = False

while True:
    has_triple_run = False
    has_double_pair = False
    #Count Up Letters

    counted_up = False
    for i in range(len(password) - 1, -1, -1):
        if counted_up:
            break
        for j in range(len(safe_letters)):
            if password[i] == safe_letters[j]:
                try:
                    password[i] = safe_letters[j + 1]
                    counted_up = True
                    break
                except IndexError:
                    password[i] = safe_letters[0]
    
    password_string = "".join(password)
    # print(password_string)

    #Test if password is good

    for i in range(len(safe_letters) - 2):
        if safe_letters[i:i+3] in password_string:
            has_triple_run = True
            break
    
    index = list()
    for i in range(len(safe_letters)):
        for j in range(len(password)):
            try:
                if safe_letters[i] == password[j] and safe_letters[i] == password[j+1]:
                    index.append(i)
            except IndexError:
                pass
        
    if len(index) > 1:
        if index[1] - index[0] > 1:
            has_double_pair = True

    
    if has_triple_run and has_double_pair:
        break

print(password_string)