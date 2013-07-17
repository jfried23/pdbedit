from src import PDB, Pose
from optparse import OptionParser
from os.path import split

optionparser = OptionParser()
optionparser.add_option( '-p', '--pdbFile', default=None, help='path to pdb file.' )

(opt,args) = optionparser.parse_args()



if opt.pdbFile == None:
	print "User must supply path to pdb file using -p flag!"
	exit()


poses = PDB.PDB( opt.pdbFile )
for pose in poses:
	pose.renumber()




file_name = split( opt.pdbFile )[-1].split('.')[0] +'_renum.pdb'

h=open( file_name, 'w')

h.writelines( poses.__str__() )

h.close()	 		




