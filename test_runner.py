import unittest
from driver_file import Driver
import time
from common_util import commonUtil
import pytest
import logging

'''
to run 
pytest -v -s --html=report2.html --self-contained-html test_runner.py
'''
class test_runner(unittest.TestCase):

    def setUp(self):
        self.driver = Driver()
        #the app will be opened for every test case


    @pytest.mark.second
    def test_two(self):
        #we again start the app and click app
        commonUtil.click(self, 'App', 'xpath')
        #then click ActionBar
        commonUtil.click(self, 'ActionBar', 'id')
        #click Display Options
        commonUtil.click(self, 'DisplayOptions', 'xpath')
        check = commonUtil.get_data(self, 'android.widget.TextView')
        '''
        the logic i have used is we use android.widget.TextView since it starts from the top at the start
        it will get the title. After we click the hide title the data which is collected is from the 
        drop down present at the bottom. we asster and check the toggle functionality in this way.
        '''
        commonUtil.click(self, 'DisplayShowTitle', 'id')
        check1 = commonUtil.get_data(self, 'android.widget.TextView')
        self.assertNotEqual(check,check1)
        commonUtil.click(self, 'DisplayShowTitle', 'id')
        check2 = commonUtil.get_data(self, 'android.widget.TextView')
        self.assertEqual(check,check2)
        time.sleep(3)

    @pytest.mark.first
    def test_one(self):
        #the app is opened
        commonUtil.click(self, 'animation', 'xpath')
        #animation button clicked
        commonUtil.click(self, 'Hide-Show Animations', 'xpath')
        #Hide-Show Animations button clicked
        commonUtil.click(self, 'Button0', 'xpath')
        #there are 4 button and we will click on button sto hide them
        commonUtil.click(self, 'Button1', 'xpath')
        commonUtil.click(self, 'Button2', 'xpath')
        commonUtil.click(self, 'Button3', 'xpath')
        #after clicking on button 3 we will check if it is still present or hidden
        check_true = commonUtil.IsPresent(self, 'Button3')
        self.assertEqual(check_true, 'false')
        #since it is hidden it returns false
        commonUtil.click(self, 'AddNewButton', 'id')
        # we click show all buttons
        check_true = commonUtil.IsPresent(self, 'Button3')
        self.assertEqual(check_true, 'true')
        #now we again check and see if the button is present.

    def tearDown(self):
        self.driver.instance.quit()
        #this is called after every test case and the app closes


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(test_runner)
    unittest.TextTestRunner(verbosity=2).run(suite)