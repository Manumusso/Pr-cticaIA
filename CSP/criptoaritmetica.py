
#Problema Suma

#
#    C3  C2 C1
#      T   W   O
# +    T   W   O  
#   ------------------
#   F   O   U   R

letters = [
    "T",
    "W",
    "O",
    "F",
    "U",
    "R",
]

carries = [
    "C3",
    "C2",
    "C1",
]

variables = letters + carries

domains = {}

for leter in letters:
    domains[leter] = list(range(10))
for carrie in carries:
    domains[carrie] = [0,1]

print ("Variables:", variables)
print ("Domains:", domains)