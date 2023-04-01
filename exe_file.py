from distutils.core import setup
import py2exe

setup()

# console is used instead of windows for console Applications.
# If we also use console for window applications then console window is also show with window and
# nothing happen in vice versa.

setup(

    windows=[
        {
            "script": "iMessenger.pyw",  # Replace iMessenger.pyw with the name you want to make .exe File
            "icon_resources": [(0, "icon.ico")]  # This Line Change the icon of the .exe File
        }
    ],
)

# After this go to Command Prompt
# Go the directory where the ExeCreatorCode.py Exist
# Run the Following commands
# 1.python ExeCreatorCode.py install
# 2.python ExeCreatorCode.py py2exe
# >exe File makes with a new folder in the same directory where the ExeCreatorCode.py File Exist.


# Note if python is not recognizes as a Command then fix it by the following method
