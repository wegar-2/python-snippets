import sys
import os


def main():
    print("os.getcwd(): ", os.getcwd())
    for key_, val_ in sys.modules.items():
        print(f"{key_}: {val_}")
    print("\n\n\n")
    print(sys.modules[__name__])


if __name__ == "__main__":
    main()