from detector import FasterRCNNDetector
import cv2


def main():

    detector = FasterRCNNDetector(model_path='./model/cars_last_model.hdf5')

    img = cv2.imread('./datasets/CARPK_devkit/data/Images/20161225_TPZ_00440.png')
    detector.detect_on_image(img)


if __name__ == '__main__':
    main()