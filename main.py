from lab_python_oop.rectangle import Rectangle
from lab_python_oop.circle import Circle
from lab_python_oop.square import Square


def main():
    rect = Rectangle("синего", 16, 16)

    cir = Circle("зеленого", 16)

    sq = Square("красного", 16)

    print(rect)
    print(cir)
    print(sq)


if __name__ == "__main__":
    main()
