import re
import math
import sys

if len(sys.argv) != 2:
 print "Usage: \n"
 print "python KissToPLA_XOR.py <input kiss2 file>"
 sys.exit(1)


filename = re.sub('\.kiss2$','',sys.argv[1])
fileoutput = filename + "_ModNextState.kiss2"


fin=open(sys.argv[1],'r')
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
    tmp = re.sub("[^\w,-]"," ",line).split()#tmp will now contain input state1, state2, output,
    tmp[1]  = re.findall('\d+', tmp[1])[0]
    tmp[2] = re.findall('\d+',tmp[2])[0]#pulling the digits out of tmp2 and tmp1 
    modifiedQ = int(tmp[1]) ^ int(tmp[2])
    tmp[2] = str(modifiedQ);
    tmp.append('\n')
    fout.write(" ".join(tmp));

    
