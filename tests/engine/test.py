from lib.engine.engine import *
from lib.Exception.EngineException import *
import pytest


class TestsEntity:
    def test_get_property_error(self=None):
        basis = VectorSpace([Vector([1, 0, 0]), Vector([0, 1, 0]), Vector([0, 0, 1])])
        entity = Entity(CoordinateSystem(basis, Point([1, 0, 0])))
        prop = "Power Up"

        with pytest.raises(EngineExceptionEntity):
            res = entity.prop