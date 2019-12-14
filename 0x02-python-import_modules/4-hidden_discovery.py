#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    d = dir(hidden_4)
    for s in d:
        if s[0] != "_":
            print(s)
