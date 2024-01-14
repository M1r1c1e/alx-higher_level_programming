#!/usr/bin/python3
"""Defines a rectangle class."""
from models.base import Base

class Rectangle(Base):
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        self._validate_positive_integer("width", value)
        self._width = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        self._validate_positive_integer("height", value)
        self._height = value

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        self._validate_non_negative_integer("x", value)
        self._x = value

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, value):
        self._validate_non_negative_integer("y", value)
        self._y = value

    def _validate_positive_integer(self, name, value):
        if not isinstance(value, int) or value <= 0:
            raise ValueError(f"{name} must be a positive integer")

    def _validate_non_negative_integer(self, name, value):
        if not isinstance(value, int) or value < 0:
            raise ValueError(f"{name} must be a non-negative integer")

    def area(self):
        return self.width * self.height

    def display(self):
        if self.width == 0 or self.height == 0:
            print("")
            return

        for _ in range(self.y):
            print("")

        for _ in range(self.height):
            print(" " * self.x + "#" * self.width)

    def update(self, *args, **kwargs):
        if args:
            self._update_from_args(args)
        elif kwargs:
            self._update_from_kwargs(kwargs)

    def _update_from_args(self, args):
        attrs = ["id", "width", "height", "x", "y"]
        for i, arg in enumerate(args):
            setattr(self, attrs[i], arg)

    def _update_from_kwargs(self, kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    def to_dictionary(self):
        return {
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y
        }

    def __str__(self):
        return f"[Rectangle] ({self.id}) {self.x}/{self.y} - {self.width}/{self.height}"

