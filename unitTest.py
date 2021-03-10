import unittest
from calculateBMIProfile import CalculateBMIProfile
from analysisBMI import AnalysisBMI
from fileHandling import JsonHandle
from unitConversion import UnitConvert

class TestBMICalculator(unittest.TestCase):

    def setUp(self):
        self.height = 171
        self.weight = 96
        

    calculateTestProfile = CalculateBMIProfile()
    analysisTestBMIData = AnalysisBMI()
    jsonTestHandle = JsonHandle()
    convert = UnitConvert()


    TestDataInput = jsonTestHandle.readFile('InputData.json')
    ExpectedOutputData = jsonTestHandle.readFile('OutputDataTest.json')
    #Test BMI Updated Functions

    def test_calculateBMI(self):
        self.assertEqual(self.calculateTestProfile.calculateBMI(self.weight, self.height), 32.83)
    
    def test_calculateBMICategory(self):
        self.assertEqual(self.calculateTestProfile.calculateBMICategory(32.83), 'Moderately obese')

    def test_calculateBMIHealthRisk(self):
        self.assertEqual(self.calculateTestProfile.calculateHealthRisk(32.83), 'Medium risk')

    def test_CountOverweight(self):
        self.assertEqual(self.analysisTestBMIData.countOverweight(self.ExpectedOutputData), 1)

    def test_CountOverweight(self):
        self.assertEqual(self.analysisTestBMIData.countOverweight(self.ExpectedOutputData), 1)

    def test_cm_to_meter(self):
        self.assertEqual(self.convert.cm_to_meter(170), 1.70)


if __name__ == '__main__':
    unittest.main()
