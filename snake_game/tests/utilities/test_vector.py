from math import isclose, radians, cos, sin
from game.utilities.vector import Vector

TOLERANCE = 1e-9


def test_str_representation():
    v = Vector(1, 2)
    assert str(v) == "(1, 2)"


def test_addition():
    v1 = Vector(1, 2)
    v2 = Vector(3, 4)
    result = v1 + v2
    assert result == Vector(4, 6)


def test_subtraction():
    v1 = Vector(1, 2)
    v2 = Vector(3, 4)
    result = v1 - v2
    assert result == Vector(-2, -2)


def test_multiplication():
    v1 = Vector(2, 3)
    result = v1 * 2
    assert result == Vector(4, 6)


def test_truedivision():
    v1 = Vector(4, 6)
    result = v1 / 2
    assert result == Vector(2, 3)


def test_floordivision():
    v1 = Vector(4, 6)
    result = v1 // 2
    assert result == Vector(2, 3)


def test_equality():
    v1 = Vector(1, 2)
    v2 = Vector(1, 2)
    assert v1 == v2


def test_inequality():
    v1 = Vector(1, 2)
    v2 = Vector(3, 4)
    assert v1 != v2


def test_dot_product():
    v1 = Vector(1, 2)
    v2 = Vector(3, 4)
    assert v1.dot(v2) == 11


def test_distance_to():
    v1 = Vector(1, 2)
    v2 = Vector(4, 6)
    assert isclose(v1.distance_to(v2), 5, rel_tol=TOLERANCE)


def test_length():
    v1 = Vector(3, 4)
    assert isclose(v1.length, 5, rel_tol=TOLERANCE)


def test_length_squared():
    v1 = Vector(3, 4)
    assert v1.length_squared == 25


def test_normalize():
    v1 = Vector(3, 4)
    result = v1.normalize()
    assert isclose(result.length, 1, rel_tol=TOLERANCE)

    v_zero = Vector(0, 0)
    result_zero = v_zero.normalize()
    assert result_zero == Vector(0, 0)


def test_rotate():
    v1 = Vector(1, 0)
    angle_degrees = 90
    theta = radians(angle_degrees)
    expected_result = Vector(cos(theta), sin(theta))
    assert isclose(
        v1.rotate(angle_degrees).x, expected_result.x, rel_tol=TOLERANCE
    ) and isclose(v1.rotate(angle_degrees).y, expected_result.y, rel_tol=TOLERANCE)


def test_perpendicular():
    v1 = Vector(1, 2)
    assert v1.perpendicular() == Vector(-2, 1)


def test_clamp():
    v1 = Vector(5, 10)
    assert v1.clamp(0, 7) == Vector(5, 7)


def test_lerp():
    v1 = Vector(1, 2)
    v2 = Vector(3, 4)
    result = Vector.lerp(v1, v2, 0.5)
    assert result == Vector(2, 3)


def test_directional_constants():
    assert Vector.UP == Vector(0, -1)
    assert Vector.DOWN == Vector(0, 1)
    assert Vector.LEFT == Vector(-1, 0)
    assert Vector.RIGHT == Vector(1, 0)
    assert Vector.ZERO == Vector(0, 0)
