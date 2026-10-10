import sys

AUDIO_PATH = "../audio"

def help():
    print("===== Genre Classifier =====")
    print("usage: main.py [-v | --version] [-h | --help] <subcommand>")


def main():
<<<<<<< Updated upstream
    argi = 1
    while len(sys.argv) > argi:
        match sys.argv[argi]:
            # Display version then exit the program
            case "-v" | "--version":
                print("Version 0.0.1")
                return
=======
    argi = 0
    l = len(sys.argv)
    while argi < l:
        argi += 1
        match sys.argv[argi]:
            # Display version then exit the program.
            case "-v" | "--version":
                print("Version 0.0.1")
                return

>>>>>>> Stashed changes
            # Display help then exit the program.
            case "-h" | "--help":
                help()
                return
<<<<<<< Updated upstream
        argi += 1
    print("Incorrect Usage!")
=======

            # Process audio
            case "process":
                do_all = False
                if argi < l:
                    match sys.argv[argi]:
                        case _:
                            pass
                
                return
            
            # Train the model
            case "train":
                if argi < l:
                    match sys.argv[argi]:
                        case _:
                            pass
                return

            case _:
                print("No subcommand given!")
                help()
                return
    print("No arguments given!")
>>>>>>> Stashed changes
    help()


if __name__ == "__main__":
    main()