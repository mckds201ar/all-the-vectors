# read in the vectors.txt file
# create a  list of vectors
# scale the first and last vector by 3
# add them all together and find
# that new vector
# find the norm of the final vector
# also find the dot product between the 2nd and 3rd vector
from vector import Vector
with open('vectors.txt') as f:
    vectorlist = []
    vectorlength = 0
    for line in f:
        vector = list(line.strip().split(','))
        print(vector)
        intvector = ([int(e) for e in vector])
        vectorlength = len(intvector)
        print(vectorlength)
        newvector = Vector(*intvector)
        print(newvector)
        vectorlist.append(newvector)

finalvectorlist = [0] * vectorlength
print(finalvectorlist)
finalvectorlist = Vector(*finalvectorlist)

for v in vectorlist:
    finalvectorlist = finalvectorlist.add(v)

print(finalvectorlist)
