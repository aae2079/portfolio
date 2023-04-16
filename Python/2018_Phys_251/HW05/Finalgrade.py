#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 14 10:41:57 2018

@author: aaron_escbr
"""
Homeworks = 78
Midterm   = 55
Final     = 86.7
 


def grader(homeworks,midterm,final):
    homeworks = Homeworks *.40
    midterm   = Midterm *.30
    final     = Final*.30
    FinalGrade = homeworks + midterm + final
    return FinalGrade
def gradeScores(FinalGrade):
    if FinalGrade >= 90 and FinalGrade <= 100:
        return("You received an A")

    elif FinalGrade >= 80 and FinalGrade < 90:
        return("You received a B")

    elif FinalGrade >= 75 and FinalGrade < 80:
        return("You received a C+")
    elif FinalGrade >= 73 and FinalGrade < 75:
        return("Yo recieved a C")
    elif FinalGrade >= 70 and FinalGrade < 73:
        return ("You recieved a C-")

    elif FinalGrade >= 60 and FinalGrade < 70:
        return("You received a D")

    else:
        return("Sorry, you received an F")
        
print(gradeScores(grader(Homeworks,Midterm,Final))) #will replace with values