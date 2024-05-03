tel = {'jack':4098,'sape':4139}
print(tel)
tel['guido']=4127
print(tel)
print(tel['jack'])
del tel['sape']
print(tel)
tel['irv']=4127
print(tel)
print(tel.keys())
a='guido' in tel
print(a)
alien={'color':'green','points':5}
print("The alien's color is "+alien['color'])
alien['x_position']=0
print(alien)
fav_numbers={'eric':17,'ever':4}
for name in fav_numbers.keys():
    print(name+" loves "+str(fav_numbers[name]))
for name, number in fav_numbers.items():
    a=str(number)
    print(a+ " is favorite number of "+name)

alien_0 = {'color':'green','points':5}
print(alien_0)
print(alien_0['color'])
print(alien_0['points'])

alien_0={'color':'green'}
print(alien_0)
alien_color=alien_0.get('color')
alien_points=alien_0.get('points',0)

print(alien_color)
print(alien_points)

alien_0 = {'color':'green','points':5}

print(alien_0)
alien_0['x']=0
alien_0['y']=25
alien_0['speed']=1.5
print(alien_0)

alien_0={}
alien_0['color']='green'
alien_0['points']=5
print(alien_0)

alien_0['color']='yellow'
alien_0['points']=10
print(alien_0)

alien_0={}
alien_0['color']='green'
alien_0['points']=5
print(alien_0)

del alien_0['points']
print(alien_0)

fav_languages ={
    'jen' : 'python',
    'sarah' : 'c',
    'edward':'ruby',
    'phil':'python'
}

for name, language in fav_languages.items():
    print(name+":"+language)

for name in fav_languages.keys():
    print(name)

for language in fav_languages.values():
    print(language)

for name in sorted(fav_languages.keys()):
    print(name+":"+language)

num_responses=len(fav_languages)
print(num_responses)