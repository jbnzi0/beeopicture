#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import cv2

file = cv2.imread('annona_reticulata.jpg')

flipVertical = cv2.flip(file, 0)
flipHorizontal = cv2.flip(file, 1)
flipBoth = cv2.flip(file, -1)

cv2.imshow('Original image', file)
cv2.imshow('Flipped vertical image', flipVertical)
cv2.imshow('Flipped horizontal image', flipHorizontal)
cv2.imshow('Flipped both image', flipBoth)


cv2.waitKey(0)
cv2.destroyAllWindows()