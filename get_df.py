# -*- coding: utf-8 -*-
"""
Created on Thu Apr  8 17:13:35 2021

@author: Ahmad Abd Elhameed
"""

import glassdoor_scraper as gs
import pandas as pd
import sys

path = webdriver.Chrome("C:/Users/Ahmad Abd Elhameed/ds_salary_project/chromedriver.exe")

df = gs.get_jobs("Data Scientist",15,False,path,15)

