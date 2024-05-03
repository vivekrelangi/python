banned_users=['ann','chad','doe']
user='erin'
if user not in banned_users:
    print("You can play!")

players=[]
if players:
    for player in players:
        print("Player:"+player.title())
else:
    print("We have no players yet!")
