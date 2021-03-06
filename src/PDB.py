import string
import Pose
import PDB_util

class PDB( object ):
	def __init__(self, path = None):
		self.__models={ 1:Pose.Pose() }
		self.__header=''
		self.__inputFile = path
		
		if path != None:
			self.__inputFile = path
			self.read_pdb()

	def __iter__(self):
		for modid in sorted(self.__models.keys()):
        		yield self.__models[ modid ]

	def __getitem__(self, model):
		return self.__models[ model]

	def __str__(self):
		data = self.__header
		if len(self.__models) == 1: data += self.__models[1].__str__()

		else:
			for model in sorted(self.__models.keys()):
				data+= "MODEL\t     " + str(model) +'\n'
				data+= self.__models[ model ].__str__()
				data+= "\nENDMDL\n"
		return data
			
	def add_pose(self, pose, modid = 1 ):
		self.__models[modid] = pose
		
	def read_pdb(self):
		model = 1
		self.__models[ model ] = Pose.Pose( model )

		for line in open( self.__inputFile, 'r'):

			if "MODEL" == line[0:5]: 
				model = int(string.split(line)[1])
				self.__models[ model ] = Pose.Pose( model )

			elif ( ("ATOM" == line[0:4]) or ( "HETATM" ==line[0:6]) ):
				self.__models[ model ].add_atom( PDB_util.pdb2Atom(line) ) 
				
			elif ( ("TER" == line[0:3] ) or ( "ENDMDL" == line[0:6] ) or ("END" == line[0:3] ) ):
				continue
			else: self.__header += line	

if __name__ == '__main__':
	filepath = '/Users/Josh/Downloads/1G03.pdb'
	#filepath = '/Users/Josh/Downloads/1C4F.pdb'
	pdb=PDB(filepath)
	#print pdb[20]['A'][20]
	#print '\n',  pdb[1]['A'][20]
	print pdb
