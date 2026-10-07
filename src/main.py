import sys

def help():
    print("===== Genre Classifier =====")
    print("usage: main.py [-v | --version] [-h | --help]")
def main():
    argi = 0
    while len(sys.argv) > argi:
        if len(sys.argv) > 0:
            match sys.argv[0]:
                case "-v", "--version":
                    print("Version 0.0.1")
                    return
                # Display help then exit the program.
                case "-h", "--help":
                    help()
                    return
    


if __name__ == "__main__":
    main()