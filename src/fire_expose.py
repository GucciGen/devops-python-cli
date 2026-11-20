"""Надати доступ до функцій із utils.py через Python Fire."""

import fire

from utils import greet, goodbye


if __name__ == "__main__":
    fire.Fire({"greet": greet, "goodbye": goodbye})
