# Program to Calculate BMI Profile contents such as BMI, BMI Category and BMI Health Risk

from unitConversion import UnitConvert


class CalculateBMIProfile():
    def __init__(self):
        pass
    
    convert = UnitConvert()

    def calculateBMI(self, mass, height):
        # Calculated BMI according to Formula 1
        heightInMeter = self.convert.cm_to_meter(height)
        bmi= mass/(heightInMeter**2)
        bmi=round(bmi,2)

        return bmi

    def calculateBMICategory(self, inputBMI):
        # Calculated BMI Catageory according to Table 1
        if(inputBMI <= 18.4):
            return 'Underweight'
        if((inputBMI >= 18.5) & (inputBMI <= 24.9)):
            return 'Normal weight'
        if((inputBMI >= 25) & (inputBMI <= 29.9)):
            return 'Overweight'
        if((inputBMI >= 30) & (inputBMI <= 34.9)):
            return 'Moderately obese'
        if((inputBMI >= 35) & (inputBMI <= 39.9)):
            return 'Severely obese'
        if(inputBMI >= 40) :
            return 'Very severely obese'       

    def calculateHealthRisk(self, inputBMI):
         # Calculated BMI Health Risk according to Table 1
        if(inputBMI <= 18.4):
            return 'Malnutrition risk'
        if((inputBMI >= 18.5) & (inputBMI <= 24.9)):
            return 'Low risk'
        if((inputBMI >= 25) & (inputBMI <= 29.9)):
            return 'Enhanced risk'
        if((inputBMI >= 30) & (inputBMI <= 34.9)):
            return 'Medium risk'
        if((inputBMI >= 35) & (inputBMI <= 39.9)):
            return 'High risk'
        if(inputBMI >= 40) :
            return 'Very high risk' 
