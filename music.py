from PythonSrc.hdf5_getters import *

h5 = open_h5_file_read("../project/MillionSongSubset/data/A/A/A/TRAAAFD128F92F423A.h5")
duration = hdf5_getters.get_duration(h5)
# get_artist_id("../project/MillionSongSubset/data/A/A/A/+TRAAAFD128F92F423A.h5",songidx=0)
h5.close()