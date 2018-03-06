# Mammographic density measurement using Otsu's method

Related Document
+ [Measurement algorithm](https://drive.google.com/open?id=0B3AORUsOcrcsbWJTZTZmQWNoU0k)
+ [Mammography density](https://drive.google.com/open?id=0B3AORUsOcrcsYzVPQ3FkTU94bDA)

Resource
+ [OpenCV with Python](https://opencv-python-tutroals.readthedocs.io/en/latest/)
+ [Matplot](http://matplotlib.org/api/pyplot_api.html)
+ [Otsu Thresholding Explained](http://www.labbookpages.co.uk/software/imgProc/otsuThreshold.html)

Developer
+ [Marktrs](https://github.com/marktrs)


### Solution
___
**A) Breast Region Segmentation**

-  Step1: Calculate image histogram and find the peak of histogram

-  Step2: Use peak of histogram to binarize image

- Step3: Find max region (sum of intensity inside a region) as the breast region


**B) Gland Tissue Segmentation**

- Step1: Otsu thresholds for gland tissue segmentation

- Step2: Find glandular tissues' contours and calculate its moment and centroid

- Step3: Find pectoral muscle


**C) Calculate the mammography density and image output**
