# Assignment 1 Report

1. Nearest neighbor
   -Calculated the shape of input image and used to calculate the shape of output image.
   -Used numpy.zeros to create an array of zeros.
   -Filled the arrays with intensity of input image by calculating new pixel coordinates.
   -Successfully resampled both images with scale of 0.5, 1.5, 4, 10.
   -The difference between images resampled with different scales(for eg 0.5 and 4) was visible easily.
   
2. Bilinear interpolation
   -Used nearest neighbor to find new coordinates.
   -Used if statements to create rules for cases when the points are on edges.
   -Calculated the 4 points and passed them to bilinear_interpolation function.
   -In the bilinear_interpolation function, used linear_interpolation to calculate intensity of the unknown point.
   -Successfully resampled both images with scale of 0.5, 1.5, 2.
   -The image quality around the edges after resampling was better than the images resampled using nearest neighbor.
   