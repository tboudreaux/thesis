from readCPython import load_C_output
import numpy as np
import argparse


def find_root(x, y):
    """ Find the root of y(x) return both x and y(x)~0
        Based on the smallest absolute value of y(x)

    Positional Arguments:
        x -- Independet Variable list
        y -- Depended Variable list (parallel to x)
    Returns -> (x[y(x)~0], y(x)~0):
        x[y(x)~0] -- the indepent location of the root
        y(x)~0 -- The actual closest value to the root
    """
    idx = (np.abs(y)).argmin()
    return x[idx], y[idx]


if __name__ == '__main__':
    # Add an argument Parser
    parser = argparse.ArgumentParser(description='Extract the root of a given solution')
    parser.add_argument('path', metavar='i', type=str, help="Files to extract Xi1")

    args = parser.parse_args()

    # Load Data
    state, metadata = load_C_output(args.path)
    x1approx, thetax1approx = find_root(state[0], state[1])

    # Print to standard output
    print(x1approx, thetax1approx)



