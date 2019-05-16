# -*- coding: utf-8 -*-
"""
Created on Wed Apr 17 09:36:10 2019

@author: Wyxx
"""

human='MLSRAVCGTSRQLAPVLAYLGSRQKHSLPDLPYDYGALEPHINAQIMQLHHSKHHAAYVNNLNVTEEKYQEALAKGDVTAQIALQPALKFNGGGHINHSIFWTNLSPNGGGEPKGELLEAIKRDFGSFDKFKEKLTAASVGVQGSGWGWLGFNKERGHLQIAACPNQDPLQGTTGLIPLLGIDVWEHAYYLQYKNVRPDYLKAIWNVINWENVTERYMACKK'
mouse='MLCRAACSTGRRLGPVAGAAGSRHKHSLPDLPYDYGALEPHINAQIMQLHHSKHHAAYVNNLNATEEKYHEALAKGDVTTQVALQPALKFNGGGHINHTIFWTNLSPKGGGEPKGELLEAIKRDFGSFEKFKEKLTAVSVGVQGSGWGWLGFNKEQGRLQIAACSNQDPLQGTTGLIPLLGIDVWEHAYYLQYKNVRPDYLKAIWNVINWENVTERYTACKK'
random='WNGFSEWWTHEVDYNQKLTIENNQRPKIHEHEQWGLRQSPPPPKLCCPTCQMCERMRHQNRFAPLMEVGCRCMCWFHDWWVISVGTWLHTVIMYMMWPKRFHHNECPKACFRTTYTRKNHHALYWMLFEMCCYDQDVVWSKTHIFTTVRDIEVYVEQVFFIWGPLCHVAIACYEPVKTIRRRIPMYLCRHCIRGDNSYLLACCSIIYYFYHHMSYYGVLDIL'


#define how to calculate percentage identity
def per(a,b):
    suma=len(a)
    sumb=len(b)
    if suma!=sumb:
        print('The two sequences differ in lenth.')
    else:         #use a loop to count the number of the same amino acids at the same sites
        count=0
        for i in range(len(a)):
            if a[i]==b[i]:
                count+=1
        per=str(count/len(a)*100)+'%' 
    return per
perhm_m=per(human,mouse)
perhm_r=per(human,random)
perm_r=per(mouse,random)


#define how to calculate edit distance
def edit_distance(a,b):
    edit_distance=0
    for i in range(len(a)):
        if a[i]!=b[i]: #at the same site, if the amino acids are different, edit_distance+1
            edit_distance+=1
    return edit_distance

dishm_m=edit_distance(human,mouse)
dishm_r=edit_distance(human,random)
dism_r=edit_distance(mouse,random)




#calculate score
#creat a 2D dictionary
xfile=open('blosum62 matrix.txt','r')
reader=xfile.readlines()
xfile.close

x=1#x is used to separate the first row
my_Dict={}
letter1=[] #letter1 will contain the elements in the first row
for line in reader:
    splited=line.split()
    if x==1:
        for i in splited:
            my_Dict[i]={}
            letter1.append(i)
        x=2 #The first row is separated from the next and the elements are stored in the dictionary. 
    else:
        letter2=splited[0]#letter2 mains the amino acid in every line
        for j in range(1,len(letter1)):
            b=letter1[j]
            my_Dict[b][letter2]=splited[j]#As the file is read line by line, we can get all combinations.

scorehm_m=0
scorehm_r=0
scorem_r=0
for n in range(0,len(human)):
    scorehm_m=scorehm_m+int(my_Dict[human[n]][mouse[n]])
    scorehm_r=scorehm_r+int(my_Dict[human[n]][random[n]])
    scorem_r=scorem_r+int(my_Dict[mouse[n]][random[n]])

print('The human-mouse score is %d'%(scorehm_m),'\nThe human-mouse normalised Blosum score is %f'%(scorehm_m/len(human)),'\nThe human-mouse edit distance is %d'%(dishm_m),'\nThe human-mouse percentage identity is about '+perhm_m)
print('\nThe human-random score is %d'%(scorehm_r),'\nThe human-random normalised Blosum score is %f'%(scorehm_r/len(human)),'\nThe human-random edit distance is %d'%(dishm_r),'\nThe human-random percentage identity is about '+perhm_r)
print('\nThe mouse-random score is %d'%(scorem_r),'\nThe mouse-random normalised Blosum score is %f'%(scorem_r/len(mouse)),'\nThe mouse-random edit distance is %d'%(dism_r),'\nThe mouse-random percentage identity is about '+perm_r)
#normalised Blosum score=score/len(human)

