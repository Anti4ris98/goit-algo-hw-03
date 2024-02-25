import turtle
import argparse
import shutil
from pathlib import Path


def parse_argv():
    parser = argparse.ArgumentParser(description="Сортування файлів за типом")
    parser.add_argument(
        "-S", 
        "--source", 
        type=Path, 
        required=True, 
        help="Шлях до вихідної директорії"
    )
    parser.add_argument(
        "-O",
        "--output",
        type=Path,
        default=Path("dist"),
        help="Шлях до директорії призначення",
    )
    return parser.parse_args()

def recursive_copy(src: Path, dst: Path):
    try:
        for item in src.iterdir():
            if item.is_dir():
                recursive_copy(item, dst)
            else:
                file_extension = item.suffix
                folder = dst / file_extension[1:]  # Remove the dot from the extension
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





# def koch_curve(t, order, size):
#     if order == 0:
#         t.forward(size)
#     else: 
#         for angle in [60, -120, 60, 0]:
#             koch_curve(t, order - 1, size / 3)
#             t.left(angle)


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

# input = int(input("Введіть рівень рекурсії >>>"))
# draw_koch_snowflake(input)