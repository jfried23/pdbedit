import Atom, PDB_util
from string import replace

AA_3to1={ 'ALA':'A', 'CYS':'C', 'ASP':'D', 'GLU':'E', 'PHE':'F',
          'HIS':'H', 'ILE':'I', 'LYS':'K', 'LEU':'L', 'MET':'M', 
          'ASN':'N', 'PRO':'P', 'GLN':'Q', 'ARG':'R', 'SER':'S',
	  'THR':'T', 'VAL':'V', 'TRP':'W', 'TYR':'Y', 'GLY':'G', 
	}
DNA_3to1={ 'DA':'A' , 'DT':'T' , 'DG':'G' , 'DC':'C',
           'A':'A'  ,  'T':'T' , 'G':'G'  , 'C':'C'
	 }   

class Residue( object ):
	def __init__(self, resi_name ):
		self.__resi_name = resi_name
		self.__resi_num = None
		self.__atoms = []

	def __str__(self):
		data=''
		for atom in self.__iter__():
			data += PDB_util.Atom2pdb( atom )
		return data

	def __iter__(self):
		for resi in self.__atoms:
        		yield resi

	def __getitem__(self, atm_name):
		try:
			for a in self.__atoms:
				if a.atm_name == atm_name: return a
			raise KeyError

		except KeyError:
			print "Atom "+ atm_name + " not found in residue " + str(self.__resi_num)+self.__resi_name  +'.'
			raise KeyError

	def resnum(self): return self.__resi_num
	
	def set_resnum(self,num):
		self.__resi_num = num
		for atom in self.__iter__():
			atom.set_param( "resSeq", self.__resi_num )

	def name3(self): return self.__resi_name

	def name1(self):
		try:
			return AA_3to1[ self.__resi_name ]
		except KeyError:
			try:
				return DNA_3to1[ self.__resi_name ]
			except KeyError:
				return ' '+self.__resi_name.replace(' ','')+' ' 

	def add_atom( self, atm ):
		if self.__resi_num == None: self.__resi_num = atm.resSeq
		self.__atoms.append( atm )

if __name__ == '__main__':
	print AA_3to1['CYT']
