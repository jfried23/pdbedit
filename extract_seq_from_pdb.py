#!/usr/bin/env python
from src import PDB
from optparse import OptionParser


optionparser = OptionParser()
optionparser.add_option( '-p', '--pdbFile', default=None, help='path to pdb file.' )
optionparser.add_option( '-r', '--reverse_seq', default=None, help='Seqencing in the reverse direction.' )

(opt,args) = optionparser.parse_args()



if opt.pdbFile == None:
	print "User must supply path to pdb file using -p flag!"
	exit()


pose = PDB.PDB( opt.pdbFile )

seq = pose[1].seq()

print seq		
