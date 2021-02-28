#Trying to create a dataframe to convert to a csv.
#Detect members in the same group, and iterate a count.

import numpy as np
import pandas as pd

myNodes = pd.read_csv(r"C:\Users\liberatorea\Desktop\Data Viz\MP\Nodes-Sheet1.csv")

#Creating lists of members for committees, in order
myNodes['Members'] = None
myNodes.iloc[0, 2] = ['Roberts, Pat (KS)',
'McConnell, Mitch (KY)',
'Boozman, John (AR)',
'Hoeven, John (ND)',
'Ernst, Joni (IA)',
'Hyde-Smith, Cindy (MS)',
'Braun, Mike (IN)',
'Grassley, Chuck (IA)',
'Thune, John (SD)',
'Fischer, Deb (NE)',
'Loeffler, Kelly (GA)',
'Stabenow, Debbie (MI)',
'Leahy, Patrick J. (VT)',
'Brown, Sherrod (OH)',
'Klobuchar, Amy (MN)',
'Bennet, Michael F. (CO)',
'Gillibrand, Kirsten E. (NY)',
'Casey, Robert P. (PA)',
'Smith, Tina (MN)',
'Durbin, Richard J. (IL)']
myNodes.iloc[1, 2] = ['Shelby, Richard C. (AL)',
'McConnell, Mitch (KY)',
'Alexander, Lamar (TN)',
'Collins, Susan M. (ME)',
'Murkowski, Lisa (AK)',
'Graham, Lindsey (SC)',
'Blunt, Roy (MO)',
'Moran, Jerry (KS)',
'Hoeven, John (ND)',
'Boozman, John (AR)',
'Capito, Shelley Moore (WV)',
'Kennedy, John (LA)',
'Hyde-Smith, Cindy (MS)',
'Daines, Steve (MT)',
'Rubio, Marco (FL)',
'Lankford, James (OK)',
'Leahy, Patrick J. (VT)',
'Murray, Patty (WA)',
'Feinstein, Dianne (CA)',
'Durbin, Richard J. (IL)',
'Reed, Jack (RI)',
'Tester, Jon (MT)',
'Udall, Tom (NM)',
'Shaheen, Jeanne (NH)',
'Merkley, Jeff (OR)',
'Coons, Christopher A. (DE)',
'Schatz, Brian (HI)',
'Baldwin, Tammy (WI)',
'Murphy, Christopher (CT)',
'Manchin, Joe (WV)',
'Van Hollen, Chris (MD)']
myNodes.iloc[2, 2] = ['Inhofe, James M. (OK)',
'Wicker, Roger F. (MS)',
'Fischer, Deb (NE)',
'Cotton, Tom (AR)',
'Rounds, Mike (SD)',
'Ernst, Joni (IA)',
'Tillis, Thom (NC)',
'Sullivan, Dan (AK)',
'Perdue, David (GA)',
'Cramer, Kevin (ND)',
'Scott, Rick (FL)',
'Blackburn, Marsha (TN)',
'Hawley, Josh (MO)',
'Reed, Jack (RI)',
'Shaheen, Jeanne (NH)',
'Gillibrand, Kirsten E. (NY)',
'Blumenthal, Richard (CT)',
'Hirono, Mazie K. (HI)',
'Kaine, Tim (VA)',
'King, Angus S. (ME)',
'Heinrich, Martin (NM)',
'Warren, Elizabeth (MA)',
'Peters, Gary C. (MI)',
'Manchin, Joe (WV)',
'Duckworth, Tammy (IL)',
'Jones, Doug (AL)']
myNodes.iloc[3, 2] = ['Crapo, Mike (ID)',
'Shelby, Richard C. (AL)',
'Toomey, Patrick J. (PA)',
'Scott, Tim (SC)',
'Sasse, Ben (NE)',
'Cotton, Tom (AR)',
'Rounds, Mike (SD)',
'Perdue, David (GA)',
'Tillis, Thom (NC)',
'Kennedy, John (LA)',
'Moran, Jerry (KS)',
'Cramer, Kevin (ND)',
'Brown, Sherrod (OH)',
'Reed, Jack (RI)',
'Menendez, Robert (NJ)',
'Tester, Jon (MT)',
'Warner, Mark R. (VA)',
'Warren, Elizabeth (MA)',
'Schatz, Brian (HI)',
'Van Hollen, Chris (MD)',
'Cortez Masto, Catherine (NV)',
'Jones, Doug (AL)',
'Smith, Tina (MN)',
'Sinema, Kyrsten (AZ)']
myNodes.iloc[4, 2] = ['Enzi, Michael B. (WY)',
'Grassley, Chuck (IA)',
'Crapo, Mike (ID)',
'Graham, Lindsey (SC)',
'Toomey, Patrick J. (PA)',
'Johnson, Ron (WI)',
'Perdue, David (GA)',
'Braun, Mike (IN)',
'Scott, Rick (FL)',
'Kennedy, John (LA)',
'Cramer, Kevin (ND)',
'Sanders, Bernard (VT)',
'Murray, Patty (WA)',
'Wyden, Ron (OR)',
'Stabenow, Debbie (MI)',
'Whitehouse, Sheldon (RI)',
'Warner, Mark R. (VA)',
'Merkley, Jeff (OR)',
'Kaine, Tim (VA)',
'Van Hollen, Chris (MD)',
'Harris, Kamala D. (CA)']
myNodes.iloc[5, 2] = ['Wicker, Roger F. (MS)',
'Thune, John (SD)',
'Blunt, Roy (MO)',
'Cruz, Ted (TX)',
'Fischer, Deb (NE)',
'Moran, Jerry (KS)',
'Sullivan, Dan (AK)',
'Gardner, Cory (CO)',
'Blackburn, Marsha (TN)',
'Capito, Shelley Moore (WV)',
'Lee, Mike (UT)',
'Johnson, Ron (WI)',
'Young, Todd (IN)',
'Scott, Rick (FL)',
'Cantwell, Maria (WA)',
'Klobuchar, Amy (MN)',
'Blumenthal, Richard (CT)',
'Schatz, Brian (HI)',
'Markey, Edward J. (MA)',
'Udall, Tom (NM)',
'Peters, Gary C. (MI)',
'Baldwin, Tammy (WI)',
'Duckworth, Tammy (IL)',
'Tester, Jon (MT)',
'Sinema, Kyrsten (AZ)',
'Rosen, Jacky (NV)']
myNodes.iloc[6, 2] = ['Murkowski, Lisa (AK)',
'Barrasso, John (WY)',
'Risch, James E. (ID)',
'Lee, Mike (UT)',
'Daines, Steve (MT)',
'Cassidy, Bill (LA)',
'Gardner, Cory (CO)',
'Hyde-Smith, Cindy (MS)',
'Alexander, Lamar (TN)',
'Hoeven, John (ND)',
'Manchin, Joe (WV)',
'Wyden, Ron (OR)',
'Cantwell, Maria (WA)',
'Sanders, Bernard (VT)',
'Stabenow, Debbie (MI)',
'Heinrich, Martin (NM)',
'Hirono, Mazie K. (HI)',
'King, Angus S. (ME)',
'Cortez Masto, Catherine (NV)']
myNodes.iloc[7, 2] = ['Barrasso, John (WY)',
'Inhofe, James M. (OK)',
'Capito, Shelley Moore (WV)',
'Cramer, Kevin (ND)',
'Braun, Mike (IN)',
'Rounds, Mike (SD)',
'Sullivan, Dan (AK)',
'Boozman, John (AR)',
'Wicker, Roger F. (MS)',
'Shelby, Richard C. (AL)',
'Ernst, Joni (IA)',
'Carper, Thomas R. (DE)',
'Cardin, Benjamin L. (MD)',
'Sanders, Bernard (VT)',
'Whitehouse, Sheldon (RI)',
'Merkley, Jeff (OR)',
'Gillibrand, Kirsten E. (NY)',
'Booker, Cory A. (NJ)',
'Markey, Edward J. (MA)',
'Duckworth, Tammy (IL)',
'Van Hollen, Chris (MD)']
myNodes.iloc[8, 2] = ['Grassley, Chuck (IA)',
'Crapo, Mike (ID)',
'Roberts, Pat (KS)',
'Enzi, Michael B. (WY)',
'Cornyn, John (TX)',
'Thune, John (SD)',
'Burr, Richard (NC)',
'Portman, Rob (OH)',
'Toomey, Patrick J. (PA)',
'Scott, Tim (SC)',
'Cassidy, Bill (LA)',
'Lankford, James (OK)',
'Daines, Steve (MT)',
'Young, Todd (IN)',
'Sasse, Ben (NE)',
'Wyden, Ron (OR)',
'Stabenow, Debbie (MI)',
'Cantwell, Maria (WA)',
'Menendez, Robert (NJ)',
'Carper, Thomas R. (DE)',
'Cardin, Benjamin L. (MD)',
'Brown, Sherrod (OH)',
'Bennet, Michael F. (CO)',
'Casey, Robert P. (PA)',
'Warner, Mark R. (VA)',
'Whitehouse, Sheldon (RI)',
'Hassan, Margaret Wood (NH)',
'Cortez Masto, Catherine (NV)']
myNodes.iloc[9, 2] = ['Risch, James E. (ID)',
'Rubio, Marco (FL)',
'Johnson, Ron (WI)',
'Gardner, Cory (CO)',
'Romney, Mitt (UT)',
'Graham, Lindsey (SC)',
'Barrasso, John (WY)',
'Portman, Rob (OH)',
'Paul, Rand (KY)',
'Young, Todd (IN)',
'Cruz, Ted (TX)',
'Perdue, David (GA)',
'Menendez, Robert (NJ)',
'Cardin, Benjamin L. (MD)',
'Shaheen, Jeanne (NH)',
'Coons, Christopher A. (DE)',
'Udall, Tom (NM)',
'Murphy, Christopher (CT)',
'Kaine, Tim (VA)',
'Markey, Edward J. (MA)',
'Merkley, Jeff (OR)',
'Booker, Cory A. (NJ)']
myNodes.iloc[10, 2] = ['Alexander, Lamar (TN)',
'Enzi, Michael B. (WY)',
'Burr, Richard (NC)',
'Paul, Rand (KY)',
'Collins, Susan M. (ME)',
'Cassidy, Bill (LA)',
'Roberts, Pat (KS)',
'Murkowski, Lisa (AK)',
'Scott, Tim (SC)',
'Romney, Mitt (UT)',
'Braun, Mike (IN)',
'Loeffler, Kelly (GA)',
'Murray, Patty (WA)',
'Sanders, Bernard (VT)',
'Casey, Robert P. (PA)',
'Baldwin, Tammy (WI)',
'Murphy, Christopher (CT)',
'Warren, Elizabeth (MA)',
'Kaine, Tim (VA)',
'Hassan, Margaret Wood (NH)',
'Smith, Tina (MN)',
'Jones, Doug (AL)',
'Rosen, Jacky (NV)']
myNodes.iloc[11, 2] = ['Johnson, Ron (WI)',
'Portman, Rob (OH)',
'Paul, Rand (KY)',
'Lankford, James (OK)',
'Romney, Mitt (UT)',
'Scott, Rick (FL)',
'Enzi, Michael B. (WY)',
'Hawley, Josh (MO)',
'Peters, Gary C. (MI)',
'Carper, Thomas R. (DE)',
'Hassan, Margaret Wood (NH)',
'Harris, Kamala D. (CA)',
'Sinema, Kyrsten (AZ)',
'Rosen, Jacky (NV)']
myNodes.iloc[12, 2] = ['Hoeven, John (ND)',
'Barrasso, John (WY)',
'Murkowski, Lisa (AK)',
'Lankford, James (OK)',
'Daines, Steve (MT)',
'Moran, Jerry (KS)',
'Udall, Tom (NM)',
'Cantwell, Maria (WA)',
'Tester, Jon (MT)',
'Schatz, Brian (HI)',
'Cortez Masto, Catherine (NV)',
'Smith, Tina (MN)']
myNodes.iloc[13, 2] = ['Graham, Lindsey (SC)',
'Grassley, Chuck (IA)',
'Cornyn, John (TX)',
'Lee, Mike (UT)',
'Cruz, Ted (TX)',
'Sasse, Ben (NE)',
'Hawley, Josh (MO)',
'Tillis, Thom (NC)',
'Ernst, Joni (IA)',
'Crapo, Mike (ID)',
'Kennedy, John (LA)',
'Blackburn, Marsha (TN)',
'Feinstein, Dianne (CA)',
'Leahy, Patrick J. (VT)',
'Durbin, Richard J. (IL)',
'Whitehouse, Sheldon (RI)',
'Klobuchar, Amy (MN)',
'Coons, Christopher A. (DE)',
'Blumenthal, Richard (CT)',
'Hirono, Mazie K. (HI)',
'Booker, Cory A. (NJ)',
'Harris, Kamala D. (CA)']
myNodes.iloc[14, 2] = ['Blunt, Roy (MO)',
'McConnell, Mitch (KY)',
'Alexander, Lamar (TN)',
'Roberts, Pat (KS)',
'Shelby, Richard C. (AL)',
'Cruz, Ted (TX)',
'Capito, Shelley Moore (WV)',
'Wicker, Roger F. (MS)',
'Fischer, Deb (NE)',
'Hyde-Smith, Cindy (MS)',
'Klobuchar, Amy (MN)',
'Feinstein, Dianne (CA)',
'Schumer, Charles E. (NY)',
'Durbin, Richard J. (IL)',
'Udall, Tom (NM)',
'Warner, Mark R. (VA)',
'Leahy, Patrick J. (VT)',
'King, Angus S. (ME)',
'Cortez Masto, Catherine (NV)']
myNodes.iloc[15, 2] = ['Rubio, Marco (FL)',
'Risch, James E. (ID)',
'Paul, Rand (KY)',
'Scott, Tim (SC)',
'Ernst, Joni (IA)',
'Inhofe, James M. (OK)',
'Young, Todd (IN)',
'Kennedy, John (LA)',
'Romney, Mitt (UT)',
'Hawley, Josh (MO)',
'Cardin, Benjamin L. (MD)',
'Cantwell, Maria (WA)',
'Shaheen, Jeanne (NH)',
'Markey, Edward J. (MA)',
'Booker, Cory A. (NJ)',
'Coons, Christopher A. (DE)',
'Hirono, Mazie K. (HI)',
'Duckworth, Tammy (IL)',
'Rosen, Jacky (NV)']
myNodes.iloc[16, 2] = ['Moran, Jerry (KS)',
'Boozman, John (AR)',
'Cassidy, Bill (LA)',
'Rounds, Mike (SD)',
'Tillis, Thom (NC)',
'Sullivan, Dan (AK)',
'Blackburn, Marsha (TN)',
'Cramer, Kevin (ND)',
'Loeffler, Kelly (GA)',
'Tester, Jon (MT)',
'Murray, Patty (WA)',
'Sanders, Bernard (VT)',
'Brown, Sherrod (OH)',
'Blumenthal, Richard (CT)',
'Hirono, Mazie K. (HI)',
'Manchin, Joe (WV)',
'Sinema, Kyrsten (AZ)']


print(myNodes)

numCom = len(myNodes['Id'])
edgeCols = ['Source', 'Target', 'Weight']
edgeIdx = [i for i in range(numCom**2)]
myEdges = pd.DataFrame(columns=edgeCols, index=edgeIdx)
print(myEdges)



#Creates the Source and Target columns for each edge
for i in range(numCom):
    for j in range(numCom):
        myEdges.iloc[i*numCom+j, 0] = myNodes.iloc[i, 0]
        myEdges.iloc[i*numCom+j, 1] = myNodes.iloc[j, 0]

#Counts the number of shared members in committees
for i in range(numCom):
    for j in range(numCom):
        temp1 = myNodes.iloc[i, 2] + myNodes.iloc[j, 2]
        temp2 = set(temp1)
        myEdges.iloc[i*numCom+j, 2] = len(temp1) - len(temp2)

#Gets rid of all self-directed edges
myEdges = myEdges[myEdges.Source != myEdges.Target]
myEdges.reset_index(drop=True, inplace=True)

#Sets all repeated edges to weight zero
initLen = len(myEdges.Weight)
for i in range(initLen-1):
    for j in range(i+1, initLen):
        curr = [myEdges.iloc[i, 0], myEdges.iloc[i, 1]]
        curr.sort()
        temp = [myEdges.iloc[j, 0], myEdges.iloc[j, 1]]
        temp.sort()
        if (curr == temp):
            myEdges.iloc[i, 2] = 0

#Removes all edges with weight zero, i.e. there are no shared representatives
myEdges = myEdges[myEdges.Weight != 0]
myEdges.reset_index(drop=True, inplace=True)

print(myEdges)

# myEdges.to_csv('Edges.csv')

#There are 136 (17 choose 2) different edges between the groups.
aveWeight = np.sum(myEdges['Weight']) / 136
print(aveWeight)
#There is an average of roughly 4 senators shared among any 2 committees.
#There are only 12 edges with a weight of 0 (i.e. 12 pairs of committees out of 136 that don't share senators. 91% of committee pairs share senators.)
#This is also known as graph density.

#Average degree of 14.588 per node. i.e. The average committee shares a senator with over 14 other committees.