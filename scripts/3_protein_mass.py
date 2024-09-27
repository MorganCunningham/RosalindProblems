




p_m_dict={}
with open("data/rosalind_protein_mass_tab.txt") as file:
    for line in file:
        p_m = line.split()
        protein, mass = p_m[0], float(p_m[1])
        p_m_dict[protein] = mass
file.close()
with open("data/rosalind_prtm.txt") as file:
    protein = file.read().strip()
file.close()
print(protein)
# test case. weight = 821.392
#protein = 'SKADYEK'

protein_weight = 0
for amino in protein: protein_weight += p_m_dict.get(amino)

print(protein_weight)