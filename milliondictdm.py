aliens=[]
for alien_num in range(10000000):
    new_alien={}
    new_alien['color']='green'
    new_alien['points']=5
    new_alien['x']=20*alien_num
    new_alien['y']=0
    aliens.append(new_alien)

num_aliens=len(aliens)
print("Number of aliens created:"+str(num_aliens))