def howmanytimes(amount,total):
	counter = total//amount
	return counter

def addup(combo,total):
	sum=combo[0]+combo[1]*5+combo[2]*10+combo[3]*25+combo[4]*100
	if sum==total:
		return True
	return False




def make_change(total):

	solution=[]

	count100=howmanytimes(100,total)
	count25=howmanytimes(25,total)
	count10=howmanytimes(10,total)
	count5=howmanytimes(5,total)
	count1=howmanytimes(1,total)
	tempsolution=[]
	newtotal = total

	if count1>=1:
		list1=[]
		for i in range(total+1):
			list1.append( [i,0,0,0,0] )

	if count5>=1:
		list5=[]
		for i in range(count5+1):
			list5.append( [0,i,0,0,0] )

	if count10>=1:
		list10=[]
		for i in range(count10+1):
			list10.append( [0,0,i,0,0] )

	if count25>=1:
		list25=[]
		for i in range(count25+1):
			list25.append( [0,0,0,i,0] )

	if count100>=1:
		list100=[]
		for i in range(count100+1):
			list100.append( [0,0,0,0,i] )

	if count100>=1:
		for val100 in list100:
			for val25 in list25:
				for val10 in list10:
					for val5 in list5:
						for val1 in list1:
							if addup([val1[0],val5[1],val10[2],val25[3],val100[4]],total):
								tempsolution=[]
								for i in range(val1[0]):
									tempsolution.append(1)
								for i in range(val5[1]):
									tempsolution.append(5)
								for i in range(val10[2]):
									tempsolution.append(10)
								for i in range(val25[3]):
									tempsolution.append(25)
								for i in range(val100[4]):
									tempsolution.append(100)
								solution.append(tempsolution)
	elif count25>=1:
		for val25 in list25:
			for val10 in list10:
				for val5 in list5:
					for val1 in list1:
						if addup([val1[0],val5[1],val10[2],val25[3],0],total):
							tempsolution=[]
							for i in range(val1[0]):
								tempsolution.append(1)
							for i in range(val5[1]):
								tempsolution.append(5)
							for i in range(val10[2]):
								tempsolution.append(10)
							for i in range(val25[3]):
								tempsolution.append(25)
							solution.append(tempsolution)

	elif count10>=1:
		for val10 in list10:
			for val5 in list5:
				for val1 in list1:
					if addup([val1[0],val5[1],val10[2],0,0],total):
						tempsolution=[]
						for i in range(val1[0]):
							tempsolution.append(1)
						for i in range(val5[1]):
							tempsolution.append(5)
						for i in range(val10[2]):
							tempsolution.append(10)
						solution.append(tempsolution)

	elif count5>=1:
		for val5 in list5:
			for val1 in list1:
				if addup([val1[0],val5[1],0,0,0],total):
					tempsolution=[]
					for i in range(val1[0]):
						tempsolution.append(1)
					for i in range(val5[1]):
						tempsolution.append(5)
					solution.append(tempsolution)
	else:
		for i in range(val1[0]):
			tempsolution.append(1)
		solution.append(tempsolution)

	return solution

def dict_filter(function,dict):
	soldict={}
	for val in dict.keys():
		key = val
		kval = dict[key]
		if function(key,kval):
			soldict[key] = kval
	return soldict




def treemap(function,tree):
    tree.key=function(tree.key,tree.value)[0]
    tree.value=function(tree.key,tree.value)[1]
    for st in tree.children:
        treemap(function,st)


