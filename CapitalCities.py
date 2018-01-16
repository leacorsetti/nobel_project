#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 16 14:58:09 2018

@author: leacaterinacorsetti
"""

import json
import csv
# Load in the country JSON data
with open('countries.json') as file:
    countries = json.load(file)
    
countries_edited = []
for dictionaries in countries:
    countries_edited.append([dictionaries['name']['official'], dictionaries['capital'], dictionaries['demonym']] + dictionaries['latlng'])

with open('processed_countries.csv', 'w', newline= '') as country:
    csvwriter = csv.writer(country, delimiter=',', quotechar='"', quoting=csv.QUOTE_NONNUMERIC)
    csvwriter.writerow(['name', 'capital', 'demonym', 'lat', 'lon'])
    csvwriter.writerows(countries_edited)
    
#for dictionaries in country:
#    tmp = []
#    for entry in countries_processed:
#        tmp.append(dictionaries[entry])
        

        
## Import the JSON and CSV packages
#import json
#import csv
#
## Load in the conflict JSON data
#with open('conflict_data_full_lined.json') as file:
#    data = json.load(file)
#    
#values = []
#for dictionaries in data:
##    print(type(dictionaries['type_of_violence']))
#    if dictionaries['type_of_violence']== 2:
#        values.append([dictionaries['id'], dictionaries['relid'], dictionaries['year'], 
#        dictionaries['type_of_violence'], dictionaries['conflict_name'],
#        dictionaries['side_a'], dictionaries['side_b'], dictionaries['latitude'],
#        dictionaries['longitude'], dictionaries['region'],
#        dictionaries['deaths_a'], dictionaries['deaths_b'], 
#        dictionaries['deaths_civilians'], dictionaries['deaths_unknown']])
#                  
#    
#with open('conflict_data_processed.csv', 'w', newline='') as cvsfile:
#    csvwriter = csv.writer(cvsfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_NONNUMERIC)
#    csvwriter.writerow(['id', 'relid', 'year', 'type_of_violence', 'conflict_name', 
#                        'side_a', 'side_b', 'latitude', 'longitude', 'region', 
#                        'deaths_a', 'deaths_b', 'deaths_civilians', 'deaths_unknown'])
#    csvwriter.writerows(values)
    

# Open the output CSV file we want to write to
#with open('preprocessed_data.csv', 'w', newline='') as file1:
#    csvwriter = csv.writer(file1, delimiter=',', quotechar='"', quoting=csv.QUOTE_NONNUMERIC)
    
#    csvwriter.writerow(['Country', 'Column A', 'Column B', 'Column C', 'etc.'])
    # Actually write the data to the CSV file here.
    # You can use the same csvwriter.writerow command to output the data 
    # as is used above to output the headers
         


#
#with open('conflict_data.json') as file:
#    data = json.load(file)
#
## Open the output CSV file we want to write to
#with open('preprocessed_data.csv', 'w', newline='') as file:
#    csvwriter = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_NONNUMERIC)
#    
#    csvwriter.writerows(['name', 'capital', 'latlng', 'demonym', 'area'])
#    
#for dictionaries in country:
#    tmp = []
#    for entry in desired_key:
#        if entry in dictionaries:
#            tmp.append(dictionaries[entry])
#        else:
#            tmp.append("NULL")
    # Actually write the data to the CSV file here.
    # You can use the same csvwriter.writerow command to output the data 
    #   as is used above to output the headers.