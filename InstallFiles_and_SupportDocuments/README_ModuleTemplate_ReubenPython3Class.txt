###########################

ModuleTemplate_ReubenPython3Class

Control class TEMPLATE (including ability to hook to Tkinter GUI) for interfacing with your own hardware device.
This is the same TEMPLATE that has been used for all of the other classes in https://github.com/Reuben-Brewer?tab=repositories.

Reuben Brewer, Ph.D.

reuben.brewer@gmail.com

www.reubotics.com

Apache 2 License

Software Revision A, 03/07/2025

Verified working on:

Python 3.11/3.12.

Windows 10, 11 64-bit

99.9% sure it will also work in Raspberry Pi 4/5 and Ubuntu (all of the dependencies have been previously verified on their own).

Notes:

1. In both "ModuleTemplate_ReubenPython3Class.py" and "test_program_for_ModuleTemplate_ReubenPython3Class.py",
copy and replace "ModuleTemplate_ReubenPython3Class" and "ModuleTemplate" with your own class name.
For Example, say that your class name is "BunnyFooFoo_BigCompanyPython3Class". You would find-and-replace
"ModuleTemplate_ReubenPython3Class" with "BunnyFooFoo_BigCompanyPython3Class" and "ModuleTemplate" with "BunnyFooFoo".

###########################

########################### Python module installation instructions, all OS's

############

test_program_for_ModuleTemplate_ReubenPython3Class.py, ListOfModuleDependencies:

ModuleTemplate_ReubenPython3Class, ListOfModuleDependencies_All:['CSVdataLogger_ReubenPython3Class', 'EntryListWithBlinking_ReubenPython2and3Class', 'future.builtins', 'keyboard', 'LowPassFilter_ReubenPython2and3Class', 'LowPassFilterForDictsOfLists_ReubenPython2and3Class', 'MyPlotterPureTkinterStandAloneProcess_ReubenPython2and3Class', 'MyPrint_ReubenPython2and3Class', 'numpy', 'pexpect', 'psutil']

############

############

ExcelPlot_CSVdataLogger_ReubenPython3Code_ModuleTemplate.py, ListOfModuleDependencies_All:['pandas', 'win32com.client', 'xlsxwriter', 'xlutils.copy', 'xlwt']

pip install pywin32         #version 305.1 as of 10/17/24

pip install xlsxwriter      #version 3.2.0 as of 10/17/24. Might have to manually delete older version from /lib/site-packages if it was distutils-managed. Works overall, but the function ".set_size" doesn't do anything.

pip install xlutils         #version 2.0.0 as of 10/17/24

pip install xlwt            #version 1.3.0 as of 10/17/24

############

###########################