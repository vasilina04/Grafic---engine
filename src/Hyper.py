from lib.engine.Engine import Ray, Entity, EntitiesList, Game
from lib.math.Math import Matrix, Vector, Point


class Mygame(Game):
    def get_hyperplane(self):
        class GameHyperPlane:

            def __init__(gameself, position: Point, normal: Vector):
                gameself.position = position
                gameself.normal = normal.normalize()

            def planar_rotate(gameself, inds: (int, int), angle: float):
                result = Matrix.rotate_matrix(gameself.normal.dim(), inds[0], inds[1], angle) * gameself.normal
                gameself.normal = result

            def rotate_3d(gameself, angles: (float, float, float)):
                rotation = Matrix.rotate_matrix(3, 1, 2, angles[1]) * Matrix.rotate_matrix(3, 0, 2, angles[1]) * \
                           Matrix.rotate_matrix(3, 0, 1, angles[1])
                gameself.normal = rotation * gameself.normal

            def intersection_distance(gameself, ray: Ray):
                numerator = gameself.normal % (gameself.position - ray.initpt)
                denominator = gameself.normal % ray.direction
                if denominator == 0:
                    if gameself.position == ray.initpt:
                        return 0
                    return -1
                if numerator == 0:
                    return 0
                t = - numerator / denominator
                if t < 0:
                    return -1
                x = gameself.position + ray.direction * t
                return x.lenght()
        return GameHyperPlane

    def get_hyperellipsoid(self):
        class GameHyperEllipsoid:
            def __init__(gameself, position: Point, direction: Vector, semiaxes: list[float]):
                super().__init__(position, direction, semiaxes)
                gameself.position = position
                gameself.direction = direction
                gameself.semiaxes = semiaxes

            def planar_rotate(gameself, inds: (int, int), angle: float):
                result = Matrix.rotate_matrix(gameself.direction.dim(), inds[0], inds[1], angle) * gameself.direction
                gameself.direction = result

            def rotate_3d(gameself, angles: (float, float, float)):
                rotation = Matrix.rotate_matrix(3, 1, 2, angles[1]) * Matrix.rotate_matrix(3, 0, 2, angles[1]) * \
                           Matrix.rotate_matrix(3, 0, 1, angles[1])
                gameself.direction = rotation*gameself.direction

            def intersection_distance(gameself, ray: Ray):
                numerator = gameself.direction % (gameself.position - ray.initpt)
                denominator = gameself.direction % ray.direction
                if denominator == 0:
                    if gameself.position == ray.initpt:
                        return 0
                    return -1
                if numerator == 0:
                    return 0
                t = - numerator / denominator
                if t < 0:
                    return -1
                x = gameself.position + ray.direction * t
                return x.lenght()

        return GameHyperEllipsoid

