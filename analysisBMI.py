# Task 2: Count the total number of overweight people using ranges in the column BMI
# Category of Table 1, check this is consistent programmatically and add any other
# observations in the documentation

class AnalysisBMI():
    def __init__(self):
        pass

    def countOverweight(self, defaultData):
        count =0
        for i in range(0, len(defaultData)):
            tempPersonData = defaultData[i]
            if (tempPersonData['BMICatgeory'] == 'Overweight'):
                count = count + 1

        return count
