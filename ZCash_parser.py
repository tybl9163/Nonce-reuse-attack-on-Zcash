#Written by Christopher Bishop for ECEN5033, spring semester at CU Boulder
#May 6, 2019

nonce_dict = {}

def parse_blockdata(filename):

	with open(filename, 'rt') as file:
		nonces_reused = 0
		txid = 0							#Holds on to txid to return in tuple
		txflag = 0							#Sets a flag low to identify first txid
		i = 0								#Counter for line of .txt
		prev_line = ''						#Useful to check for proper hex field
		for line in file:											#	#
			i= i+1
			if (txflag is 0) and ('txid' in line) and ('transaction' not in line):
				txid = line
				txflag = 1							#Set flag high to read hex scriptSig
			if (txflag is 1) and ('asm"' in prev_line) and ('string' not in prev_line):
				if ('OP' not in prev_line):				#This is to handle newly generated coin errors
					#print('txt #: ', i)
					txflag = 0							#Reset txflag for next transaction
					
					#Format the txid. Keep this here for efficiency
					txid = txid.split(": ")
					txid = txid[1]						#Throwout "hex" string
					txid = txid[1:-1]					#Throwout quotes
					
					sig = line.split(": ")				#This list is ["hex", "sig...[ALL]...."]
					sig = sig[1]						#Throwaway "hex" string
					sig = sig[3:-2]						#Throwout first (") and two digit OP code at beginning, last (") and \n
					sig = sig[0:130]					#Grab 64 byte signature

					(r, s) = decode_sig(sig)
					print('r:', r)

					if r in nonce_dict:					#Append txid to value list of dict
						nonce_dict[r].append(txid)
						print('reused r:', r)
						nonces_reused = (nonces_reused + 1)
					else:								#Add new key, value pair
						nonce_dict[r] = [txid]
			prev_line = line
		print('nonces reused:', nonces_reused)


def decode_sig(sig, bits=256):
    '''
    Decodes a signature (hex) string to a tuple (r, s)
    This code was written by Eric Wustrow, and provided for the course ECEN5033
    '''
    #print('sig:',sig)
    #print('sig len', len(sig))
    r = int(sig[:bits/4], 16)
    s = int(sig[bits/4:], 16)
    return (r, s)


#parse_blockdata('transaction_output_full.txt')
parse_blockdata('parse_1000.txt')

