from lib.engine.engine import *
from lib.Exception.EngineException import *
import pytest


class TestRay:
    def testInitial(self):
        basis = VectorSpace([Vector([1, 0, 0]), Vector([0, 1, 0]), Vector([0, 0, 1])])
        point = Point([0, 0, 0])
        coordinate = CoordinateSystem(point, basis)
        vector = Vector([1, 1, 1])
        ray = Ray(coordinate, point, vector)

        act = isinstance(ray, Ray)

        assert act


class TestEntity:
    def testInitial(self):
        point = Point([[0], [1], [0]])
        vecspace = VectorSpace([Vector([1, 0, 0]), Vector([0, 1, 0]), Vector([0, 0, 1])])
        cs = CoordinateSystem(point, vecspace)
        a = Entity(cs)

        act = isinstance(a, Entity)

        assert act

    def testpropExeption(self):
        point = Point([[0], [1], [0]])
        vecspace = VectorSpace([Vector([1, 0, 0]), Vector([0, 1, 0]), Vector([0, 0, 1])])
        cs = CoordinateSystem(point, vecspace)
        entity = Entity(cs)
        prop = "Coordinate"

        with pytest.raises(EngineExceptionEntity):
            act = entity.prop

    def testpropety(self):
        point = Point([[0], [1], [0]])
        vecspace = VectorSpace([Vector([1, 0, 0]), Vector([0, 1, 0]), Vector([0, 0, 1])])
        cs = CoordinateSystem(point, vecspace)
        a = Entity(cs)
        prop = "PowerUp"
        val = "QuadShot"
        a.set_property(prop, val)

        act = ((a.get_property("PowerUp")) == "QuadShot")

        assert act