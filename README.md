# Election_Analysis

## Overview of Election Audit
This analysis was performed to determine the winner of the congressional election held in Jefferson, Denver and Arapahoe counties per request by Colarado board of elections. Also, the county with the highest number of votes was determined.

### Resources
Data source: election_results.csv                                                                                                                         
Software: Python 3.6.12 and Visual Studio Code 1.38.1

## Election-Audit Results
The main goal of this analysis was to determine the winner of the election and the county  that had the largest number of votes. The goal was achieved by extracting the following information: 

* Total Number of votes: **369,711**
As the first step, the total number of votes in the election was determined. The prgramme ran through each row in the entire election results file.  

* The percentage of votes and the number of Votes for each county are displayed below.

  <img width="224" alt="Screen Shot 2022-09-28 at 3 44 49 PM" src="https://user-images.githubusercontent.com/112113327/192876898-e50e02b8-a041-422d-b49b-eb66f5c69d59.png">
  
 * According to the above reults, the **Denver county** has the highest number of votes which is **306,055** out of 369,711. 
 
 * The percentage of the total votes and the number of votes for each candidate is listed bellow.
    
    <img width="298" alt="Screen Shot 2022-09-28 at 4 08 56 PM" src="https://user-images.githubusercontent.com/112113327/192879028-e9cd4a95-4bf1-4ba6-9582-e99c67add9ce.png">

  * Finally, the winning candidate, and her total number of votes and the percentage is given bellow. 

    <img width="205" alt="Screen Shot 2022-09-28 at 9 17 59 PM" src="https://user-images.githubusercontent.com/112113327/192916823-32d242db-7821-4905-a8a9-6df494fc476d.png">

## Election Audit Summary
According to the information extracted from the given data set, there are only three candidates and only three counties. However, this script can be used for any number of candidates and any number of counties without any modifications. Please make sure to check the order of the colums, and if there is any differece compared to the "election_results.csv" file, remember to update the lines 49 and 52 accordingly. 
On the ohter hand, this script can be used for even to determine candidate votes in each state in presidential election. In that case, we can change the variables and names start with "county" to "state". More importantly, please remember to update rows 49 and 52 with appropriate number.
