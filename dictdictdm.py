users={
    'aeinstein':{
        'first':'albert',
        'last':'einstein',
        'location':'princeton'
    },
    'mcurie':{
        'first':'marie',
        'last':'curie',
        'location':'paris'
    }
}

for un,dt in users.items():
    print("Username:"+un)
    for k,v in dt.items():
        print(k+":"+v)
        print("\n")

for username, user_dict in users.items():
    print("\nUsername: "+username)
    full_name=user_dict['first']+" "+user_dict['last']
    location=user_dict['location']

    print("\tFull name: "+full_name.title())
    print("\tLocation: "+location.title())