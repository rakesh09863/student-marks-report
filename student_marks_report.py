while(True):
    a=int(input('enter the value:'))
    if a<=0:
        print('invalid try again')
    else:
        break
while(True):
    name=input('enter the name:')
    if len(name)==0:
        print('don`t enter space try again')
    else:
        words=name.split()
        res='valid'
        for i in words:
            if not i.isalpha():
                res='invalid'
        if res=='invalid':
            print('{} is {}'.format(name,res))
        elif res=='valid':
            print('{} is {}'.format(name,res))
            break
while(True):
    cm=int(input('enter marks of cm:'))
    if cm<=0 or cm>100:
        print('invalid try again')
    else:
        break
while(True):
    cppm=int(input('enter marks of cm:'))
    if cppm<=0 or cppm>100:
        print('invalid try again')
    else:
        break
while(True):
    osm=int(input('enter marks of cm:'))
    if osm<=0 or osm>100:
        print('invalid try again')
    else:
        break
#total marks
total=cm+cppm+osm
#percentage
percent=(total/300)*100
#grade
if cm<40 or cppm<40 or osm<40:
    grade='Fail'
elif total in range(250,301):
    grade ='Distinction'
elif total in range(200,250):
     grade='First'
elif total in range(150,200):
     grade='Second'
elif total in range(120,150):
     grade='Third'
print('student number={}'.format(a))
print('student name={}'.format(name))
print('marks in cm ={}'.format(cm))
print('marks in cppm ={}'.format(cppm))
print('marks in osm ={}'.format(osm))
print('total marks={}'.format(total))
print('percentage={}'.format(percent))
print('grade={}'.format(grade))
