"""Structures that contain multiple sequences."""

import matplotlib.pyplot as plt

class DotPlot:

    def __init__(self, sequence1, sequence2):
        self._matrix = []
        for char1 in sequence1._string:
            row = []
            for char2 in sequence2._string:
                row.append(1 if char1 == char2 else 0)
            self._matrix.append(row)


    def __repr__(self):
        return f"<DotPlot ({len(self._matrix)} x {len(self._matrix[0])})>"


    def __getitem__(self, index):
        return self._matrix[index]


    @property
    def matrix(self):
        return self._matrix


    def show(self):
        plt.matshow(self._matrix)
        plt.show()
