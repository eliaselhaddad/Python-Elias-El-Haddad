from argparse import Namespace
import os, sys

os.system("cls||clear")

print(f"\n('='*30)main.py('='*30)")

# code imported from another module is exucuted when imported
import module1

# note __name__ is module1 when ran from outside of module1.py
# when module1.py is ran then __name__ = __main__


# when importing a module - a reference will be created to sys.modules
print("globals namespace")
print(globals()(module1))



print(f"\n('='*30)main.py('='*30)")
