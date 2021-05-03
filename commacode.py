def commacode(mylist):
	string=''
	l=len(mylist)

	string+=str(mylist[0] )

	for i in range(1,l-1):
		
			string+=', '+str(mylist[i])

	string+=' and '+str(mylist[l-1])
	return string



spam = ['apples', 'bananas', 'tofu', 'cats']
gourob=[1,2,3,4,5,6,7]
spamres = commacode(gourob)
print(spamres)