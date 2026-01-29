#!/usr/bin/env python3

import sys
import os
import site

"""
Check if the user is in a Python virtual environment.
"""


def main() -> None:
    # Check if the current enviroment is isolated
    # sys.base_prefix: path to the main Python installation
    # sys.prefix: path to the current enviroment (differs if in a venv)
    if (sys.prefix != sys.base_prefix):
        print("MATRIX STATUS: Welcome to the construct")
        print("")

        print(f"Current Python: {sys.executable}")
        print(f"Virtual Environment: {os.path.basename(sys.prefix)}")

        print("")
        print("SUCCESS: You're in an isolated environment!")
        print("Safe to install packages without affecting")
        print("the global system.")
        print("")

        print("Package_installation path:")
        for path in site.getsitepackages():
            print(path)
    else:
        # User is in the global system enviroment
        print("MATRIX STATUS: You're still plugged in")
        print("")
        print(f"Current Python: {sys.executable}")
        print("Virtual Environment: None detected")
        print("")
        print("WARNING: You're in the global environment!")
        print("The machines can see everything you install.")
        print("")
        print("To enter the construct, run:")
        print("python -m venv matrix_env")
        print("source matrix_env/bin/activate # On Unix")
        print("matrix_env")
        print("Scripts")
        print("activate # On Windows")
        print("")
        print("Then run this program again.")


if __name__ == "__main__":
    main()
