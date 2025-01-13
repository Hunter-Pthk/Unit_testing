# Import the 'unittest' module to create unit tests for your code.
import unittest

# Import the 'square' and 'double' functions from the 'mymodule' module.
from mymodule import square, double, add

class TestSquare(unittest.TestCase): 
    # Define the first test method for the 'square' function.
    # Test methods should start with the word 'test' so that the test runner recognizes them as test cases.
    def test1(self): 
        # Check that calling 'square(2)' returns 4.
        # This tests if the function correctly computes the square of 2.
        self.assertEqual(square(2), 4) # test when 2 is given as input the output is 4.
        self.assertEqual(square(3.0), 9.0)  # test when 3.0 is given as input the output is 9.0.
        self.assertNotEqual(square(-3), -9)  # test when -3 is given as input the output is not -9.
# Define a test case class for testing the 'double' function.
class TestDouble(unittest.TestCase): 
    # Define the first test method for the 'double' function.
    def test1(self): 
        # Check that calling 'double(2)' returns 4.
        self.assertEqual(double(2), 4) # test when 2 is given as input the output is 4.
        self.assertEqual(double(-3.1), -6.2) # test when -3.1 is given as input the output is -6.2.
        self.assertEqual(double(0), 0) # test when 0 is given as input the output is 0.
        
# Run all the test cases defined in the module when the script is executed.
# This will automatically discover and run all the test cases defined in the module.
class TestAdd(unittest.TestCase):
    # Method for addition function.
    def test1(self):
        self.assertEqual(add(2, 4), 6) # test when 2 and 4 is passed as input the output should be 6
        self.assertEqual(add(0, 0), 0) # test when 0 and 0 is passed as input the output should be 0
        self.assertEqual(add(2.3, 3.6), 5.9) # test when 2.3 and 3.6 is passed as input and output should be 
        self.assertEqual(add('hello', 'world'),'helloworld') # test two strings
        self.assertEqual(add(2.3000, 4.300), 6.6) # Testing inputs 2.3000 and 4.300 to give output 6.6
        self.assertNotEqual(add(-2, -2), 0) # Test when inputs are -2 and output should not be 0
        
unittest.main()
