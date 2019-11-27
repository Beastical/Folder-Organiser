import os
import numpy as np
import math
import shutil
import pandas as pd

filename = 'Mapping.csv'
path = 'C:\Users\Mentalist\Desktop\Projects\Test folder'
src_path = 'C:\Users\Mentalist\Desktop\Projects\TEST_SRC'
master =[]

class FolderOrganizer:

    def __init__(self):
        # define the Folder -> file type lists
        map,master = self.getMapping()
        # Set default folder
        os.chdir(path)
        # Traverse source path
        self.findFiles()

    def createFolder(self,dict):
        # Create folders if they do not exists
        for fol in dict:
            # Check if folder exists
            if not (os.path.isdir(os.path.join(path,fol))):
                try:
                    os.mkdir(os.path.join(path,fol))
                    print("Folder created",fol)
                except OSError:
                    print("Error occured during folder creation",fol)

    def getMapping(self):
        # Get the mappings from the csv file
        df = pd.read_csv(filename).to_dict()
        # Create folders
        self.createFolder(df)
        # Master list
        mstr = []
        for d in df :
            print(d)
            print(df[d].values())
            tmp = pd.Series(df[d].values())
            mstr = mstr + tmp[~tmp.isnull()].to_list()
        # mstr = mstr[np.logical_not(pd.isnull(mstr))]
        print('Master ->',mstr)
        return df,mstr

    # def moveFile(self,src_f,trg_f):
    #     dest = shutil.move()
    #

    def findFiles(self):
        # Traverse and check for files
        for dir,subdir,file in os.walk(src_path):
            # Go through files in the list
            for f in file:
                # Check if they match master extension list
                if(f.endswith('.mkv')):
                    print(f,'extension')


if __name__ == '__main__':
    org = FolderOrganizer()
