from src import PDB
from src import Pose
from optparse import OptionParser

optionparser = OptionParser()
optionparser.add_option( '-p', '--pdbFile', default=None, help='path to pdb file.' )
optionparser.add_option( '-v', '--exclude', default=None, help='Chains to exlude.' )
optionparser.add_option( '-c', '--include', default=None, help='Chains to include.' )

(opt,args) = optionparser.parse_args()



if opt.pdbFile == None:
	print "User must supply path to pdb file using -p flag!"
	exit()
if ( (opt.exclude == None) and (opt.include == None ) ):
	print "User must supply path chains to extract (-c) or chains to exclude (-v)!"
	print "\t example ( \"-c ACD\" will extract chains A, C, & D"
	print "\t           \"-v B\"   will extract all chains except B)"
	exit()



poses = PDB.PDB( opt.pdbFile )
if opt.exclude != None:   opt.exclude = set([ one for one in opt.exclude ])
elif opt.include != None: opt.include = set([ one for one in opt.include ])	

final=PDB.PDB()
for p in poses:
	pose = Pose.Pose( p.model )	
	if opt.exclude:  
		for chain in p:
			if chain.ID() in opt.exclude: continue
			pose.add_chain( chain )
	
	elif opt.include:
		for chain in p:
			if chain.ID() not in opt.include: continue
			pose.add_chain( chain )
	pose.renumber()
	final.add_pose(pose,p.model)


print final			

#seq = pose[1].seq()

