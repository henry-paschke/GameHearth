import numpy as np
from typing import Type

"""
Represents a 2D vector with x and y components.
Internally represented as a 3x1 column matrix in homogeneous coordinates.
"""
class Vector2:
    def __init__(self, x: float = 0, y: float = 0) -> None:
        self.matrix = np.array([
            [x], 
            [y],
            [1]
        ])

    @staticmethod
    def from_matrix(matrix: np.ndarray) -> Type['Vector2']:
        return Vector2(matrix[0, 0], matrix[1, 0])

    @property
    def x(self) -> float:
        return self.matrix[0, 0]
    
    @x.setter
    def x(self, value: float) -> None:
        self.matrix[0, 0] = value
    
    @property
    def y(self) -> float:
        return self.matrix[1, 0]
    
    @y.setter
    def y(self, value: float) -> None:
        self.matrix[1, 0] = value
    
    @property
    def length(self) -> float:
        return np.linalg.norm(self.matrix[:2])
    
    @length.setter
    def length(self, value: float) -> None:
        if value != 0:
            self.matrix = self.matrix / self.length * value
        else:
            self = Vector2()
    
    @staticmethod
    def get_rotation_matrix(angle) -> np.ndarray:
        return np.array([
            [ np.cos(angle),  -np.sin(angle),  0 ],
            [ np.sin(angle),   np.cos(angle),  0 ],
            [     0,                0,         1 ]
        ])
    
    def __add__(self, other: Type['Vector2']) -> Type['Vector2']:
        sum = self.matrix + other.matrix[:2]
        sum[2,0] = 1
        return Vector2.from_matrix(sum)
    
    def __sub__(self, other: Type['Vector2']) -> Type['Vector2']:
        difference = self.matrix - other.matrix[:2]
        difference[2,0] = 1
        return Vector2.from_matrix(difference)
    
    def __mul__(self, other: Type['Vector2'] | float) -> Type['Vector2']:
        if isinstance(other, Vector2):
            result = Vector2.from_matrix(self.matrix * other.matrix)
        else:
            result = Vector2.from_matrix(self.matrix * other)
        result[2,0] = 1
        return result
        
    def __truediv__(self, other: Type['Vector2'] | float) -> Type['Vector2']:
        if isinstance(other, Vector2):
            result =  Vector2.from_matrix(self.matrix / other.matrix)
        else:
            result =  Vector2.from_matrix(self.matrix / other)
        result[2,0] = 1
        return result
        
    def rotate(self, angle: float) -> Type['Vector2']:
        return Vector2.from_matrix(np.dot(self.get_rotation_matrix(angle), self.matrix))
    
    def __repr__(self) -> str:
        return f'Vector({self.x:.2f}, {self.y:.2f})'
    
    def __str__(self) -> str:
        return f'Vector({self.x:.2f}, {self.y:.2f})'
    
    def get_normalized(self) -> Type['Vector2']:
        return Vector2.from_matrix(self.matrix / self.length)