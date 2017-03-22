import re
import math
import sys

if len(sys.argv) < 2:
 print "Usage: \n"
 print "python KissToPLA_XOR.py <input kiss2 file> <outputName>"
 sys.exit(1)


filename = sys.argv[1]
outputName = sys.argv[2]
fileoutput = outputName + ".pla"


fin=open(filename,'r')
fout=open(fileoutput, 'w')

fin.readline() # garbage line
i= fin.readline()
o = fin.readline()
p = fin.readline()
s = fin.readline()

s = int(re.findall('\d+',s)[0])
numBits = int(math.log(int(s),2))
FORMAT = "{:0"+ str(numBits)+"b}"
print(numBits)

inputs = list()
outputs = list()

for line in fin:
    tmp = re.sub("[^\w,-]"," ",line).split()    #tmp will now contain input state1, state2, output,
    tmp[1]  = re.findall('\d+', tmp[1])[0]
    tmp[2] = re.findall('\d+',tmp[2])[0]#pulling the digits out of tmp2 and tmp1 

    modifiedQ = int(tmp[1]) ^ int(tmp[2])#XOR state1 and state2
    tmp[2] = FORMAT.format(modifiedQ);#redundantly putting it back, but oh well
    tmp[1] = FORMAT.format(int(tmp[1]))
    inputs.append( str(tmp[0]) + str(tmp[1]))
    outputs.append( str(tmp[2]) + str(tmp[3]))
    

#modify the Header for the PLA
# .i size inputs
# .o size outputs
# .ilb names of inputs
# .ob names of outputs
# .p nume of statements

ilb = ""
ob = ""

for i in range(0,len(inputs[0])):
    ilb = ilb + " i" + str(i)
for o in range(0,len(outputs[0])):
    ob = ob + " o" + str(o)


i = ".i " + str(len(inputs[0]))
o = ".o " + str(len(outputs[0]))
ilb = ".ilb" + ilb
ob = ".ob" + ob
p = ".p " + str(len(inputs))

fout.write(i + "\n")
fout.write(o + "\n")
fout.write(ilb + "\n")
fout.write(ob + "\n")
fout.write(p + "\n")
for i in range(0,len(inputs)):
    fout.write(inputs[i] +" "+ outputs[i] + "\n");
