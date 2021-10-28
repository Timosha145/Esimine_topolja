print('Tere, see on väga keeruline ülesanne!!!')
print()
v=''
while type(v)!=int or v not in[1,0]:
  try:
    v=int(input('kas teate kuidas big mac burgeri kastme teha? (1-jah, 0-ei)'))
  except ValueError:
    print('palun kirjuta ainult "1" või "0"!')
if v==0:
  v2=''
  while type(v2)!=int or v2 not in[1,0]:
    try:
       v2=int(input('kas soovite teade kuidas seda teha? (1-jah, 0-ei)'))
    except ValueError:
      print('palun kirjuta ainult "1" või "0"!')
  if v2==1:
    print('sul on vaja:')
    print('1/2 klaasi majoneesi')
    print('4 tl marineeritud kurgi salatit')
    print('1/8 tl soola')
    print('2 spl Prantsuse kastet')
    print('1 spl väga peeneks hakitud sibulat')
    print('1 tl suhkrut')
    print('Soovitan segada kõik koostisosad kausis kokku ning jätta kauss ööseks kaetuna külmkappi. Vahepeal tuleks segu paar korda läbi segada.')
  if v2==0:
    print('ei taha kui taha')
if v==1:
  print('väga tore')
v3=''
while type(v3)!=int or v3 not in[1,0]:
  try:
    v3=int(input('kas tahad viktorini kuidas big mac burgeri kastme teha? (1-jah, 0-ei)'))
  except ValueError:
    print('palun kirjuta ainult "1" või "0"!')
if v3==0:
  print('ei taha kui taha!')
elif v3==1:
  h=0
  b=''
  while type(b)!=int or b not in[1,0]:
    try:
      b=int(input('Kui palju majoneezi on vaja? (1-1 klaasi, 0-1/2 klaasi)'))
    except ValueError:
      print('palun kirjuta ainult "1" või "0"!')
  if b==0:
    h=h+1
  b1=''
  while type(b1)!=int or b1 not in[2,1,0]:    
    try:
      b1=int(input('Kui palju soola on vaja?) (2-1tl, 1-1/8tl, 0-3/8tl)'))
    except ValueError:
      print('palun kirjuta ainult "2" või "1" või "0"!')
  if b1==1:
    h=h+1
  b2=''
  while type(b2)!=int or b2 not in[1,0]:
    try:
      b2=int(input('Kas ketsup on vaja? (1-jah, 0-ei)'))
    except ValueError:
      print('palun kirjuta ainult "1" või "0"!')
  if b2==0:
    h=h+1
  b3=''
  while type(b3)!=int or b3 not in[1,0]:
    try:
      b3=int(input('Milline sibul on vaja? (1-hakkitud, 0-praetud)'))
    except ValueError:
      print('palun kirjuta ainult "1" või "0"!')
  if b3==1:
    h=h+1
  print('Viimane küsimus!')
  b4=''
  while type(b4)!=int or b4 not in[2,1,0]:
    try:
      b4=int(input('Mis on viimane etapp? (2-ööseks külmkappi panna, 1-segada paar korda, 0-suhkru panna)'))
    except ValueError:
      print('palun kirjuta ainult "2" või "1" või "0"!')
  if b4==1:
    h=h+1
  print(f"Sinu hinne on {h}!")

            
