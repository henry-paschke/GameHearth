import numpy as np
from typing import Type
from .vector import Vector2

class Transform2:
    def __init__(self, translation: Vector2 = Vector2(), rotation: float = 0, scale: Vector2 = Vector2(1,1)) -> None:
        self.matrix = np.array([
            [ scale.x * np.cos(rotation), -scale.y * np.sin(rotation), translation.x ],
            [ scale.x * np.sin(rotation),  scale.y * np.cos(rotation), translation.y ],
            [           0,                          0,                      1        ]
        ])

    @staticmethod
    def identity() -> Type['Transform2']:
        return Transform2()

    @staticmethod
    def from_matrix(matrix: np.ndarray) -> Type['Transform2']:
        transform = Transform2()
        transform.matrix = matrix
        return transform

    @property
    def position(self) -> Vector2:
        return Vector2.from_matrix(self.matrix[:, 2:])
    
    @position.setter
    def position(self, value: Vector2) -> None:
        self.matrix[2:] = value.matrix

    @property
    def rotation(self) -> float:
        return np.arctan2(self.matrix[1, 0], self.matrix[0, 0])

    @rotation.setter
    def rotation(self, value: float) -> None:
        rotation_matrix = np.array([
            [np.cos(value), -np.sin(value)],
            [np.sin(value),  np.cos(value)]
        ])

        self.matrix[0:2, 0:2] = rotation_matrix

    @property
    def scale(self) -> Vector2:
        return Vector2(
            np.linalg.norm(self.matrix[0:2, 0]),
            np.linalg.norm(self.matrix[0:2, 1])
        )
    
    @scale.setter
    def scale(self, value: Vector2) -> None:
        self.matrix[0:2, 0] = self.matrix[0:2, 0] / np.linalg.norm(self.matrix[0:2, 0]) * value.x
        self.matrix[0:2, 1] = self.matrix[0:2, 1] / np.linalg.norm(self.matrix[0:2, 1]) * value.y
    
    def get_translated(self, vector: Vector2) -> None:
        base = np.array([
            [1, 0],
            [0, 1],
            [0, 0]
        ])
        base = np.concatenate((base, vector.matrix), axis=1)
        return Transform2.from_matrix(self.matrix @ base)
    
    def get_rotated(self, angle: float) -> None:
        base = np.array([
            [np.cos(angle), -np.sin(angle), 0],
            [np.sin(angle),  np.cos(angle), 0],
            [0, 0, 1]
        ])
        return Transform2.from_matrix(self.matrix @ base)
    
    def get_scaled(self, vector: Vector2) -> None:
        base = np.array([
            [vector.x, 0, 0],
            [0, vector.y, 0],
            [0,    0,     1]
        ])
        return Transform2.from_matrix(self.matrix @ base)
    
    def __mul__(self, other: float):
        if isinstance(other, float):
            return Transform2.from_matrix(self.matrix * other)
        else:
            raise TypeError(f"unsupported operand type(s) for *: 'Transform' and '{type(other)}'")
        
    def __truediv__(self, other: float):
        if isinstance(other, float):
            return Transform2.from_matrix(self.matrix / other)
        else:
            raise TypeError(f"unsupported operand type(s) for /: 'Transform' and '{type(other)}'")
    
    def __matmul__(self, other: Type['Transform2'] | Vector2) -> Type['Transform2'] | Vector2:
        if isinstance(other, Vector2):
            return Vector2.from_matrix(self.matrix @ other.matrix)
        elif isinstance(other, Transform2):
            return Transform2.from_matrix(self.matrix @ other.matrix)
        else:
            raise TypeError(f"unsupported operand type(s) for @: 'Transform' and '{type(other)}'")
    
    def __str__(self) -> str:
        return f"Transform(translation={self.position}, rotation={self.rotation:.2f}, scale={self.scale})"