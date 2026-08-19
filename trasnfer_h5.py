#!/usr/bin/env python3

import glob
import os
import h5py
import numpy as np
import pyvista as pv

# ---------------------------------------------------------------------
# Physical domain (change if you know the real dimensions)
# ---------------------------------------------------------------------
DX = 1.0
DY = 1.0
DZ = 1.0

# ---------------------------------------------------------------------
# Convert every HDF5 file
# ---------------------------------------------------------------------
files = sorted(glob.glob("channel_field_*.h5"))

print(f"Found {len(files)} files")

for fname in files:

    print(f"Converting {fname}")

    with h5py.File(fname, "r") as f:
        p = f["pn"][:]
        u = f["un"][:]
        v = f["vn"][:]
        w = f["wn"][:]

    nx, ny, nz = p.shape

    grid = pv.ImageData(
        dimensions=(nx, ny, nz),
        spacing=(DX, DY, DZ),
        origin=(0.0, 0.0, 0.0),
    )

    grid["p"] = p.ravel(order="F")
    grid["u"] = u.ravel(order="F")
    grid["v"] = v.ravel(order="F")
    grid["w"] = w.ravel(order="F")

    velocity = np.column_stack((
        u.ravel(order="F"),
        v.ravel(order="F"),
        w.ravel(order="F")
    ))

    grid["velocity"] = velocity

    out = os.path.splitext(fname)[0] + ".vti"
    grid.save(out)

print("Done.")
