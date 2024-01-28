# -*- coding: utf-8 -*-
"""
Created on Thu Jan 18 13:31:58 2024

@author: efiel

"""
from Truck import Truck
from HashMap import HashMap
from Package import Package
import pandas as pd

### code to read package file, initialzie hash map and populate it###### 


package_manifest_df = pd.read_csv('package_file.csv')

package_manifest = []


for i, row in package_manifest_df.iterrows():
    package_instance = Package(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7])
    package_manifest.append(package_instance)
    
hash_map_manifest = HashMap()

for package in package_manifest:
    hash_map_manifest.add(package.GetPackageId(), package)
    
###################################################################

##### Read distance table and #####################################

distance_table = pd.read_csv('Real_Distance_Table.csv', index_col=0)

#print(distance_table.loc['6351 South 900 East','HUB']) 

###################################################################

####   create the three truck instances and load them #############

truck_one = Truck()
truck_two = Truck()
truck_three = Truck()

print(truck_one.find_next_stop())

truck_one.driver_manifest.add(1, "package")

print(truck_one.find_next_stop())


####################################################################








