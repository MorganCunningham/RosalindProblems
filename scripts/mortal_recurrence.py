def recurring_rabbits(m,k,d, rabbits):

    if m == 0 or m == 1: 
        rabbits.append(1)
        
    elif m<d:
        rabbits.append(rabbits[m-1] + rabbits[m-2])
    elif m==d:
        rabbits.append(rabbits[m-1] + rabbits[m-2]-1)
    else:
        rabbits.append(rabbits[m-1] + rabbits[m-2]-rabbits[m-(d+1)])
    
    return rabbits

#n months
#k rabbits
file = open("data/rosalind_fibd.txt").read()
file = file.replace("\n", "")
file = file.split(" ")

n = int(file[0])
d = int(file[1])

#n = 6
#rabbits live for this many months
#d=3 
#rabbit reproduction multiplier
k = 1

rabbits = []

for m in range(n):
    print(m)
    rabbits = recurring_rabbits(m,k,d,rabbits)
    print(rabbits)
print(rabbits[n-1])