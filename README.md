# US-Senate-Committees
A tableau story explaining diversity and the interconnected nature of Senate committees. Created by AJ Liberatore (liberatorea@wit.edu) and Jayden Butts (buttsj@wit.edu). This project had a focus on data collection and data visualization.

## Summary

### Goals of this Project

With this project, we aimed to give the voting American citizen, or anyone interested in the US Senate for that matter, an interactive tool which allows users to investigate the make-up of US Senate committees. We wanted our audience to be better informed and feel more comfortable with the subject of politics, enriching them with the knowledge of the power members of the Senate hold.

### Instructions

To view the Tableau story, download the provided .twbx file to your desired location on your pc. It is of note that in order to view the story and interactive dashboard themselves, a Tableau license is required.

#### Story

For the story, scroll to the story tab in the provided .twbx titled "Diversity in US Senate Committees". Click on the right arrow next to each story point to progress through the story. 

![](/Tutorial/StoryTutorial1.png)

Further instructions, such as how to interact with the demographic visualization, are included in the story. More in-depth instruction for the dashboard are below.

#### Dashboard

For the dashboard, scroll to the dashboard tab in the provided .twbx titled "Senate Representation Breakdown".

Scrolling over each individual dot in the geographic map, you are able to see a bio for a specific Senator. The size of the dot is scaled based on the number of committees and seats of power a Senator holds, and the dot is colored to their identified party.

![](/Tutorial/DashboardTutorial1.png)

If you wish to view the demographics of a specific group of committees, you can go to the middle of the dashboard and select up to 10 committees you wish to view.

![](/Tutorial/DashboardTutorial2.png)

![](/Tutorial/DashboardTutorial3.png)

Pie charts comparing the gender and race demographics of the US Senate to the US as a whole are on the right side of the dashboard. The rest is up to you from here! Play around with the dashboard a bit and see what you discover.

### Results & Discussion

With this project, it was found overall that the US Senate is not as representative of the US population as a whole as would be desired in this diverse nation. While the US is 49% male and 58% white, the Senate is 74% male and 91% white. Beyond these interesting statistics, the committee network also provided a lot of insight into the general lack of diversity in thought of the US Senate. Below is the network visualization itself.

![](/images/Committee_Network.png)

Though the viz contains some technical jargon, we may take note of the following:
* There are 136 possible pairs of committees
* There is an average of almost 4 Senators shared among any two committees
* There are only 12 committee pairs which do not share a Senator
* 91% of committee pairs share at least one Senator
* The average committee shares a Senator with over 14 other committees

Every US election, citizens have a chance for their voices to be heard. Even beyond that, we can create movements and propositions to make the Senate both more representative and efficient. Let's continue to work and make the US a country our citizens deserve!

## Data
The data we used was collected from two places. We used the [demographics and economy section of the Kaiser Family Foundation website](https://www.kff.org/state-category/demographics-and-the-economy/) for up to date US demographics, and we used the [US Senate website](https://www.senate.gov/reference/stats_and_lists.htm) to collect information about Senators and committees during the 116th United States Congress.

## Methods
Tools:
* Tableau 2020.3, to create dashboard and story points
* Gephi, to create network of committees
* VSCode, as code editor of choice
* MS Excel, to store node and edge data

Python Packages:
* Numpy, to uncover underlying stats
* Pandas, to store and clean data

## Future Work
With the base work set for the project, we have decided the following next steps would be appropriate:
* Add functionality as a website through utilization of open source web technology like React JS or similar frameworks
* Distribution of Senators by age compared to US population aged old enough to be Senators
* Developing charts displaying the relative influence of Senators, as well as further explaining how that was calculated
* Adding more professional flare to the project, elevating it to a level where we feel it is publishable as a website
