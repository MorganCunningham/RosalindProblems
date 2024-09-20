
class mendel_population:
    def __init__(self, zygosity, n):
        self.zygosity = zygosity
        self.n = n


def punnet_odds(organism_1, organism_2):

    if organism_1.zygosity == "dominant" and organism_2.zygosity == "dominant": return 1
    if organism_1.zygosity == "dominant" and organism_2.zygosity == "hetero": return 1
    if organism_1.zygosity == "dominant" and organism_2.zygosity == "recessive": return 1
    if organism_1.zygosity == "hetero" and organism_2.zygosity == "hetero": return 0.75
    if organism_1.zygosity == "hetero" and organism_2.zygosity == "homo": return 0.50
    if organism_1.zygosity == "homo" and organism_2.zygosity == "homo": return 0

def population_odds_dom_pheno(dominant, hetero, recessive):

    odds_sum = 0

    population_total = dominant.n + recessive.n + hetero.n

    odds_sum += (dominant.n/population_total) * ((dominant.n-1)/(population_total -1))*1 #dom dom
    
    odds_sum += (dominant.n/population_total) * ((hetero.n)/(population_total -1)*1)*1*2 # hetero dom
    
    odds_sum += (dominant.n/population_total) * ((recessive.n)/(population_total -1))*1*2 # dom recessive
    
    odds_sum += (hetero.n/population_total) * ((hetero.n-1)/(population_total -1))*.75 #hetero hetero
    
    odds_sum += (hetero.n/population_total) * ((recessive.n)/(population_total -1))*.50*2 # hetero rec

    return odds_sum


file = open("data/rosalind_iprb.txt").read()
file = file.replace("\n", "")
population_count = file.split(" ")

dominant = mendel_population("dominant", float(population_count[0]))
hetero = mendel_population("hetero", float(population_count[1]))
recessive = mendel_population("recessive", float(population_count[2]))

probability = population_odds_dom_pheno(dominant, hetero, recessive)
print(probability)

