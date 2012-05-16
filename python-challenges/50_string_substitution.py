from itertools import izip
import sys

class StringPiece():
	def __init__(self, value, scannable=True):
		self.value = value
		self.scannable = scannable


def scan(string, scan_list):
	string_pieces = []
	string = StringPiece(string)
	string_pieces.append(string)

	for scan in scan_list:
		piece_idx = 0
		while piece_idx < len(string_pieces):
			string_p = string_pieces[piece_idx]
			if string_p.scannable == False:
				piece_idx += 1
				continue
			
			scan_idx = string_p.value.find(scan[0])
			if scan_idx > -1:
				# remove the whole piece and split it up into 
				# piece before replacement
				# replacement (no scannable)
				# piece after replacement
				string_p_idx = string_pieces.index(string_p)
				string_pieces.remove(string_p)

				end_p = string_p.value[scan_idx + len(scan[0]):]
				if len(end_p) > 0:
					string_pieces.insert(string_p_idx, StringPiece(end_p))

				replacement = scan[1]
				string_pieces.insert(string_p_idx, StringPiece(replacement, False))

				start_p = string_p.value[:scan_idx]
				if len(start_p) > 0:
					string_pieces.insert(string_p_idx, StringPiece(start_p))
			else:
				piece_idx += 1

	final = []
	for string_piece in string_pieces:
		final.append(string_piece.value)

	print ''.join(final)
		


if __name__ == '__main__':
	for line in open(sys.argv[1]):
		if len(line.strip()) > 0:
			string, scan_list = line.strip().split(';')
			it = iter(scan_list.split(','))
			scan_list = izip(it, it)
			scan(string, scan_list)
	sys.exit(0)
