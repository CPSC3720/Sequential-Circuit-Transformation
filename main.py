import sys
import os
from subprocess import call

## Constants
ESOP_EXT = ".esop"
PLA_EXT = ".pla"

if len(sys.argv) != 3:
    print "Usage:"
    print "python main.py <input-kiss2-file> <output name>"
    sys.exit(1)

# ## Store arguments
inputKiss2 = sys.argv[1]
output = sys.argv[2]

## First, we convert the input kiss2 file to a .pla
call("python KissToPLA_XOR.py %s %s" %
    (inputKiss2,output), shell = True)

## Second, pass .pla file through exorcism_org
call("./exorcism_org %s" %
    output + PLA_EXT, shell = True)


## Call shared cubed synthesis program and output to a metrics text file
call("./GetGateCount.sh %s" % output + ESOP_EXT, shell = True)

## Clean up
os.remove(output + PLA_EXT)
