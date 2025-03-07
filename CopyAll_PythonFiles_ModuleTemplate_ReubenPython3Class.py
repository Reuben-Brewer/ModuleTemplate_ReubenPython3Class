# -*- coding: utf-8 -*-

'''
Reuben Brewer, Ph.D.
reuben.brewer@gmail.com
www.reubotics.com

Apache 2 License
Software Revision A, 03/07/2025

Verified working on: Python 3.11/3.12 for Windows 10, 11 64-bit.
'''

__author__ = 'reuben.brewer'

########################################
import datetime
import os
import sys
import shutil #For copying file
import time
import traceback
########################################

########################################
import distutils #For CopyEntireDirectoryWithContents(). Both imports are needed to avoid errors in 'distutils.dir_util.copy_tree("./foo", "./bar")'
from distutils import dir_util #For CopyEntireDirectoryWithContents(). Both imports are needed to avoid errors in 'distutils.dir_util.copy_tree("./foo", "./bar")'
########################################

#######################################################################################################################
def CreateNewDirectory(directory):
    try:
        #print("CreateNewDirectory, directory: " + directory)
        if os.path.isdir(directory) == 0: #No directory with this name exists
            os.makedirs(directory)
    except:
        exceptions = sys.exc_info()[0]
        print("CreateNewDirectory ERROR, Exceptions: %s" % exceptions)
        traceback.print_exc()
#######################################################################################################################

#######################################################################################################################
def CopyEntireDirectoryWithContents(SourceDir, DestDir): #Destination directory doesn't need to exist first
    distutils.dir_util.copy_tree(SourceDir, DestDir)  # Copies the entire directoy
#######################################################################################################################

#######################################################################################################################
def getTimeStampString():

    ts = time.time()
    st = datetime.datetime.fromtimestamp(ts).strftime('%m_%d_%Y---%H_%M_%S')

    return st
#######################################################################################################################

#######################################################################################################################
def IsTheTimeCurrentlyAM():
    ts = time.time()
    hour = int(datetime.datetime.fromtimestamp(ts).strftime('%H'))
    if hour < 12:
        return 1
    else:
        return 0
#######################################################################################################################

FileWorkingDirectory = "E:\\" #Use "E:\\" if the filepath length is too long
#FileWorkingDirectory = os.getcwd() #Use "E:\\" if the filepath length is too long

AMflag = IsTheTimeCurrentlyAM()
if AMflag == 1:
    AMorPMstring = "AM"
else:
    AMorPMstring = "PM"

FileDirectoryToCreate = FileWorkingDirectory + "\\ModuleTemplate_ReubenPython3Class_PythonDeploymentFiles_" + getTimeStampString() + AMorPMstring
CreateNewDirectory(FileDirectoryToCreate)

try:
    CopyEntireDirectoryWithContents("G:\\My Drive\\CodeReuben\\ModuleTemplate_ReubenPython3Class\\InstallFiles_and_SupportDocuments", FileDirectoryToCreate + "\\InstallFiles_and_SupportDocuments")  # Copies the entire directory

    shutil.copy("G:\\My Drive\\CodeReuben\\ModuleTemplate_ReubenPython3Class\\ModuleTemplate_ReubenPython3Class.py", FileDirectoryToCreate)
    shutil.copy("G:\\My Drive\\CodeReuben\\ModuleTemplate_ReubenPython3Class\\test_program_for_ModuleTemplate_ReubenPython3Class.py", FileDirectoryToCreate)
    shutil.copy("G:\\My Drive\\CodeReuben\\ModuleTemplate_ReubenPython3Class\\ExcelPlot_CSVdataLogger_ReubenPython3Code_ModuleTemplate.py", FileDirectoryToCreate)
    shutil.copy("G:\\My Drive\\CodeReuben\\ModuleTemplate_ReubenPython3Class\\CopyAll_PythonFiles_ModuleTemplate_ReubenPython3Class.py", FileDirectoryToCreate)

    shutil.copy("G:\\My Drive\\CodeReuben\\CSVdataLogger_ReubenPython3Class\\CSVdataLogger_ReubenPython3Class.py", FileDirectoryToCreate)
    #shutil.copy("G:\\My Drive\\CodeReuben\\CSVdataLogger_ReubenPython3Class\\test_program_for_CSVdataLogger_ReubenPython3Class.py", FileDirectoryToCreate)

    shutil.copy("G:\\My Drive\\CodeReuben\\EntryListWithBlinking_ReubenPython2and3Class\\EntryListWithBlinking_ReubenPython2and3Class.py", FileDirectoryToCreate)
    #shutil.copy("G:\\My Drive\\CodeReuben\\EntryListWithBlinking_ReubenPython2and3Class\\test_program_for_EntryListWithBlinking_ReubenPython2and3Class.py", FileDirectoryToCreate)

    shutil.copy("G:\\My Drive\\CodeReuben\\LowPassFilter_ReubenPython2and3Class\\LowPassFilter_ReubenPython2and3Class.py", FileDirectoryToCreate)
    #shutil.copy("G:\\My Drive\\CodeReuben\\LowPassFilter_ReubenPython2and3Class\\test_program_for_LowPassFilter_ReubenPython2and3Class.py", FileDirectoryToCreate)

    shutil.copy("G:\\My Drive\\CodeReuben\\LowPassFilterForDictsOfLists_ReubenPython2and3Class\\LowPassFilterForDictsOfLists_ReubenPython2and3Class.py", FileDirectoryToCreate)
    #shutil.copy("G:\\My Drive\\CodeReuben\\LowPassFilterForDictsOfLists_ReubenPython2and3Class\\test_program_for_LowPassFilterForDictsOfLists_ReubenPython2and3Class.py", FileDirectoryToCreate)

    shutil.copy("G:\\My Drive\\CodeReuben\\MyPlotterPureTkinterStandAloneProcess_ReubenPython2and3Class\\MyPlotterPureTkinterStandAloneProcess_ReubenPython2and3Class.py", FileDirectoryToCreate)
    #shutil.copy("G:\\My Drive\\CodeReuben\\MyPlotterPureTkinterStandAloneProcess_ReubenPython2and3Class\\test_program_for_MyPlotterPureTkinterStandAloneProcess_ReubenPython2and3Class.py", FileDirectoryToCreate)

    shutil.copy("G:\\My Drive\\CodeReuben\\MyPrint_ReubenPython2and3Class\\MyPrint_ReubenPython2and3Class.py", FileDirectoryToCreate)
    #shutil.copy("G:\\My Drive\\CodeReuben\\MyPrint_ReubenPython2and3Class\\test_program_for_MyPrint_ReubenPython2and3Class.py", FileDirectoryToCreate)

    shutil.make_archive(FileDirectoryToCreate, 'zip', FileDirectoryToCreate)

except:
    exceptions = sys.exc_info()[0]
    print("CopyAll_PythonFiles_ModuleTemplate_ReubenPython3Class ERROR, Exceptions: %s" % exceptions)
    traceback.print_exc()

print("CopyAll_PythonFiles_ModuleTemplate_ReubenPython3Class copied all files successfully.")
