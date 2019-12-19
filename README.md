# CDC_Natality_Analysis

## Introduction
The Center for Disease Control and Prevention (https://www.cdc.gov/nchs/nvss/births.htm) publishes selected characteristics for all birth and pregnancy-related events yearly for independent research and analysis. This project aims to understand the non-genetic risk factors for congenital abnormalities and neonatal intensive care unit (NICU) admissions and to ultimately predict these instances. 

## Creation
This code was written by Aron Berke, Bee Kim, Paul Lee, Bettina Meier, and Ira Villar to be used for non-commercial (academic in nature) purposes.

## Layout
The Initial_Data_Processing folder contains code for transferring the original fixed width format files into a MySQL database. The .py file takes the FWF files and text copies of the data user guides as inputs, and returns CSVs. The .sql files contain various methodologies for loading the data into MySQL.

The CCHD folder contains all analysis related to cyanotic congenital heart disease. The Functions file is a central repository of all functions used in the other files (exploratory analysis and models). The NICU folder is structured in the same manner, though filenames indicate whether a model was built considering data collected post-labor vs. pre-labor only.

## Final Output
All exploratory data analysis can be found here: https://public.tableau.com/profile/bee.kim#!/vizhome/CDC2018/General

Please feel free to email us if you'd like to view a copy of the presentation associated with this project.




