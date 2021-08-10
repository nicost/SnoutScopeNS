# Third party imports, installable via pip:
import numpy as np
from scipy.ndimage import zoom, rotate

# Snoutscope optical configuration (edit as needed):
M1 = 200 / 2
Mscan = 70 / 70
M2 = 5 / 357
M3 = 200 / 5
MRR = M1 * Mscan * M2
Mtot = MRR * M3
camera_px_um = 6.5
sample_px_um = camera_px_um / Mtot
tilt = np.deg2rad(30)


# Very slow but pleasing - rotates the native view to the traditional view!
def traditional_view(
        self,
        native_volume,  # native volume 3D: single volume, single channel
        scan_step_size_px):
    voxel_aspect_ratio = calculate_voxel_aspect_ratio(scan_step_size_px)
    native_volume_cubic_voxels = zoom(
        native_volume, (voxel_aspect_ratio, 1, 1))
    traditional_volume: object = rotate(
        native_volume_cubic_voxels, np.rad2deg(tilt))
    return traditional_volume


def calculate_voxel_aspect_ratio(scan_step_size_px):
    return scan_step_size_px * np.tan(tilt)
