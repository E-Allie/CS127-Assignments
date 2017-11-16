import csv

def remove_non_alpha(w):
	w=list(w)
	for i,l in enumerate(w):
		if not l.isalpha() and l!=" " and l!="\n" and l!="'":
				w[i]=" "
	w="".join(w).lower().split()
	return w

def interpret_csv(file):
	offend = csv.reader(open(file,newline=""))
	l = []
	for line in offend:
	    l.append(line)
	return l

def build_index(file,id_num,state_num):
	inv={}
	l=interpret_csv(file)
	ID=[x[id_num] for x in l]
	statement=[remove_non_alpha(x[state_num]) for x in l]
	for i,sinlist in enumerate(statement):
		for w in sinlist:
			if w not in inv:
				inv.setdefault(w,[])
			if ID[i] not in inv[w]:
				inv[w].append(ID[i])
	return inv


d=build_index("offenders.csv",3,8)
print("I've:", sorted(d["i've"]))
print("Mom:", sorted(d["mom"]))
print("Dog:", sorted(d["dog"]))