import sys, csv
import os
from math import *

def Calculate_Grade_Stats(studentList,passThreshold=50):
    total_Score=0
    passed_students=[]
    for s in studentList:
        score=float(s['score'])
        if score>=passThreshold:
            passed_students.append(s['name'])
        total_Score+=score
    avg=total_Score/len(studentList) if len(studentList)>0 else 0.0
    return {'average':avg,'passed':passed_students,'total_count':len(studentList)}

def Print_Summary( stats_dict,courseName="Python 101"):
    print("=== Summary for " + courseName + " ===")
    print("Average Score: " + str(stats_dict['average']))
    print("Passed Students: " + ", ".join(stats_dict['passed']))

data = [{'name':'Charlie','score':'85.5'},{'name':'River','score':'42.0'},{'name':'Jordan','score':'68.0'}]
res = Calculate_Grade_Stats(data)
Print_Summary(res)