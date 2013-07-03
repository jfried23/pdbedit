
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
for pose in poses:
	if opt.exclude ! = None:  
		

seq = pose[1].seq()

print seq	
