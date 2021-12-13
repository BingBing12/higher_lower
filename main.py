import random 
from art import logo, vs
from data import data


def play():
    print(logo)
    score = 0
    game_over=False
    while not game_over:
        influencer_one=random.choice(data)
        influencer_two=random.choice(data)
        while(influencer_one["name"] ==influencer_two["name"]):
            influencer_two=random.choice(data)
        print(f"\n{influencer_one['name']}, a {influencer_one['description']} from {influencer_one['country']}")
        print(vs)
        print(f"{influencer_two['name']}, a {influencer_two['description']} from {influencer_two['country']} \n")

        choice = input(f"guess {influencer_one['name']} 'a' or {influencer_two['name']} 'b'").lower()
        if(choice=='a' and influencer_one["follower_count"]>influencer_two["follower_count"]):
            score +=1
            print(f"{influencer_one['name']} is correct, your score is {score}")
        elif(choice=='b' and influencer_two["follower_count"]>influencer_one["follower_count"]):
            score +=1
            print(f"{influencer_two['name']} is correct, your score is {score}")
        else:
            print(f"you lost, your final score is {score}")
            game_over=True
while(input("type 'y' to play high low or 'n' to exit")=="y"):
    play()
print("Goodbye")
