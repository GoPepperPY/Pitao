#!/usr/bin/env python3

from os import environ, path
import sys
import site

def main() -> None:
    if not environ.get('VIRTUAL_ENV'):
        print("MATRIX STATUS: You're still plugged in")
        print(" -> Current Python: " + sys.executable)
        print("\n Virtual Environment: None Detected")
        print("The machines can see everything you install.")

        print(  "\nTo enter the construct, run:"
                "\npython -m venv matrix_env"
                "\nsource matrix_env/bin/activate # On Unix"
                "\nmatrix_env\Scripts\activate # On Windows"
                "\nThen run this program again.")
    else:
        print("MATRIX STATUS: Welcome to the construct")
        print(" -> Current Python: " + sys.executable)
        print(" -> Virtual Environment: " + path.basename(environ.get('VIRTUAL_ENV')))
        print(  "\nSUCCESS: You're in an isolated environment!\n"
                "Safe to install packages without affecting\n"
                "the global system.")
        print("Package installation path:\n" +
              site.getsitepackages()[0])

if __name__ == "__main__":
    main()
