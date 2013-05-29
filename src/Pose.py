from sys import exit
from string import ascii_uppercase
import PDB_util
import Chain 


class Pose( object ):
	def __init__(self, model=1):
		self.__model = model
		self.__chains = {}

	def __iter__(self):
		for chain in sorted(self.__chains.keys()):
        		yield self.__chains[ chain ]

	def __str__(self):
		data=''
		for chain in self.__iter__():
			for rnum, residue in enumerate(chain):
				for offset, atom in enumerate(residue):
					data += PDB_util.Atom2pdb( atom )
			ter = atom
			ter.set_param('atm_type','TER')
			ter.set_param('atm_name',' ')
			data += PDB_util.Atom2pdb( atom )[0:26]
		data += '\nEND'
		return data
	
	def __getitem__(self, chain):
		try: return self.__chains[ chain ]
		except KeyError:
			print "Chain ID "+ chain + " not found in pose. Available Chains: " +str( self.__chains.keys() )
			raise KeyError
	
	def keys( self ): return sorted( self.__chains.keys() )

	def add_atom( self, atm ):
		if atm.chain not in self.__chains.keys():
			self.__chains[ atm.chain ] = Chain.Chain( atm.chain )
		self.__chains[ atm.chain ].add_atom( atm )
 
	def add_chain( self, chain):
		if chain.ID() not in self.__chains.keys():
			self.__chains[ chain.ID ] = chain
		else:
			for letter in  ascii_uppercase:
				if letter in self.__chains.keys(): continue
					chain.set_ID( letter )
					self.__chains[letter]=chain	 

	def renumber( self, i=1 ):
		for chain in self.__iter__():
			i=chain.renumber(i)	
	
	def seq( self ):
		fasta=''
		for i,ch in enumerate(self):
			if i !=0: fasta+='\n\n'
			fasta += '>' + ch.ID() +'\n' + ch.seq()
		return fasta	

def build_pose( atom_objs ):
	pose = Pose()
	for atm in atom_objs:
		pose.add_atom( atm )	
	return pose

if __name__ == '__main__':
	data=[]
	path1='/Users/Josh/Documents/pdb/1FOS_cln.pdb'
	path2='/Users/Josh/Downloads/1HGD.pdb'
	for line in open(path2,'r'):
		if line[0:4] != 'ATOM': continue
		data.append( PDB_util.pdb2Atom(line) )
			
	pose = build_pose( data )
	pose.renumber()	
	#`for r in pose['A'][8:40]:
	#	print r['N']

	 
	print pose.seq()

