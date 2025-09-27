from sys import argv

dna = argv[1]
x = int(argv[2]) - 1
first_name = int(argv[3]) - 3
lists_tuple = int(argv[4])

print(dna[x])
print(dna[first_name:lists_tuple])