def list_sort(lista):
	sorted_dict={'chars':[],'evens':[],'odds':[]}
	if type(lista)!=int:
		if type(lista)!=str:
			if len(lista)==0:
				return sorted_dict
			else:
				for a in lista:

					if type(a) == str:
						sorted_dict['chars'].append(a)
					else:
						if a%2==0:
							sorted_dict['evens'].append(a)
						else:
							sorted_dict['odds'].append(a)
		else:
			return "Invalid Input"
	else:
		return "Invalid Input"	
	sorted_dict['chars'].sort()
	sorted_dict['evens'].sort()
	sorted_dict['odds'].sort()

	return sorted_dict	

print(list_sort([2,0,6,5,1,7,'a','z']))

