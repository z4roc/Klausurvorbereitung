import numpy
import numpy as np
class Mat:
    def __init__(self, mat):
        if not isinstance(mat, list):
            raise TypeError("mat must be a list")
        self.mat: np.array = numpy.array(mat)
        lens = list(map(lambda x: len(x), mat))
        if not all([i[0] != i for i in lens]):
            raise ValueError("Länge der Listen nicht gleich")
    def getrow(self, i: int):
        return self.mat[i]

    def getcol(self, i: int):
        return [v[i] for v in self.mat]





