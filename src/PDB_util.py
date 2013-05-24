from string import strip, ljust, rjust, center
from scipy import array
import Atom

def pdb2Atom( line ):
		try:
			atomobj = Atom.Atom()
			atomobj.atm_type = line[0:6].strip()
			atomobj.atm_number=int(line[6:11])
			atomobj.atm_name  =line[12:16].strip()
			atomobj.alt_loc   =line[16].strip()
			atomobj.resi_name =line[17:20].strip()
			atomobj.chain     =line[21].strip()
			atomobj.resSeq    =int(line[22:26])
			atomobj.icode     =line[26].strip()
			atomobj.pos       =array([ float(line[30:38]),float(line[38:46]),float(line[46:54]) ] )
			atomobj.occ       =float(line[54:60])
			atomobj.bfac      =float(line[60:66])
			atomobj.elem      =line[76:78].strip()
			atomobj.charge    =line[78:80].strip()
			atomobj.valid     = True
			return atomobj
		except:
			pass 

def Atom2pdb( atmobj ):
		try:
			if atmobj.valid != True: return ''
		except:
			return None
			
		atm_type   = ljust(str(atmobj.atm_type),6).upper()
		atm_number = rjust(str(atmobj.atm_number),5)
		
		if atmobj.atm_name[0].isdigit() and atmobj.atm_name[-1].isdigit(): atm_name   = ' '+center(str(atmobj.atm_name),4).upper()	
		elif atmobj.atm_name[-1].isdigit(): atm_name   = ' '+ljust(str(atmobj.atm_name),4).upper()
		elif (atmobj.atm_name[-1] =='\''): atm_name   = ' '+rjust(str(atmobj.atm_name),4).upper()
		else: atm_name   = ' '+center(str(atmobj.atm_name),4).upper()
		
		alt_loc    = center(str(atmobj.alt_loc),1)
		resi_name  = center(str(atmobj.resi_name),3).upper()+' '
		chain      = center(str(atmobj.chain),1).upper()
		resSeq     = rjust( str(atmobj.resSeq),4) 
		icode      = center(str(atmobj.icode),1)+3*' '
		pos        = rjust( "%.3f" % atmobj.pos[0],8)+rjust("%.3f" % atmobj.pos[1],8)+rjust("%.3f" % atmobj.pos[2], 8)
		occ        = rjust( str(atmobj.occ), 6) 
		bfac       = rjust( str(atmobj.bfac),5) + 11*' '
		elem       = center( str(atmobj.elem),2)
		charge     = center(str(atmobj.charge),2) 
	
		return atm_type + atm_number + atm_name + alt_loc+ resi_name + chain + resSeq + icode + pos + occ + bfac + elem + charge+'\n'		


if __name__ == '__main__':
	for line in open('/Users/Josh/Documents/pdb/1FOS_cln.pdb','r'):
		if line[0:4] != 'ATOM': continue
		a = pdb2Atom(line)

		print Atom2pdb(a)
