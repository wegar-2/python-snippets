import pathlib

def main():
    path_ = pathlib.Path(__file__).parent / "words.txt"
    print(f"path_: {path_}")

    with open(path_, mode="r") as f:
        res = f.readlines()
    num_of_lines = len(res)

    


if __name__ == "__main__":
    main()

