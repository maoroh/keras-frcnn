import os
import glob
class AnnotationFileGenerator:
    def __init__(self,path_to_annotations_folder, images_path,train_file_path):
        self.path_to_annotations_folder = path_to_annotations_folder
        self.images_path = images_path
        self.train_file_path = train_file_path

    def generate(self):
        with open(self.train_file_path, 'r') as train_file:
            train_file_content = train_file.readlines()
            train_files_list = [x.strip() for x in train_file_content] 
            
        files_list = glob.glob(self.path_to_annotations_folder + '/*.txt')
        with open('./data/' + "train.txt", 'w') as converted_file:
            for f in files_list:
                with open(f,'r') as original_file:
                    file_name = os.path.basename(f).split('.')[0]
                    if file_name in train_files_list:
                       
                        for line in original_file:
                            #split the line according spaces
                            converted_file.write(self.images_path + file_name + '.png,')
                            converted_file.write(self.convert_line(line))
                            converted_file.write('\n')
                            
                            
                        

    def convert_line(self,line):
        line_split = line.strip().split(' ')
        #taking all details for the bounding box
        (x1, y1, x2, y2, class_name) = line_split
        line_print = x1+','+y1+','+x2+','+y2+','+'Car'
        return line_print + ' '

