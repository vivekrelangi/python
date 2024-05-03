users=[]

new_user={
    'last':'fermi',
    'first':'enrico',
    'username':'efermi'
}
users.append(new_user)
print(users)

new_user={
    'last':'curie',
    'first':'marie',
    'username':'mcurie'
}
users.append(new_user)
print(users)

for user_dict in users:
    for k,v in user_dict.items():
        print(k+": "+v)
    print("\n")

users=[
    {
    'last':'fermi',
    'first':'enrico',
    'username':'efermi'
    },
    {
    'last':'curie',
    'first':'marie',
    'username':'mcurie'
    }
]

for user_dict in users:
    for k,v in user_dict.items():
        print(k+": "+v)
    print("\n")