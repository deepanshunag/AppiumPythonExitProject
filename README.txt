The requirements for the above code to run are as follows

1. pycharm, android studio, appium server, android emulator should be installed
2. the emulator is Pixel XL with API version 25, android 7.1.1. The app API Demos is present in the emulator by 
   default
3. the code is run from the terminal by the command "pytest -v -s --html=report2.html --self-contained-html test_runner.py"
4. driver_file.py -> contains the driver and is import to test_runner
   common_util.py -> contains the methods click, get data which have been repeated multiple times
   jsonRead.py-> for reading data from the json file
   test_runner.py -> contains the test cases
   