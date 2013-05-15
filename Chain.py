import Residue, PDB_util

class Chain( object ):
	def __init__(self, chain='A' ):
		self.__ID = chain
		self.__resi = {}
		self.__map = {}

	def __str__(self):
		data=''
		for resi in self.__iter__():
			for atom in resi:
				data += PDB_util.Atom2pdb( atom )
		return data

	def __iter__(self):
		for resi in sorted(self.__resi.keys()):
        		yield self.__resi[ resi ]
	
	def __getitem__(self, resnum):
		try: return self.__resi[ self.__map[ resnum ]  ]
		except KeyError:
			print "Residue number "+ str(resnum) + " not found in chain " + self.__ID +'.'
			print  "Available residues: " +str( self.__resi.keys() )
			raise KeyError
	
	def __getslice__(self, begin, end):
		try:
			new = Chain( self.__ID )
			for one in sorted(self.__map.keys()):
				if ( one < begin ): continue
				if ( one > end ): break
				for a in self.__resi[ self.__map[one] ]:
					new.add_atom( a )
			return new
		except KeyError:
			print "Residue number "+ str(one) + " not found in chain " + self.__ID +'.'
			print  "Available residues: " +str( self.__resi.keys() )
			raise KeyError			
	
	def __add__(self, chain2):
		ch = Chain( self.__ID )
		i = sorted(self.__resi.keys())[-1] + 1
		chain2.set_ID( self.__ID )
		for r in self:
			for a in r:
				ch.add_atom( a )
		for off,r2 in enumerate(chain2):
			r2.set_resnum(i+off)
			for a2 in r2:
				ch.add_atom( a2 )
		return ch
	
	def seq( self ):
		s=''
		for r in self:
			if r.name3() == 'HOH': continue
			s+=r.name1()	
		return s		

	def ID(self): return self.__ID

	def set_ID(self, ID ):
		self.__ID = ID
		for resi in self.__iter__():
			for atm in resi: atm.set_param( "chain", self.__ID  )	
	
	def add_atom( self, atm ):
		if atm.resSeq  not in self.__resi.keys():
			self.__resi[ atm.resSeq ] = Residue.Residue( atm.resi_name )
			self.__map[ atm.resSeq ] = atm.resSeq
		self.__resi[ atm.resSeq ].add_atom( atm )
 
	def renumber(self, i=1):
		for num, resi in enumerate(self.__iter__()):
			self.__map[ resi.resnum ] = num+1
			resi.set_resnum( num+1 )
			for atom in resi:
				atom.set_param("atm_number", i )
				i+=1
		return i
			
