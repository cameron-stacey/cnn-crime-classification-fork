import pdb
import sys
import os
import re
import subprocess

def split_file(frac_num,root,fp):
    bashCommand = "split -n " + str(frac_num) + " "  + root + "/"+ fp
    process = subprocess.Popen(bashCommand.split(),stdout=subprocess.PIPE)
    output, error = process.communicate()
    m = re.search('(?<=bak)\w+',os.path.join(root,fp))
    bashCommand2 = "mv xaa " + root + "/"  + m.group(0) + ".txt"
    process = subprocess.Popen(bashCommand2.split(),stdout=subprocess.PIPE)
    output, error = process.communicate()
def clean_folder(root,files,frac_num):
    for fp in files:    
        if not (re.search('(bak)\w+',fp)):
            os.remove(os.path.join(root,fp))
	else:
            split_file(frac_num,root,fp)
def run(argv):
    frac_num = argv[1]
    for root, subdir, files in os.walk("data/subdata/"):
        for fp in files:
            if not (re.search('(bak)\w+',fp)):
                os.remove(os.path.join(root,fp))
            else:
                split_file(frac_num,root,fp)

run(sys.argv)