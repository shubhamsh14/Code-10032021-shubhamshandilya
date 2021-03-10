from fileHandling import JsonHandle
from updateBMIProfile import UpdateBMIProfile
from analysisBMI import AnalysisBMI
from unitTest import TestBMICalculator
import unittest
class BMICalculator():
    def __init__(self):
        pass

    jsonHandle = JsonHandle()
    updateProfileData = UpdateBMIProfile()
    analysisBMIData = AnalysisBMI()

    # Read Input Json File
    defaultData = jsonHandle.readFile('InputData.json')
    
    # Update data according to task 1.
    updatedData = updateProfileData.updateBMIProfile(defaultData)
    
    # Overweight count according to task 2.
    overweightCount = analysisBMIData.countOverweight(updatedData)
    print('Overweight Count : %d' %overweightCount)

    # Write Updated data to output json file
    jsonHandle.writeFile( defaultData,'OutputData.json')


    

if __name__ == '__main__':
    startBMICalculator = BMICalculator()
