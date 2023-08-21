
class Amino:
	def __init__(self,kod,namn,grupp,mm):
		self.kod = kod
		self.namn = namn
		self.grupp = grupp
		self.mm = mm
	
	def __str__(self):
		return self.kod + ' ' +  self.namn + ' '+ self.grupp + ' ' + str(self.mm)

	def split(self):
		return (self.__str__()).split()

	def __repr__(self):
		return self.__str__()


def read():
	aminotxt = open('aminosyror.txt', 'r', encoding='latin-1')
	read = []
	for line in aminotxt.readlines():
		inputs = line.split()

		read.append(
			Amino(inputs[0],inputs[1],inputs[2],float(inputs[3])))

	return read


def main():
	blah = read()	
	while True:
		print(
			' 1 - print table of aminoacids sorted by code','\n',
			'2 - print table of aminoacids sorted by name','\n',
			'3 - print table of aminoacids sorted by group','\n',
			'4 - print table of aminoacids sorted by mm','\n',
			'5 - close program')
		svar = int(input('Enter one option: '))
		print('\n'*2)
		if svar==1:
			blah.sort(key = lambda x:x.kod)
		elif svar==2:
			blah.sort(key = lambda x:x.namn)
		elif svar==3:
			blah.sort(key = lambda x:x.grupp)
		elif svar==4:
			blah.sort(key = lambda x:x.mm)
		elif svar==5:
			return 5
		for x in blah:
			print(str(x))
main()