import pytest
from pytest_mock import mocker  # Import mocker

from game.entities.snake import Snake
from game.utilities.vector import Vector as V


def test_initialization():
    snake = Snake()
    assert snake.head_pos == V.ZERO
    assert snake.head_dir == V.RIGHT
    assert snake.body == [V.ZERO, V.ZERO - V.RIGHT, V.ZERO - V.RIGHT * 2]
    assert snake.speed == 1
    assert snake.color == (0, 255, 0)
    assert not snake.growing


def test_movement():
    snake = Snake()
    initial_head_pos = snake.head_pos
    snake.move()
    assert snake.head_pos == initial_head_pos + snake.head_dir * snake.speed
    assert len(snake.body) == 3


def test_grow():
    snake = Snake()
    initial_length = len(snake.body)
    snake.grow()
    snake.move()
    assert len(snake.body) == initial_length + 1
    assert not snake.growing


def test_change_direction():
    snake = Snake()
    snake.change_direction(V.UP)
    assert snake.head_dir == V.UP
    snake.change_direction(V.DOWN)
    assert snake.head_dir == V.UP


def test_collision_with_bounds():
    snake = Snake()

    snake.head_pos = V(-1, 0)
    assert snake.check_collision_with_bounds(10, 10)
    snake.head_pos = V(0, -1)
    assert snake.check_collision_with_bounds(10, 10)

    snake.head_pos = V(10, 0)
    assert snake.check_collision_with_bounds(10, 10)
    snake.head_pos = V(0, 10)
    assert snake.check_collision_with_bounds(10, 10)


def test_collision_with_self():
    snake = Snake()
    snake.body[0] = snake.body[1]
    assert snake.check_collision_with_self()

    # No collision
    snake = Snake()
    assert not snake.check_collision_with_self()


def test_draw():
    snake = Snake()
    screen_mock = pytest.mock.Mock()
    snake.draw(screen_mock)
    assert screen_mock.method_name.call_count == len(snake.body)
