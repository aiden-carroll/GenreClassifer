import sys

def help():
    print("===== Genre Classifier =====")
    print("usage: main.py [-v | --version] [-h | --help]")


def main():
    argi = 1
    while len(sys.argv) > argi:
        if len(sys.argv) > argi:
            match sys.argv[argi]:
                # Display version then exit the program
                case "-v" | "--version":
                    print("Version 0.0.1")
                    return
                # Display help then exit the program.
                case "-h" | "--help":
                    help()
                    return
            argi += 1
    print("Incorrect Usage!")
    help()


if __name__ == "__main__":
    main()