from random import choice

import art
import game_data

print(art.logo)
continue_game = True

compare_a = choice(game_data.data)
score = 0

while continue_game:
    print(f"Compare A: {compare_a.get('name')}, a {compare_a.get('description')}, from {compare_a.get('country')}")
    print(art.vs)
    compare_b = choice(game_data.data)
    print(f"Compare B: {compare_b.get('name')}, a {compare_b.get('description')}, from {compare_b.get('country')}")
    answer = input("Who was more followers? Type 'A' or 'B': ")
    if answer == 'A' and compare_a.get('follower_count') > compare_b.get('follower_count'):
        score += 1
        print(f"You are right! Current score {score}")
        compare_b = compare_a
    elif answer == 'B' and compare_b.get('follower_count') > compare_a.get('follower_count'):
        score += 1
        print(f"You are right! Current score {score}")
        compare_b = compare_a
    else:
        print(f"You lose! Current score {score}")
        continue_game = False
