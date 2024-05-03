banned_users=['eve','fred','gray','helen']

prompt="\nAdd a player to your team."
prompt+="\nEnter 'quit when you're done."

players =[]
while True:
    player=input(prompt)
    if player == 'quit':
        break
    elif player in banned_users:
        print(player+" is banned!")
        continue
    else:
        players.append(player)

print("\nYor team:")
for player in players:
    print(player)