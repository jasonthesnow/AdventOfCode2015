from itertools import combinations_with_replacement

puzzle_input = "input.txt"

ingredients = list()

ounces = dict()

teaspoons = 100
calories = 500

max_cookie_score = 0

capacity = dict()
durability = dict()
flavor = dict()
texture = dict()
calories = dict()

with open(puzzle_input) as f:
    for line in f:
        word = line.split()
        ingredients.append(word[0])
        ounces[word[0]] = 0
        capacity[word[0]] = int(word[2].strip(','))
        durability[word[0]] = int(word[4].strip(','))
        flavor[word[0]] = int(word[6].strip(','))
        texture[word[0]] = int(word[8].strip(','))
        calories[word[0]] = int(word[10].strip(','))



print(ingredients)
print(f'Capacity: {capacity}')
print(f'Durability: {durability}')
print(f'Flavor: {flavor}')
print(f'Texture: {texture}')
print(f'Calories: {calories}')

next_perm = combinations_with_replacement(ingredients, teaspoons)

for i in next_perm:
    current_cookie_score = 0
    capacity_total = 0
    durability_total = 0
    flavor_total = 0
    texture_total = 0
    calories_total = 0
    
    for j in range(len(ingredients)):
        ounces[ingredients[j]] = 0;
    
    for j in range(teaspoons):
        ounces[i[j]] += 1

    for j in range(len(ingredients)):
        capacity_total += (capacity[ingredients[j]] * ounces[ingredients[j]])
        durability_total += (durability[ingredients[j]] * ounces[ingredients[j]])
        flavor_total += (flavor[ingredients[j]] * ounces[ingredients[j]])
        texture_total += (texture[ingredients[j]] * ounces[ingredients[j]])
        calories_total += (calories[ingredients[j]] * ounces[ingredients[j]])

    if not (calories_total == 500):
        continue

    current_cookie_score = (max(0,capacity_total) * max(0,durability_total) * max(0,flavor_total) * max(0,texture_total))

    #print(ounces)
    #print(f'Capacity Total: {capacity_total}')
    #print(f'Durability Total: {durability_total}')
    #print(f'Flavor Total: {flavor_total}')
    #print(f'Texture Total:{texture_total}')
    #print(f'Total Cookie Score: {current_cookie_score}')

    max_cookie_score = max(max_cookie_score, current_cookie_score)
    #print(f'Max Cookie So far: {max_cookie_score}')
    #print("")

print(f'Max Cookie Total: {max_cookie_score}')


        

