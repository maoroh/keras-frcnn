from annotation_generator import AnnotationFileGenerator
from image_dict_creator import ImagesDictCreator
import cv2


def main():
    parser = AnnotationFileGenerator(path_to_annotations_folder = './dataset/CARPK_devkit/data/Annotations',images_path = './dataset/CARPK_devkit/data/Images/',train_file_path = './dataset/CARPK_devkit/data/ImageSets/train.txt')
    parser.generate()
    print ('Annotation file saved in data/train.txt')
    basicParser = ImagesDictCreator(path_to_dataset_folder='./dataset/CARPK_devkit/data')
    dict = basicParser.parseAll()
    print ('Dictionary created!')

if __name__ == '__main__':
    main()