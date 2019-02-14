# instructions
# create a vector class
# that should...
# add vectors
# scale vector
# norm or len
# dot product
# override __str__ and __repr__


class Vector:
    def __init__(self, *vector):
        self.vector = vector
        print(self.vector)
        print(self.vector)

    def add(self, *avector):
        print((x + y for x, y in zip(self.vector, avector)))
        return (Vector([x + y for x, y in zip(self.vector, avector)]))
