
# we take a kiss2 file, which is formatted as follows
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

filename = '../MCNC/Sequential/Kiss2/ex1.kiss2'
fileoutput = './ex1Converted.kiss2'

fin=open(filename,'r')
fout=open(fileoutput, 'w')

fin.readline() # garbage line
i= fin.readline()
o = fin.readline()
p = fin.readline()
s = fin.readline()

fout.write('\n')
fout.write(i)
fout.write(o)
fout.write(p)
fout.write(s)

for line in fin:
    tmp = re.sub("[^\w,-]"," ",line).split()    #tmp will now contain input state1, state2, output,
    modifiedQ = int(tmp[1]) ^ int(tmp[2])
    tmp[2] = str(modifiedQ);
    tmp.append('\n')
    fout.write(" ".join(tmp) );

  