fav_languages={
    'jen':['python','ruby'],
    'sarah':['C'],
    'edward':['ruby','go'],
    'phil':['python','haskell']
}

for name,langs in fav_languages.items():
    print("\n"+name+": ",end="")
    for lang in langs:
        print(lang+" ",end="")