import numpy as np
import cv2 as cv
import sys

def make_base_map(size, boxes, method='', save=False):
    '''
    Parameters
    ------
    - size: tuple of ints
        (height, width) or equivalent to (rows, columns)
    - boxes: list of tuples of ints
        Each tuple must be formed by four ints and represent the rectangles/boxes
        specified by the "method" parameter
        (y, x, height, width)
    - method: str
        - full: The provided rectangles are the obstacles
        - Otherwise the default option, the provided rectangles are the hallways
    - save: bool
        Defines whether to save the generated base map as an image or not, defaults
        to False.
    ------
    Returns
    - Numpy array of dimension "size" created by the provided array of boxes.
    ------
    '''
    base_map = np.zeros(size)
    fill = 255
    if method == 'full':
        base_map, fill = np.full(size, 255), 0
    for y, x, h, w in boxes:
        base_map[y:y+h, x:x+w] = fill

    if save:
        cv.imwrite('basemap.jpg', base_map)

    return base_map


def load_base_map(img_path):
    '''
    Parameters
    ------
    ------
    Returns
    ------
    '''
    pass

if __name__ == '__main__':
    size = (182, 360)
    boxes = [
        (10, 0, 20, 360),
        (152, 0, 20, 360),
        (30, 130, 122, 20),
        (30, 330, 132, 20),
    ]
    bm = make_base_map(size, boxes, save = True)
    
