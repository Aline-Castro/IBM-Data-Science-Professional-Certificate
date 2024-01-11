# Graded Quiz: Exploratory Data Analysis using SQL

#### 1. Question 1: Which of the following will retrieve  upto 20 records  from the spacex table?

- ✔ ***SELECT *  from SPACEXTBL LIMIT 20***
- SELECT TOP 20 rows from SPACEXTBL
- SELECT * from SPACEXTBL where count(*)=20
- SELECT * from SPACEXTBL MAX 20


#### 2. Question 2: Which of the following queries display the minimum payload mass?

- select payload_mass__kg_ from SPACEXTBL order by payload_mass__kg_ group by  booster_version LIMIT 1
- ✔ ***select min(payload_mass__kg_) from SPACEXTBL*** 
- select payload_mass__kg_ from SPACEXTBL where payload_mass__kg_=(select max(payload_mass__kg_) from SPACEXTBL) LIMIT 1
- select payload_mass__kg_ from SPACEXTBL order by payload_mass__kg_ desc LIMIT 1


#### 3. Question 3
You are writing a query that will give you the total payload_mass_kg carried by the booster versions. The mass  should be  stored in the mass column. You want the result column to be called “Total_Payload_Mass”. Which of the following SQL queries is correct?

- ✔ ***SELECT sum(PAYLOAD_MASS__KG_) as Total_Payload_Mass from SPACEXTBL*** 
- SELECT count(PAYLOAD_MASS__KG_) as Total_Payload_Mass from SPACEXTBL 
- SELECT sum(PAYLOAD_MASS__KG_)  from SPACEXTBL 


#### 4. Question 4
Which of the following query is used to display the mission outcome counts for each launch site?

- ✔ ***select  count("Mission_Outcome") as MISSION_OUTCOME_COUNT,Launch_Site  from SPACEXTBL group by "Launch_Site"***
- select  sum("Mission_Outcome") as MISSION_OUTCOME_COUNT,Launch_Site  from SPACEXTBL group by "Launch_Site"


#### 5. Question 5
What are the unique launch sites mentioned in the Spacex table?

- CCAFS LC-40,KSC LC-39B,VAFB SLC-4k , CCAFS SLC-40
- ✔ ***CCAFS LC-40,KSC LC-39A, VAFB SLC-4E , CCAFS SLC-40***
- CCAS LC-40,KSC LC-39A,VAFB SLC-4E , CCAFS SLC-80 
- None of the Above

