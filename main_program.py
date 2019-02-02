from annotation_generator import AnnotationFileGenerator
import cv2


def main():
    parser = AnnotationFileGenerator(path_to_annotations_folder = './dataset/CARPK_devkit/data/Annotations',images_path = './dataset/CARPK_devkit/data/Images/',train_file_path = './dataset/CARPK_devkit/data/ImageSets/train.txt')
    parser.generate()


if __name__ == '__main__':
    main()