

import glob

read_files = glob.glob("*.txt")

with open("IIO_FMCOMMS5_relative_phase_offsets.txt", "wb") as outfile:
    for f in read_files:
        with open(f, "rb") as infile:
            outfile.write(infile.read())
