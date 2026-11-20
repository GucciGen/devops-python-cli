"""Звичайні функції, які Python Fire зробить CLI-командами."""


def greet(name: str) -> str:
    """Повернути привітання для вказаного імені."""
    return f"Привіт, {name}!"


def goodbye(name: str) -> str:
    """Повернути прощання для вказаного імені."""
    return f"До побачення, {name}!"
