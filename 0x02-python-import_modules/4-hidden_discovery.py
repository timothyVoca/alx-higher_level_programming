#!/usr/bin/python3
'''
Prints all names defined by the compiled module
should not execute when importedodule hidden_4.pyc
Print one name per line in alpha order
Print only names that do not start with __
Your code should not execute when imported
'''

if __name__ == "__main__":
    import hidden_4

    names = dir(hidden_4)
    for name in names:
        if name[:2] != "__":
            print(name)
