import PDB_util
from string import strip, ljust, rjust, center
from scipy import array

class Atom( object ):
	def __init__(self, line=None):
			self.atm_type  =''
			self.atm_number=0
			self.atm_name  =''
			self.alt_loc   =''
			self.resi_name =''
			self.chain     =''
			self.resSeq    =0
			self.icode     =''
			self.pos       =array([0.0, 0.0, 0.0])
			self.occ       =0.0
			self.bfac      =0.0
			self.elem      =''
			self.charge    =''
			self.valid     =False
			
	def __str__(self):
		return PDB_util.Atom2pdb( self )			

	def set_param(self, param, value):
		vt=type(value)
		if param in self.__dict__.keys():
			if vt == type(self.__dict__[param] ): self.__dict__[param] = value
			else: print "Passed " + str(param) +" of type "+ str(vt) +" dose not match required " +str(type(self.__dict__[param]))  
		else:
			print str(param) + " is not in [" + join(self.__dict__.keys(),', ') +']'

