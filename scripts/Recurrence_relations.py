def recurring_rabbits(m,k, rabbits):

    if m == 0 or m == 1: 
        rabbits.append(1)
        print(m)
    else: 
        rabbits.append(rabbits[m-1] + k*rabbits[m-2])
        print(m)
    return rabbits

#n months
#k rabbits
file = open("data/rosalind_fib.txt").read()
file = file.replace("\n", "")
file = file.split(" ")

n = int(file[0])
k = int(file[1])
#n = 5
#k = 3

rabbits = []

for m in range(0,n):
    rabbits = recurring_rabbits(m,k,rabbits)
    
print(rabbits[n-1])