import re
import math
import os
import sys

if len(sys.argv) != 2:
 print "Usage: \n"
 print "python KissToKiss_XOR.py <input kiss2 file>"
 sys.exit(1)

splitPath = os.path.split(sys.argv[1])[1]
filename = os.path.splitext(splitPath)[0]
fileoutput = filename + ".kiss2"

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
