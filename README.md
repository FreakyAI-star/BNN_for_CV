# Updates



# Results on UCF-101
| Technique   |    Model     | Train Accuracy | Val Accuracy | Test Accuracy |
| ----------- | -----------  | -------- | -------- | -------- |
| RGB                     | R3D (Resnet-18)                     | 62.5 %  | 57.43 % | 59.34 % |
| Grayscale               | R3D (Resnet-18)                     | 58 % | 55 % | 57 % |
| Grayscale + sobel       | R3D (Resnet-18)                     | 65.81 % | 61.97 % | 63.27 % |
| Grayscale + laplacian   | R3D (Resnet-18)                     | 63.20 % | 59.47 % | 61.1 % |
| Grayscale + sobel       | R3D (Resnet-34)                     | 56.84 % | 52.80 % | 53.10 % |
| Grayscale + sobel       | R(2+1D)                             | 44.85 % | 45.29 % | 47.13 % |
| RGB                     | R3D (Resnet-18) pretrained          | 95.66 % | 90.18 % | 93.35 % |
| Grayscale + sobel       | R3D (Resnet-18) pretrained, freezed | 82.22 % | 78.64 % | 56.90 % |
| Grayscale + sobel       | R3D (Resnet-18) pretrained          | 90.82 % | 84.66 % | 85.07 % |
| Grayscale + sobel       | R(2+1D) pretrained                  | 75.01 % | 72.22 % | 72.83 % |
| Grayscale + sobel       | MC3_18 pretrained                   | 72.37 % | 70.26 % | 71.14 % |
| RGB                     | S3D pretrained                      | **98.98 %** | **95.73 %** | **96.70 %** |
| Grayscale + sobel       | S3D pretrained                      | **97.29 %** | **93.37 %** | **93.29 %** |

# Results on HMDB-51
| Technique   |    Model     | Train Accuracy | Val Accuracy | Test Accuracy |
| ----------- | -----------  | -------- | -------- |-------- |
| RGB      | R3D (Resnet-18)       | 29.28 % | 25.61 % | 22.81 % |
| RGB      | R3D (Resnet-18) pretrained       | 74.49 %  | 56.31 % | 23.22 % |
| Grayscale + sobel   | R3D (Resnet-18) pretrained         | 56.35 % | 44.32 % | 44.04 % |
| Grayscale + sobel   | R(2+1D) pretrained         | 40.84 % | 35.33 % | 33.50 % |
| Grayscale + sobel   | MC3_18 pretrained        | 72.20 % | 55.58 % | 56.68 % |
| RGB   | S3D pretrained        | **92.84 %** | **68.84 %** | **69.11 %** |
| Grayscale + sobel   | S3D pretrained        | **90.34 %** | **62.57 %** | **63.23 %** |


# Results on HMDB-51
| Technique   |    Model     | Average Accuracy across 3-folds |
| ----------- | -----------  | -------- |
| RGB      | R3D (Resnet-18) pretrained       | 51.34 %  |
| Grayscale + sobel   | R3D (Resnet-18) pretrained         | 48.23 % |
| Grayscale + sobel   | R(2+1D) pretrained         | 40.84 % |
| Grayscale + sobel   | MC3_18 pretrained        | 36.55 % |
| RGB   | S3D pretrained        | **76.93 %** | 
| Grayscale + sobel   | S3D pretrained        | **72.04 %** |
