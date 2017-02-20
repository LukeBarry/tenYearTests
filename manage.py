import os
from flask.ext.script import Manager
from form import app
from form.database import session, Entry
import csv
import psycopg2
import re
from form.database import session, Entry

manager = Manager(app)

@manager.command
def run():
    port = int(os.environ.get('PORT', 8080))
    app.run(host='0.0.0.0', port=port)
    
@manager.command
def importdata():
    with open('pssa10year.csv') as csvfile:
        for row in csv.DictReader(csvfile):
            school_score = Entry()
            school_score.Subject = row['Subject']
            school_score.PASecureID = row['PASecureID']
            school_score.state_subject_year = row['state_subject_year']
            school_score.Local_Student_ID = row['Local_Student_ID']
            school_score.PVAAS = row['PVAAS']
            school_score.Grade = row['Grade']
            school_score.Tested_Year = row['Tested_Year']
            school_score.PASA_Record = row['PASA_Record']
            school_score.Ethnicity_Code = row['Ethnicity_Code']
            school_score.IEP = row['IEP']
            school_score.Economically_Disadvantaged = row['Economically_Disadvantaged']
            school_score.Historically_Underperforming_Subgroup = row['Historically_Underperforming_Subgroup']
            school_score.Scaled_Score = row['Scaled_Score']
            school_score.Performance_Level_Code = row['Performance_Level_Code']
            school_score.Performance_Level_Name = row['Performance_Level_Name']
            school_score.Total_Raw_Score = row['Total_Raw_Score']
            school_score.MultipleChoice_Raw_Score = row['MultipleChoice_Raw_Score']
            school_score.OpenEnded_Raw_Score = row['OpenEnded_Raw_Score']
            school_score.Reporting_Category_1_Raw_Score = row['Reporting_Category_1_Raw_Score']
            school_score.Anchor_1_1 = row['Anchor_1_1']
            school_score.Anchor_1_2 = row['Anchor_1_2']
            school_score.Anchor_1_3 = row['Anchor_1_3']
            school_score.Anchor_1_4 = row['Anchor_1_4']
            school_score.Reporting_Category_2_Raw_Score = row['Reporting_Category_2_Raw_Score']
            school_score.Anchor_2_1 = row['Anchor_2_1']
            school_score.Anchor_2_2 = row['Anchor_2_2']
            school_score.Anchor_2_3 = row['Anchor_2_3']
            school_score.Anchor_2_4 = row['Anchor_2_4']
            school_score.Reporting_Category_3_Raw_Score = row['Reporting_Category_3_Raw_Score']
            school_score.Anchor_3_1 = row['Anchor_3_1']
            school_score.Anchor_3_2 = row['Anchor_3_2']
            school_score.Anchor_3_3 = row['Anchor_3_3']
            school_score.Anchor_3_4 = row['Anchor_3_4']
            school_score.Reporting_Category_4_Raw_Score = row['Reporting_Category_4_Raw_Score']
            school_score.Anchor_4_1 = row['Anchor_4_1']
            school_score.Anchor_4_2 = row['Anchor_4_2']
            school_score.Anchor_4_3 = row['Anchor_4_3']
            school_score.Anchor_4_4 = row['Anchor_4_4']
            school_score.Reporting_Category_5_Raw_Score = row['Reporting_Category_5_Raw_Score']
            school_score.Anchor_5_1 = row['Anchor_5_1']
            school_score.Anchor_5_2 = row['Anchor_5_2']
            school_score.Anchor_5_3 = row['Anchor_5_3']
            school_score.Anchor_5_4 = row['Anchor_5_4']
            school_score.Reporting_Category_6_Raw_Score = row['Reporting_Category_6_Raw_Score']
            school_score.Anchor_6_1 = row['Anchor_6_1']
            school_score.Anchor_6_2 = row['Anchor_6_2']
            school_score.Anchor_6_3 = row['Anchor_6_3']
            school_score.Anchor_6_4 = row['Anchor_6_4']
            school_score.Reporting_Category_7_Raw_Score = row['Reporting_Category_7_Raw_Score']
            school_score.Anchor_7_1 = row['Anchor_7_1']
            school_score.Anchor_7_2 = row['Anchor_7_2']
            school_score.Anchor_7_3 = row['Anchor_7_3']
            school_score.Anchor_7_4 = row['Anchor_7_4']
            school_score.Reporting_Category_8_Raw_Score = row['Reporting_Category_8_Raw_Score']
            school_score.Anchor_8_1 = row['Anchor_8_1']
            school_score.Anchor_8_2 = row['Anchor_8_2']
            school_score.Anchor_8_3 = row['Anchor_8_3']
            school_score.Anchor_8_4 = row['Anchor_8_4']
            school_score.Reporting_Category_9_Raw_Score = row['Reporting_Category_9_Raw_Score']
            school_score.Anchor_9_1 = row['Anchor_9_1']
            school_score.Anchor_9_2 = row['Anchor_9_2']
            school_score.Anchor_9_3 = row['Anchor_9_3']
            school_score.Anchor_9_4 = row['Anchor_9_4']
            school_score.Reporting_Category_10_Raw_Score = row['Reporting_Category_10_Raw_Score']
            school_score.Anchor_10_1 = row['Anchor_10_1']
            school_score.Anchor_10_2 = row['Anchor_10_2']
            school_score.Anchor_10_3 = row['Anchor_10_3']
            school_score.Anchor_10_4 = row['Anchor_10_4']
            school_score.Reporting_Category_1_Strength_Profile = row['Reporting_Category_1_Strength_Profile']
            school_score.Reporting_Category_2_Strength_Profile = row['Reporting_Category_2_Strength_Profile']
            school_score.Reporting_Category_3_Strength_Profile = row['Reporting_Category_3_Strength_Profile']
            school_score.Reporting_Category_4_Strength_Profile = row['Reporting_Category_4_Strength_Profile']
            school_score.Reporting_Category_5_Strength_Profile = row['Reporting_Category_5_Strength_Profile']
            school_score.Reporting_Category_6_Strength_Profile = row['Reporting_Category_6_Strength_Profile']
            school_score.Reporting_Category_7_Strength_Profile = row['Reporting_Category_7_Strength_Profile']
            school_score.Reporting_Category_8_Strength_Profile = row['Reporting_Category_8_Strength_Profile']
            school_score.Reporting_Category_9_Strength_Profile = row['Reporting_Category_9_Strength_Profile']
            school_score.Reporting_Category_10_Strength_Profile = row['Reporting_Category_10_Strength_Profile']
            school_score.Gender = row['Gender']
            school_score.Title_I = row['Title_I']
            school_score.enrolled_after_Oct_1st = row['enrolled_after_Oct_1st']
            school_score.enrolled_between_Octobers = row['enrolled_between_Octobers']
            
            session.add(school_score)   
            session.commit()        
        

    

if __name__ == "__main__":
    manager.run()