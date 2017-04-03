import sys
import os
from subprocess import call

## Constants
ESOP_EXT = ".esop"
KISS2_EXT = ".kiss2"
PLA_EXT = ".pla"
TXT_EXT = ".txt"

INPUTS_DIR = "inputs/"

OUTPUT_1 = "outputs/step1_Kiss2ToKiss2XOR/"
OUTPUT_2 = "outputs/step2_Kiss2XORToPLA/"
OUTPUT_3 = "outputs/step3_PLAToESOP/"
OUTPUT_4="outputs/step4_metrics/"

if len(sys.argv) == 2:
    INPUTS_DIR = sys.argv[1];

## Iterate each .kiss2 file in the inputs directory and generate a metrics file
for filename in os.listdir(INPUTS_DIR):
    if filename.endswith(".kiss2"):

        tempPath = os.path.split(filename)[1]
        inputFileNameWithExtensionRemoved = os.path.splitext(tempPath)[0]

        ## First, we convert the input kiss2 file to kiss2 with modified states
        call("python KissToKiss_XOR.py %s" %
            INPUTS_DIR + filename, shell = True)

        ## Second, we convert the modified kiss2 file to .pla
        call("python KissToPLA.py %s %s" %
            (inputFileNameWithExtensionRemoved + KISS2_EXT, inputFileNameWithExtensionRemoved), shell = True)

        ## Third, pass .pla file through exorcism_org
        call("./exorcism_org %s" %
            inputFileNameWithExtensionRemoved + PLA_EXT, shell = True)
        ## Note: the .esop file is consumed by the shared cube synthesis program, so we make a
        ## copy of the file to the OUTPUT_3 folder in this step.
        call("cp " + inputFileNameWithExtensionRemoved + ESOP_EXT + " " + OUTPUT_3, shell = True)

        # Fourth, call shared cubed synthesis program and output to a metrics text file
        call("./GetGateCount.sh %s" % inputFileNameWithExtensionRemoved + ESOP_EXT, shell = True)

        ## Move intermediate files to outputs folder,
        call("mv " + inputFileNameWithExtensionRemoved + KISS2_EXT + " " + OUTPUT_1, shell = True)
        call("mv " + inputFileNameWithExtensionRemoved + PLA_EXT + " " + OUTPUT_2, shell = True)
        call("mv " + inputFileNameWithExtensionRemoved + TXT_EXT + " " + OUTPUT_4, shell = True)

        continue
    else:
        continue
