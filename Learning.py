
import os

destination_path  = r'C:\Users\91751\Desktop\script\WorkingDemoArea'
clone_command = "git clone https://github.com/divyamrai28/PythonScriptingForPomXMLchange.git" 

clone_with_path = clone_command  +" "+ destination_path
os.system(clone_with_path)

print ("\n CLONED SUCCESSFULLY.! \n")
