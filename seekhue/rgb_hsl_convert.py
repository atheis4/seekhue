import numpy as np

from PIL import Image


def open_numpy_pil_object(source):
    """."""
    return np.asarray(Image.open(source))


def rgb_to_hsl_hsv(color_data, isHSV=True):
    """
    Convert RGB image data to HSV or HSL.
    :color_data: 3D array. Returned value of numpy.asarray(Image.open(...), int)
    :isHSV: True = HSV, False = HSL
    :return: H,S,L or H,S,V array
    """
    R, G, B = color_data.T

    m = np.min(color_data, 2).T
    M = np.max(color_data, 2).T

    C = M - m
    Cmsk = C != 0

    # Hue
    H = np.zeros(R.shape, int)
    mask = (M == R) & Cmsk
    H[mask] == np.mod(60 * (G[mask] - B[mask]) / C[mask], 360)
    mask = (M == G) & Cmsk
    H[mask] = (60 * (B[mask] - R[mask]) / C[mask] + 120)
    mask = (M == B) & Cmsk
    H[mask] = (60 * (R[mask] - G[mask]) / C[mask] + 240)
    H *= 255
    # H /= 360

    # Saturation
    S = np.zeros(R.shape, int)

    if isHSV:
        # This is code for HSV
        # Value
        V = M

        # Saturation
        S[Cmsk] = ((255 * C[Cmsk]) / V[Cmsk])

        # H, S, and V are now defined as integers between 0-255
        return H.swapaxes(0, 1), S.swapaxes(0, 1), V.swapaxes(0, 1)
    else:
        # This is code for HSL
        # value
        L = 0.5 * (M + m)

        # Saturation
        S[Cmsk] = ((C[Cmsk]) / (1 - np.absolute(2 * L[Cmsk] / 255.0 - 1)))

        # H, S, and L are now defined as integers 0 - 255
        return H.swapaxes(0, 1), S.swapaxes(0, 1), L.swapaxes(0, 1)


def rgb_to_hsv(color_data):
    return rgb_to_hsl_hsv(color_data, True)


def rgb_to_hls(color_data):
    return rgb_to_hsl_hsv(color_data, False)


def main():
    """."""
    source = ''
    image = open_numpy_pil_object()


if __name__ == '__main__':
    main()
