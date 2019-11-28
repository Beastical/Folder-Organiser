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
        print('init',master)
        filters =  self.getFilters(map)
        # Set default folder
        os.chdir(path)
        # Traverse source path
        self.findFiles(filters)

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

    def getFilters(selef,map):
        print('Generating filters')
        fltrs = {}
        # Get the filter list and folders
        for folder_name in map:
            values = map[folder_name]
            values = values.values()
            folder_name = os.path.join(path,folder_name)
            print(folder_name)
            fltrs[folder_name] = values
        print('Filters ->',fltrs)
        return fltrs

    def moveFiles(self,src,trg):
        dest = shutil.move(src, trg)
        print('Moved to ->',dest)


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



    def findFiles(self,fltrs):
        print('Find files')
        # Traverse and check for files
        for dir,subdir,file in os.walk(src_path):
            for f in file:
                for folders in fltrs:
                    print(folders,'fltrs',fltrs[folders])
                    print(f)
                    key_list = fltrs[folders]
                    print([ele for ele in key_list if (str(ele) in f)])
                    if([ele for ele in key_list if (str(ele) in f)]):
                        src_file_path = os.path.join(dir,f)
                        trg_file_path = os.path.join(path,folders)
                        self.moveFiles(src_file_path,trg_file_path)

# print([ele for ele in m if(ele in f)])

if __name__ == '__main__':
    org = FolderOrganizer()
