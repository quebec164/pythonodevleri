avukat = 0
polis = 0
sporcu = 0
doktor = 0
muhendis = 0
sanatcı = 0

isim = input('isminiz nedir?')
print('hosgeldin ,', isim)
print('lütfen sorulara E veya H olarak yanıt verin')

soru1=input('Silahlara ilginiz var mıdır? \n E/H')
if soru1 == 'E':
      polis+=1
      print('sıradaki soru')
else:
      print('sıradaki soru')

soru2=input('Hakkınızı savunmayı sever misiniz? \n E/H')
if soru2 == 'E':
      avukat+=1
      print('sıradaki soru')
else:
      print('sıradaki soru')

soru3=input('fiziksel aktiviteleri sever misiniz? \n E/H')
if soru3 == 'E':
      sporcu+=1
      print('sıradaki soru')
else:
      print('sıradaki soru')

soru4=input('Hastalıklar ilginizi ceker mi? \n E/H')
if soru4 == 'E':
      doktor+=1
      print('sıradaki soru')
else:
      print('sıradaki soru')

soru5=input('teknik seylerle ugrasmaktan keyif alır mısınız? \n E/H')
if soru5 == 'E':
      muhendis+=1
      print('sıradaki soru')
else:
      print('sıradaki soru')

soru6=input('sanata ilginiz var mı? \n E/H')

if avukat >= 1 :
    print("avuktaklığa ilginiz var")
if polis >= 1 :
    print("polisliğe ilginiz var")
if sporcu >= 1 :
    print("sporculuğa ilginiz var")
if doktor >= 1 :
    print("doktorluğa ilginiz var")
if muhendis >= 1 :
    print("muhendisliğe ilginiz var")
if sanatcı >= 1 :
    print("sanatçılığa ilginiz var")

