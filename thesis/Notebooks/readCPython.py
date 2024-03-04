import numpy as np
def load_C_output(filename, oh=False):
    """Open the file as a byte string

    Positional Arguments:
        filename -- path to binary file to read
        oh -- only reaturn the header (saves load time)
    Returns -> state:
        state -- 2D Numpy array containing [xi, theta, dtheta/dxi]
        metadata -- dictionary of metadata extracted from the dump file

    """
    with open(filename, 'rb') as f:
        body = False
        metadata = dict()
        # read until the body (binary string) is reached
        while not body:
            # Read lines until the header is over
            line = f.readline()
            # parse bytes to utf-8 encoded text
            line = line.decode("utf-8").rstrip().lstrip()
            if 'BODY' in line:
                body = True
            else:
                # Select only the header lines
                if line.startswith("#"):
                    # define key value pair
                    data = line[2:].split(':')
                    metadata[data[0]] = float(data[1])
        if not oh:
            # read the remaning bytes of the file after the header is over
            contents = f.read()
    if not oh:
        # Read the bytes as a c type double
        state = np.frombuffer(contents, dtype=np.float64)

        # Reshape to the known shape of the data (a 2D 3xn list)
        # Using totalsize = 3*n, we know total size so we can
        # find n
        state = state.reshape(3, int(state.shape[0]/3))
    else:
        state = None
    return state, metadata
