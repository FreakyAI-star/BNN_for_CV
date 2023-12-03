# Updates



# Results on UCF-101
| Technique   |    Model     | Train Accuracy | Val Accuracy | Test Accuracy |
| ----------- | -----------  | -------- | -------- | -------- |
| RGB      | R3D (Resnet-18)       | 62.5 %  | 57.43 % | 59.34 % |
| RGB      | R3D (Resnet-18) pretrained       | 95.66 % | 90.18 % | - |
| Grayscale      | R3D (Resnet-18)        | 58 % | 55 % | - |
| Grayscale + sobel   | R3D (Resnet-18)         | 65.81 % | 61.97 % | - |
| Grayscale + sobel   | R3D (Resnet-18) pretrained        | 90.82 % | 84.66 % | 85.07 % |
| Grayscale + sobel   | R3D (Resnet-18) pretrained, freezed        | 82.22 % | 78.64 % | 56.90 % |
| Grayscale + laplacian   | R3D (Resnet-18)     | 63.20 % | 59.47 % | 61.1 % |
| Grayscale + sobel   | R3D (Resnet-34)         | 56.84 % | 52.80 % | - |
| Grayscale + sobel   | R(2+1D)         | 44.85 % | 45.29 % | - |
| Grayscale + sobel   | R(2+1D) pretrained        | 75.01 % | 72.22 % | - |
| Grayscale + sobel   | MC3_18 pretrained        | 72.37 % | 70.26 % | - |
| Grayscale + sobel   | S3D pretrained         | **97.29 %** | **93.37 %** | **93.29 %** |
| RGB   | S3D pretrained         | **98.98 %** | **95.73 %** | **96.70 %** |

# Results on HMDB-51
| Technique   |    Model     | Train Accuracy | Val Accuracy | Test Accuracy |
| ----------- | -----------  | -------- | -------- |-------- |
| RGB      | R3D (Resnet-18)       | 29.28 % | 25.61 % | 22.81 % |
| RGB      | R3D (Resnet-18) pretrained       | 74.49 %  | 56.31 % | 23.22 % |
| Grayscale + sobel   | R3D (Resnet-18) pretrained         | 56.35 % | 44.32 % | 44.04 % |
| Grayscale + sobel   | R(2+1D) pretrained         | 40.84 % | 35.33 % | 33.50 % |
| Grayscale + sobel   | MC3_18 pretrained        | 72.20 % | 55.58 % | 56.68 % |
| Grayscale + sobel   | S3D pretrained        | **90.34 %** | **62.57 %** | - |
| RGB   | S3D pretrained        | ** %** | ** %** | ** %** |


# To do
- Push prediction accuracy to its limits
- VIT transformer
- Finetune pretrained Res3D
- Journal
