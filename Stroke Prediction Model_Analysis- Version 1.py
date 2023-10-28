#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep  2 17:11:53 2023

@author: susanzgiri
"""


import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df1 = pd.read_csv(r"/Users/susanzgiri/Downloads/healthcare-dataset-stroke-data 2.csv")
print(df1)


df1.isnull().sum()
df1.dropna(inplace =True)
df1.columns

df1.drop(columns = "id",inplace =True)

df1

#Patients who had stroke
stroke_yes = df1.loc[(df1.stroke == 1)]
stroke_yes

##----------------------------------------Categorizing based on Age ---------------------------
stroke_yes.nlargest(5,"age")
stroke_yes.nsmallest(5,"age")


stroke_yes.age=stroke_yes.age.astype(int)
stroke_yes

stroke_yes.loc[stroke_yes.age <=19,"Group"]="Below 19"
stroke_yes.count()

stroke_yes.loc[(stroke_yes.age >=20)&(stroke_yes.age <=45) ,"Group"]="20-45 Years"
stroke_yes

stroke_yes.loc[(stroke_yes.age >=46)&(stroke_yes.age <=65) ,"Group"]="46-65 Years"
stroke_yes.count()

stroke_yes.loc[(stroke_yes.age >=66),"Group"]="66+ Years"
stroke_yes.count()

grp1 = stroke_yes.groupby("Group").count()
grp1.index


##************Glucose level Category ******************

# Normal : less than 117
# Prediabetic : 117-137
# Diabetic : greater than 137

# stroke dataset
## 1.
Normal_gluc = stroke_yes.avg_glucose_level < 117 

stroke_yes.loc[Normal_gluc,"Remark"] ="Normal_glucose"
stroke_yes


## 2.
Prediabetic1 = stroke_yes.avg_glucose_level >=117  
Prediabetic2= stroke_yes.avg_glucose_level <=137
stroke_yes.loc[Prediabetic1 & Prediabetic2,"Remark"] ="Prediabetic"
stroke_yes

## 3.
Diabetic =stroke_yes.avg_glucose_level > 137 

stroke_yes.loc[Diabetic,"Remark"] ="Diabetic"
stroke_yes.columns

stroke_yes.Remark.unique()
stroke_yes.Remark.nunique()

grp1 = stroke_yes.groupby("Remark").count()
grp1.index
grp1.gender

#*************Heart disease and hypertension columns****************
#heart disease
stroke_yes.loc[stroke_yes.heart_disease == 1 ,"heart_disease"]="Yes"
stroke_yes.loc[stroke_yes.heart_disease == 0 ,"heart_disease"]="No"

#hypertension
stroke_yes.loc[stroke_yes.hypertension == 1 ,"hypertension"]="Yes"
stroke_yes.loc[stroke_yes.hypertension == 0 ,"hypertension"]="No"


#******************BMI Category************************************
# Underweight: BMI less than 18.5
# Normal weight: BMI 18.5 to 24.9
# Overweight: BMI 25 to 29.9

## 1.
Normal_weight1=df1.bmi>=18.5 
Normal_weight2=df1.bmi<=24.9 

df1.loc[Normal_weight1 & Normal_weight2,"Remark_bmi"] ="Normal_weight"
df1

## 2.
Underweight=df1.bmi<18.5 
df1.loc[Underweight,"Remark_bmi"] ="Underweight"
df1

## 3.
Overweight1=df1.bmi>=25 
Overweight2=df1.bmi<=29.9
df1.loc[Overweight1 & Overweight2,"Remark_bmi"] ="Overweight"
df1