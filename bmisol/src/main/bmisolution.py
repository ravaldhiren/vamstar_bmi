import pandas as pd
import numpy as np

def bmi(weight,hight):
    bmival = round(weight / (hight / 100) ** 2)
    return bmival

def bmi_solution(data):

    datadf = pd.read_json(data)

    bmidf = datadf.assign(BMI_Range=bmi(datadf["WeightKg"],datadf["HeightCm"]))

    bmidf["BMI_Category"] = np.select(
        [
            bmidf["BMI_Range"]<=18.4,
            bmidf["BMI_Range"].between(18.5,24.9),
            bmidf["BMI_Range"].between(25, 29.9),
            bmidf["BMI_Range"].between(30, 34.9),
            bmidf["BMI_Range"].between(35, 39.9),
            bmidf["BMI_Range"]>=40
        ],
        [
            'Underweight',
            'Normal weight',
            'Overweight',
            'Moderately obese',
            'Severely obese',
            'Very severely obese'
        ],
        default = 'Unknown'
    )

    bmidf["Health_risk"] = np.select(
        [
            bmidf["BMI_Range"]<=18.4,
            bmidf["BMI_Range"].between(18.5,24.9),
            bmidf["BMI_Range"].between(25, 29.9),
            bmidf["BMI_Range"].between(30, 34.9),
            bmidf["BMI_Range"].between(35, 39.9),
            bmidf["BMI_Range"]>=40
        ],
        [
            'Malnutrition risk',
            'Low risk',
            'Enhanced risk',
            'Medium risk',
            'High risk',
            'Very high risk'
        ],
        default = 'Unknown'
    )
    return bmidf


if __name__=='__main__':
    FinalBMI = bmi_solution('data.json')
    df = pd.read_json('data.json')
    Health_risk='Medium risk|Low risk|Enhanced risk'
    BMI_Category='Moderately obese|Normal weight|Overweight'
    assert FinalBMI.shape[0] == df.shape[0]
    assert len(FinalBMI.columns) == 6
    assert FinalBMI['Health_risk'].astype(str).str.contains(Health_risk).all()
    assert FinalBMI['BMI_Category'].astype(str).str.contains(BMI_Category).all()


