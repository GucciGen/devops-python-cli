"""Простий CLI-скрипт із перевіркою прямого запуску."""

import sys


def main() -> None:
    if "--help" in sys.argv[1:] or "-h" in sys.argv[1:]:
        print("Використання: python src/sys_tool.py [--help]")
    else:
        print("командна строка")


if __name__ == "__main__":
    main()
