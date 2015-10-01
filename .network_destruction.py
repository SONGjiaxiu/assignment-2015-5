import sys

def readfile(input):
	f = open(input, 'r')
	for line in f:
		temp = line.split()
		var1 = int(temp[0])
		var2 = int(temp[1])
		if var1 in adjlist:
			adjlist[var1].append(var2)
		else:
			adjlist[var1] = [var2] 
		if var2 in adjlist:
			adjlist[var2].append(var1)
		else:
			adjlist[var2] = [var1] 
def changelist1(netlist):
	max = 0
	for d in netlist:
		if len(d) > max:
			max = len(d)
			maxnet = d	
	max = 0
	for key in maxnet:
		if max < len(maxnet[key]):
			max = len(maxnet[key])
			k = key
	netlist.remove(maxnet)
	removenode(netlist, maxnet, k)
	return k, max


def changelist2(netlist):
	max = 0
	for d in netlist:
		if len(d) > max:
			max = len(d)
			maxnet = d	
	maxmetric = 0
	sum = 0
	for key in maxnet:
		visited = []
		l = []
		for i in range(maxcount):
			visited.append(False)
		DFS2(maxnet, key, visited, l)
		for i in l:
			sum += len(maxnet[i]) - 1
		metric = (len(maxnet[key]) - 1) * sum
		if maxmetric < metric:
			maxmetric = metric
			k = key
		sum = 0
	netlist.remove(maxnet)
	removenode(netlist, maxnet, k)
	return k, maxmetric
def DFS2(maxnet, node, visited, l, prev = [], c = -1):
	if visited[node] == True:
		return
	elif c == r+1:
		return
	visited[node] = True
	c += 1
	if c == r:
		l.append(node)
		return
	for i in maxnet[node]:
		if visited[i] == False and i not in prev:
			DFS2(maxnet, i, visited, l, maxnet[node],c)
			
def removenode(netlist, maxnet, key):
	
	l = maxnet[key]
	del maxnet[key]
	d = {key:[key]}
	netlist.append(d)
	for i in l:
		maxnet[i].remove(key)
	visited = []
	for i in range(maxcount):
		visited.append(False)

	for node in l:
		d = {}
		DFS(maxnet, node, visited, d)
		if d != {}:
			netlist.append(d)

def DFS(maxnet, node, visited, d):
	if visited[node] == True:
		return
	visited[node] = True
	for i in maxnet[node]:
		if visited[i] == False:
			DFS(maxnet, i, visited, d)
	d[node] = maxnet[node]
	del maxnet[node]
		
def nettolist(dict):
	l = []
	for n in dict:
		l.append(n)
	l.sort()
	return l	

def listtostr(list):
	s = "Size: "
	s += str(len(list))
	s += " members: "
	list.sort()
	s += str(list)	
	return s

def customprint(s):
	if len(s) > 80:
		for i in range(79, 0, -1):
			if s[i] == ' ':
				break
		print(s[0:i])
		print("    ",end='')
		print(s[i+1:])
	else:
		print(s)

def printnets(netlist, node, metric):
	l = []
	print("Removing node:",node,"with metric:",metric)
	for d in netlist:
		l.append(nettolist(d))
	l.sort()
	for t in l:
		s = listtostr(t)
		customprint(s)


def count_influence(c):
	# h lista ayth tha periexei ola ta diktya pou
	# prokyptoyn kathe fora
	netlist = [adjlist]
	l = nettolist(netlist[0])
	s = listtostr(l)
	customprint(s)
	for i in range(c):
		node, metric = changelist1(netlist)
		printnets(netlist, node, metric)


def collective_influence(c):
	# h lista ayth tha periexei ola ta diktya pou
	# prokyptoyn kathe fora
	netlist = [adjlist]
	l = nettolist(netlist[0])
	s = listtostr(l)
	customprint(s)
	for i in range(c):
		node, metric = changelist2(netlist)
		printnets(netlist, node, metric)


adjlist = {}
r = 2
if len(sys.argv) < 3 or len(sys.argv) > 5:
	print("lathos orismata!!")
	exit(1)
if len(sys.argv) == 3:
	inputfile = sys.argv[2]
	readfile(inputfile)
	loops = int(sys.argv[1])
	maxcount = len(adjlist)+1
	collective_influence(loops)
elif len(sys.argv) == 4:
	if sys.argv[1] != "-c":
		print("lathos orismata!!")
		exit(2)
	inputfile = sys.argv[3]
	readfile(inputfile)
	loops = int(sys.argv[2])
	maxcount = len(adjlist)+1
	count_influence(loops)
else:
	if sys.argv[1] != "-r":
		print("lathos orismata!!")
		exit(2)
	inputfile = sys.argv[4]
	readfile(inputfile)
	loops = int(sys.argv[3])
	r = int(sys.argv[2])
	maxcount = len(adjlist)+1
	collective_influence(loops)




















