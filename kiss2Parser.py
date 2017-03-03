#Currently what i Think needs to happen is...
# we take a kiss2 file, which is formatted as follows ( i think, please correct me if i am misunderstanding )
# .i i  
# .o o 
# .p p 
# .s s 
# iiii stateQ stateQ+ oooo
# ....
# ....
# .... 
# iiii stateQ stateQ+ oooo

#where 'i' is the size of inputs (that is a input will be i digits long), note that i is the index 4
#where 'o' is the size of outputs (output will be o digits long), note that o is the index 8
#where 'p' is the size of the list of transitions that will be described
#where 's' is the number of states that will be described  ////"This is what i think atleast"////

import re

#Lets try opening a .kiss2 file with python first.
##filename = 'E:/pythonParser/ex1.kiss2' 
##fin=open(filename,'r') # 'r' means we are openiong the file for reading versus 'w' for writing
##
##i = fin.readline() #this is some garbage?
##
##i= fin.readline()
##val_i =''.join(n for n in i if n.isdigit())
##print(val_i)
##
##o = fin.readline()
##val_o =''.join(n for n in o if n.isdigit())
##print(val_o)
##
##p = fin.readline()
##val_p =''.join(n for n in p if n.isdigit())
##print(val_p)
##
##s = fin.readline()
##val_s =''.join(n for n in s if n.isdigit())
##print(val_s)

##for line in fin:
##    print(line)

# while not at end of body
# loop
# delete forst
# increment
# increment
# delete
filename = 'D:/3720Project/ex1.kiss2'
fileoutput = 'D:/3720Project/ex1Converted.kiss2'

fin=open(filename,'r')
fout=open(fileoutput, 'w')

fin.readline() # garbage line
i= fin.readline()
o = fin.readline()
p = fin.readline()
s = fin.readline()
print(i)
print(o)
print(p)
print(s)

states = []
listLines = []
listAllInput = []

# in the re.sub("this"), define anything you want to find in the "this" line
for line in fin:
    tmp = re.sub("[^\w,-]", " ", line).split()
    listAllInput += tmp
    listLines.append(tmp)
    listAllInput += '\n'
    print("line; line[1]; line[2]; :")
    print(line)
    print(tmp[1])
    print(tmp[2])
    states.append(int(tmp[1]))
    states.append(int(tmp[2]))


# counts states, sorts a list 
print("states before processing:")
print(states)
states = list(set(states))
states.sort()
print("States:")
print(states)

print("listLines")
print(listLines)

# generates binary map that is parallel with the state map
binaryMap = []
for x in range(0, len(states)):
    binaryMap.append(bin(x))

print("binaryMap:")
print(binaryMap)


# generate a list with the state as a key and the bit value as the answer

print("states:")
for x in range(0, len(states)):
    print(states[x])


#print all lines in listLines

print("List Lines:")
for x in range(0, len(listLines)):
    print(listLines[x][1])
    print(listLines[x][2])
    listLines[x][1] = bin(states.index(int(listLines[x][1])))
    listLines[x][2] = bin(states.index(int(listLines[x][2])))

print("states after they have been replaced:")
for x in range(0, len(listLines)):
    print(listLines[x])

#writing the newly parsed document to a file

fout.write('\n')
fout.write(i)
fout.write(o)
fout.write(p)
fout.write(s)
for x in range(0, len(listLines)):
    fout.write(listLines[x][0])
    fout.write(' ')
    fout.write(listLines[x][1])
    fout.write(' ')
    fout.write(listLines[x][2])
    fout.write(' ')
    fout.write(listLines[x][3])
    fout.write('\n')



#Now we know the size of each 'field' in the body of the file. That is the transition descriptions on each line, so we can use those to parse if needed.
#Also know that I am currently assuming that like ex1, the other kiss2 file states will be labelled from 1<->s (ie. in ex1, s = 20, and we see states [1,20])
# https://en.wikipedia.org/wiki/State_transition_table
#I am going to base this off the one-dimensional table, but perhaps we should ask what the preference is. That or implement both forms for Dr.Rice's convenience

#So we can do a readline(), then grab the first 'i' digits as the input, the next number as the state (Q), the next number as the state-next (Q+), and the last 'o' digits for output
#For the one dimensional format, we would then make each digit of 'i' a column, Q as a column, Q+ as a column and the last 'o' digits as columns

