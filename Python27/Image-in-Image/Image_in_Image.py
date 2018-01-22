from PIL import Image
from numpy import array
from pylab import gray
from pylab import figure
from pylab import imshow
from pylab import axis
from pylab import show

from PCV.geometry import warp

im1 = array(Image.open('beatle.jpg').convert('L'))
im2 = array(Image.open('billboard.jpg').convert('L'))
tp = array([[264, 538, 540, 264], [40, 36, 605, 605], [1, 1, 1, 1]])
tp1 = array([[675, 826, 826, 677], [55, 52, 281, 277], [1, 1, 1, 1]])
im3 = warp.image_in_image(im1, im2, tp)
im4 = warp.image_in_image(im1, im2, tp1)

figure(1)
gray()
imshow(im3)
axis('equal')
axis('off')

figure(2)
gray()
imshow(im4)
axis('equal')
axis('off')
show()
