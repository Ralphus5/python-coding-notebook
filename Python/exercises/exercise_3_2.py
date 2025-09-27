AA_MASS = dict(
    G=57.05132, A=71.0779, S=87.0773, P=97.11518, V=99.13106,
    T=101.10388, C=103.1429, L=113.15764, I=113.15764, N=114.10264,
    D=115.0874, Q=128.12922, K=128.17228, E=129.11398, M=131.19606,
    H=137.13928, F=147.17386, R=156.18568, Y=163.17326, W=186.2099
)

WATER_MASS = 18.01528
H_MASS = 1.00784

class Protein:
    def __init__(self, name, uniprot_id, sequence):
        self.name = name
        self.uniprot_id = uniprot_id
        self.sequence = sequence

    def get_length(self):
        return len(self.sequence)
    
    def contains(self, peptide):
        self.peptide = peptide
        return True if peptide in self.sequence else False

    def get_mw(self, disulfides=0):
        total_weight = 0
        for aa in self.sequence:
            total_weight += AA_MASS[aa]
        total_weight += WATER_MASS
        total_weight -= 2 * H_MASS * disulfides
        return total_weight



galanin = Protein("Galanin", "P22466", "GWTLNSAGYLLGPHAVGNHRSFSDKNGLTS")
print(type(galanin))
#> <class '__main__.Protein'>
print(galanin.get_length())
#> 30
print(galanin.contains("CGSHLV"))
#> False
print(galanin.get_mw())
#> 3157.4102999999996
insulin_B = Protein(name="Insulin B chain", uniprot_id="P01308", sequence="FVNQHLCGSHLVEALYLVCGERGFFYTPKT")
print(insulin_B.get_length())
#> 30
print(insulin_B.contains("CGSHLV"))
#> True
print(insulin_B.get_mw(disulfides=1))
#> 3427.9056799999994