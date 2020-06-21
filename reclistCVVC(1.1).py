#Author: zimtroeschen
#Date: 21.03.2020 (21st June 2020)
#Programm Version: 1.1
#Ask me if you want to edit this program and republish it.
#Contact Email: zimtroeschenchan@gmail.com

print('ReclistCVVC (Version 1.1)')
print('-Release 2020/06/21')
print('-License: Freeware')
print('-Author: Zimtroeschen')
print('PLEASE INPUT YOUR LETTERS DEVIDED WITH A COMMA')
helpf=input('WRITE "HELP" IF YOU NEED HELP WITH ANYTHING ')
if helpf=='HELP' or helpf=='help':
    print('Tutorial: https://youtu.be/eZABLNzXm90')
    print('Contact: zimtroeschenchan@gmail.com/zimty_p')
    
print(' ')
k=input('Consonants: ')
v=input('Vowels: ')
print(' ')
a=0
b=0
a2=0
b2=0
yn=input("Do you want to give your reclist a custom name? (Y/N) ")
if yn=="N" or yn=="n":
    reclist="reclist"
else:
    reclist=input("Reclist Filename: ")


import os #writes the text files
fileName=reclist+".txt"
os.path.isfile(fileName)
fobj=open(fileName, "w")

def cfind(string,counter):
    while len(string)>counter and string[counter]!=",":
        counter=counter+1
    counter=counter+1
    return counter

ynvv=input('Do you want to add vowel transitions? (Y/N) ')
if ynvv=='Y' or ynvv=='y':
	vv=v
	t=input('Input the transition sign for your VVs! (Or leave it empty.) ')

print(' ')

def vokala(a,k):
   fobj.write(v[b:cfind(v,b)-1]+"\n")
   while a<=len(k):
       fobj.write(k[a:cfind(k,a)-1]+v[b:cfind(v,b)-1]+k[a:cfind(k,a)-1]+"\n")
       a=cfind(k,a)

def vokalvokal(a2,vv):
   while a2<=len(vv):
       fobj.write(vv[a2:cfind(vv,a2)-1]+t+v[b2:cfind(v,b2)-1]+"\n")
       a2=cfind(vv,a2)

if ynvv=='Y' or ynvv=='y':
    while b2<=len(v):
        vokalvokal(a2,vv)
        b2=cfind(v,b2)

while b<=len(v):
   vokala(a,k)
   b=cfind(v,b)

print('Your reclist is finished!')

fobj.close()

quit=input("Press a random key to quit the program.")
#only there to keep the program running as long as you want
