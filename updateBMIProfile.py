# Task 1 : Calculate the BMI (Body Mass Index) using Formula 1, BMI Category and Health
# risk from Table 1 of the person and add them as 3 new columns

from calculateBMIProfile import CalculateBMIProfile

class UpdateBMIProfile():
    def __init__(self):
        pass

    calculateProfile = CalculateBMIProfile()
    def updateBMIProfile(self, defaultData):
        for i in range(0, len(defaultData)):
            tempPersonData = defaultData[i]
            tempPersonHeight = tempPersonData['HeightCm']
            tempPersonWeight = tempPersonData['WeightKg']
            tempPersonData['BMI'] = self.calculateProfile.calculateBMI(tempPersonWeight, tempPersonHeight)
            tempPersonData['BMICatgeory'] = self.calculateProfile.calculateBMICategory(tempPersonData['BMI'])
            tempPersonData['BMIHealthRish'] = self.calculateProfile.calculateHealthRisk(tempPersonData['BMI'])
            defaultData[i] = tempPersonData

        return defaultData
