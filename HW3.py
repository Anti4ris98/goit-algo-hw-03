import turtle
import argparse
import shutil
from pathlib import Path


def parse_argv():
    parser = argparse.ArgumentParser("Сортування картинок")
    parser.add_argument(
        "-S", 
        "--source", 
        type=Path, 
        required=True, 
        help="Папка з картинками"
    )
    parser.add_argument(
        "-O",
        "--output",
        type=Path,
        default=Path("output"),
        help="Папка з відсортованими картинками",
    )
    return parser.parse_args()


def recursive_copy(src: Path, dst: Path):
    try:
        for item in src.iterdir():
            if item.is_dir():
                recursive_copy(item, dst)
            else:
                folder = dst / item.name[:1]  # output/f
                folder.mkdir(exist_ok=True, parents=True)
                shutil.copy2(item, folder)
    except PermissionError as e:
        print(f"Помилка доступу: {e}")
    except FileNotFoundError as e:
        print(f"Файл або директорія не знайдені: {e}")
    except Exception as e:
        print(f"Несподівана помилка: {e}")

def main():
    try:
        args = parse_argv()
        print(f"Вхідні аргументи: {args}")
        recursive_copy(args.source, args.output)
    except Exception as e:
        print(f"Помилка при виконанні програми: {e}")


if __name__ == "__main__":
    main()




# def draw_koch_snowflake(order, size=300):
#     window = turtle.Screen()
#     window.bgcolor("white")

#     t = turtle.Turtle()
#     t.speed(0)
#     t.penup()
#     t.goto(-size / 2, size / 2 / 3**0.5)
#     t.pendown()

#     for _ in range(3):
#         koch_curve(t, order, size)
#         t.right(120)

#     window.mainloop()

# draw_koch_snowflake(4)