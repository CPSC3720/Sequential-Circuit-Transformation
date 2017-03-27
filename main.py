import sys
import os
import os.path
from subprocess import call

## Constants
ESOP_EXT = ".esop"
PLA_EXT = ".pla"

if len(sys.argv) != 2:
    print "Usage:"
    print "python main.py <input-kiss2-file>"
    sys.exit(1)

# ## Store arguments
inputKiss2 = sys.argv[1]

tempPath = os.path.split(inputKiss2)[1]
inputFileNameWithExtensionRemoved = os.path.splitext(tempPath)[0]

## First, we convert the input kiss2 file to a .pla
call("python KissToPLA_XOR.py %s %s" %
    (inputKiss2, inputFileNameWithExtensionRemoved), shell = True)

## Second, pass .pla file through exorcism_org
call("./exorcism_org %s" %
    inputFileNameWithExtensionRemoved + PLA_EXT, shell = True)


## Call shared cubed synthesis program and output to a metrics text file
call("./GetGateCount.sh %s" % inputFileNameWithExtensionRemoved + ESOP_EXT, shell = True)

## Clean up
os.remove(inputFileNameWithExtensionRemoved + PLA_EXT)
