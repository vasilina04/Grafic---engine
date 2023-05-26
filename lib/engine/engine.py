from lib.math.main import *
from lib.Exception.EngineException import *
import uuid
from math import *

PRECISION = 5


class Ray:
    def __init__(self, cs, initpt, direction):
        self.cs = cs
        self.initpt = initpt
        self.direction = direction


class Identifier:
    ids = list()

    def __init__(self, value=None):
        self.value = value

        if value is None:
            self.value = Identifier.__generate__()
            Identifier.ids.append(self.value)

    @classmethod
    def __generate__(cls):
        return uuid.uuid4()

    def get_value(self):
        return self.value


class Entity:
    def __init__(self, cs: CoordinateSystem):
        self.__dict__["properties"] = set()
        self.set_property("cs", cs)
        self.set_property("identifier", Identifier())

    def get_property(self, prop: str, default):
        if prop not in self.__dict__["properties"]:
            return default

        return self.__dict__[prop]

    def set_property(self, prop: str, value: any):
        if prop == "properties":
            raise EngineExceptionEntity(EngineExceptionEntity.WRONG_TYPE)

        self.__dict__[prop] = value
        self.__dict__["properties"].add(prop)

    def remove_property(self, prop):
        if prop == "properties":
            raise EngineExceptionEntity(EngineExceptionEntity.WRONG_TYPE)

        self.__delattr__(prop)
        self.__dict__["properties"].remove(prop)

    def __getitem__(self, prop):
        return self.get_property(prop)

    def __setitem__(self, prop, value):
        self.set_property(prop, value)

    def __getattr__(self, prop):
        return self.get_property(prop)

    def __setattr__(self, prop, value):
        self.set_property(prop, value)


class EntitiesList:
    def __init__(self, entities: list):
        self.entities = entities

    def append(self, entity: Entity):
        if entity.Identifier() not in self.entities:
            self.entities.append(entity)
        else:
            raise EngineExceptionEntity(EngineExceptionEntity.HAVE_ENTITY)

    def remove(self, entity: Entity):
        self.entities.remove(entity)

    def get(self, id: Identifier):
        for entity in self.entities:
            if entity.Identifier.get_value() == id.get_value():
                return entity
        raise EngineExceptionEntity(EngineExceptionEntity.NOT_ENTITY_LIST)

    def exec(self, function):
        pass

    def __getitem__(self, id):
        return self.get(id)


class Game:
    def __init__(self, cs: CoordinateSystem, entities: EntitiesList):
        self.cs = cs
        self.entities = entities

    def run(self):
        pass

    def update(self):
        pass

    def exit(self):
        pass

    def get_entity_class(self):
        class GameEntity(Entity):
            def __init__(entityself):
                super().__init__(self.cs)
                self.entities.append(entityself)

        return GameEntity

    def get_ray_class(self):
        class GameRay(Ray):
            def __init__(entityself, pt, direction):
                super().__init__(self.cs, pt, direction)

        return GameRay

    def get_object_class(self):
        class GameObject(self.get_entity_class()):
            def __int__(entityself, position: Point, direction: Vector):
                super().__init__(entityself.cs)
                if position.dim() != direction.dim():
                    raise EngineException(VectorException.VECTOR_SIZE)

                entityself.position = position
                entityself.direction = direction.normalize()

            def move(entityself, direction: Vector):
                entityself.position += direction

            def planar_rotate(entityself, inds: (int, int), angle: float):
                result = entityself.direction * Matrix.rotate_matrix(entityself.dim, inds[0], inds[1], angle)
                entityself.set_property(result)

            def rotate_3d(entityself, angles: (float, float, float)):
                rotation = Matrix.rotate_matrix(3, 1, 2, angles[1]) * Matrix.rotate_matrix(3, 0, 2, angles[1]) * \
                      Matrix.rotate_matrix(3, 0, 1, angles[1])
                result = entityself.direction * rotation
                entityself.set_direction(result)

            def set_position(entityself, position: Point):
                entityself.set_property('Position', position)

            def set_direction(entityself, direction: Vector):
                entityself.set_property('Direction', direction.normalize())

    def get_camera_class(self):
        class GameCamera(self.get_entity_class()):
            def __init__(self, draw_distance: (float, int), fov: (float, int), vfov: (float, int) = None,
                         look_at: Point = None):
                self.fov = fov
                self.vfov = vfov
                self.look_at = look_at
                self.draw_distance = draw_distance
