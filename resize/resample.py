from resize import interpolation
import numpy as np

class resample:
    def resize(self, image, fx=None, fy=None, interpolation=None):
        """calls the appropriate funciton to resample an image based on the interpolation method
        image: the image to be resampled
        fx: scale along x direction (eg. 0.5, 1.5, 2.5)
        fx: scale along y direction (eg. 0.5, 1.5, 2.5)
        interpolation: method used for interpolation ('either bilinear or nearest_neighbor)
        returns a resized image based on the interpolation method
        """
        if interpolation == 'bilinear':
            return self.bilinear_interpolation(image, float(fx), float(fy))

        elif interpolation == 'nearest_neighbor':
            return self.nearest_neighbor(image, float(fx), float(fy))

    def nearest_neighbor(self, image, fx, fy):
        """resizes an image using bilinear interpolation approximation for resampling
        image: the image to be resampled
        fx: scale along x direction (eg. 0.5, 1.5, 2.5)
        fx: scale along y direction (eg. 0.5, 1.5, 2.5)
        returns a resized image based on the nearest neighbor interpolation method
        """

        # Write your code for nearest neighbor interpolation here
        # image2 = cv2.imread(image, 0)
        x, y = image.shape[:2]
        #y = image.shape[1]
        print(image.shape)
        nx = int(fx * x)
        ny = int(fy * y)
        new_image = np.zeros((int(nx), int(ny)), np.uint8)
        print(new_image.shape)
        for i in range(new_image.shape[0]):
            for j in range(new_image.shape[1]):
                ni = round((i / fx) - 1)
                nj = round((j / fy) - 1)
                new_image[i][j] = image[ni][nj]

        return new_image

    def bilinear_interpolation(self, image, fx, fy):
        """resizes an image using bilinear interpolation approximation for resampling
        image: the image to be resampled
        fx: scale along x direction (eg. 0.5, 1.5, 2.5)
        fx: scale along y direction (eg. 0.5, 1.5, 2.5)
        returns a resized image based on the bilinear interpolation method
        """

        # Write your code for bilinear interpolation here
        x, y = image.shape[:2]
        #y = image.shape[1]
        print(image.shape)
        nx = int(fx * x)
        ny = int(fy * y)
        new_image = np.zeros((int(nx), int(ny)), np.uint8)
        print(new_image.shape)
        inter = interpolation.interpolation()
        for i in range(new_image.shape[0]):
            for j in range(new_image.shape[1]):
                ni = round((i / fx) - 1)
                nj = round((j / fy) - 1)

                if (ni == 0 and nj == 0) or (ni == image.shape[0] - 1 and nj == 0) or \
                        (ni == image.shape[0] - 1 and nj == image.shape[1] - 1):
                    new_image[i][j] = image[ni][nj]

                elif ni == 0 or ni == image.shape[0] - 1:
                    new_image[i][j] = inter.linear_interpolation([nj - 1, image[ni][nj - 1]],
                                                                 [nj + 1, image[ni][nj + 1]], nj)
                elif nj == 0 or nj == image.shape[1] - 1:
                    new_image[i][j] = inter.linear_interpolation([ni - 1, image[ni - 1][nj]],
                                                                 [ni + 1, image[ni + 1][nj]], ni)
                else:
                    point11i, point11j = ni - 1, nj - 1
                    point12i, point12j = ni - 1, nj + 1
                    point21i, point21j = ni + 1, nj - 1
                    point22i, point22j = ni + 1, nj + 1

                    n1 = [point11i, point11j, image[point11i][point11j]]
                    n2 = [point12i, point12j, image[point12i][point12j]]
                    n3 = [point21i, point21j, image[point21i][point21j]]
                    n4 = [point22i, point22j, image[point22i][point22j]]
                    new_image[i][j] = inter.bilinear_interpolation(n1, n2, n3, n4, [ni, nj])

        return new_image
