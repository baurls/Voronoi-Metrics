import numpy as np
#import global_code

#...........................................................................................
#                                      Loading logic
#...........................................................................................

def save_matrix(datafile, M):
    return np.savetxt(datafile, M)

def save_single_value(full_path, value):
    return np.savetxt(full_path, np.array([value]))