import glob
import os
class ImagesDictCreator:
    def __init__(self, path_to_dataset_folder):
        self.path_to_dataset_folder = path_to_dataset_folder
        self.parser_dict = {}
    
    def parseAll(self):
        self.parseAnnotations()
        self.parseImageSets()
        return self.parser_dict

    #Parsing the image set for each image
    def parseImageSets(self):
        #Read train.txt file
        with open(self.path_to_dataset_folder + '/ImageSets/train.txt','r') as train_file:
            t = [line[:-1] for line in train_file]
            for train_file_name in t:
                self.parser_dict[train_file_name]['imageset'] = 'train'
         #Read test.txt file       
        with open(self.path_to_dataset_folder + '/ImageSets/test.txt','r') as test_file:
            t = [line[:-1] for line in test_file]
            for train_file_name in t:
                self.parser_dict[train_file_name]['imageset'] = 'test'
       
    def parseAnnotations(self):
        #Getting all file paths
        files_list = glob.glob(self.path_to_dataset_folder + '/Annotations/*.txt')
       
        #Loop over all files
        for f in files_list :
            #Getting file name
            file_name = os.path.splitext(os.path.basename(f))[0]
    
            #init dictionary for this file
            self.parser_dict[file_name] = {}
            #open file in read mode
            with open(f,'r') as file:
                #count lines
                data = file.read()
                self.parser_dict[file_name]['count']  = len(data.split('\n')) - 1