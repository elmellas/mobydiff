import h5py
import matplotlib.pyplot as plt

with h5py.File("channel_field_100000.h5", "r") as f:
    u = f["un"][:]

for k in range(u.shape[2]):
    plt.figure(figsize=(6,3))
    plt.imshow(u[:, :, k], origin="lower", cmap="jet")
    plt.colorbar()
    plt.title(f"Slice {k}")
    plt.show()
