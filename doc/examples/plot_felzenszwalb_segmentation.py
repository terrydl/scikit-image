"""
=================================================
Felzenszwalb's efficient graph based segmentation
=================================================

This fast 2d image segmentation algorithm, proposed in [1]_ is popular in the
computer vision community. It is often used to extract "superpixels", small
homogeneous image regions, which build the basis for further processing.

The algorithm has a single ``scale`` parameter that influences the segment
size. The actual size and number of segments can vary greatly, depending on
local contrast.

.. [1] Efficient graph-based image segmentation, Felzenszwalb, P.F. and
       Huttenlocher, D.P.  International Journal of Computer Vision, 2004
"""
print __doc__

import matplotlib.pyplot as plt
import numpy as np

from skimage.data import lena
from skimage.segmentation import felzenszwalb_segmentation
from skimage.util import img_as_float

img = img_as_float(lena())
segments = felzenszwalb_segmentation(img, scale=1)
segments = np.unique(segments, return_inverse=True)[1].reshape(img.shape[:2])

print("number of segments: %d" % len(np.unique(segments)))


fig, (ax_org, ax_sp, ax_mean) = plt.subplots(1, 3)
ax_org.set_title("original")
ax_org.imshow(img, interpolation='nearest')
ax_org.axis("off")

ax_sp.set_title("superpixels")
ax_sp.imshow(segments, interpolation='nearest', cmap=plt.cm.prism)
ax_sp.axis("off")

colors = [np.bincount(segments.ravel(), img[:, :, c].ravel()) for c in
        xrange(img.shape[2])]
counts = np.bincount(segments.ravel())
colors = np.vstack(colors) / counts
ax_mean.set_title("mean color")
ax_mean.imshow(colors.T[segments], interpolation='nearest')
ax_mean.axis("off")
fig.subplots_adjust(wspace=0.02, hspace=0.02, top=0.9,
                    bottom=0.02, left=0.02, right=0.98)
plt.show()
