from random import shuffle
from sys import argv

def rearrange_args():
    args = argv[1:]
    shuffle(args)
    print(" ".join(args))

if __name__ == "__main__":
    rearrange_args()