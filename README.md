# Global-Warming-Visualization
Time Series Data Exploration of Global Warming Data

Completed Project Compared to the Proposal:

  Initially we set out to create a 3D model or representation of deforestation data over time that would create an effective impact on the user. After our initial research however, we found that if we wanted to best represent the larger issue at hand, we would have to analyze the larger problem of climate change using more than one variable. Since there are so many factors contributing to climate change, we decided it would be most efficient for the user to be able to freely explore this data over time. 
    Since our initial goal was for users to have an effecient way to see how their country is contributing to the global issue of climate change, we decided to collect datasets on a geospacial scale. This along with the fact that global warming is a trend occuring over the past 100 years means that many of our data sets were very large, and the most efficient way to compare these values to those across the globe was with several geospatial maps with user selected exploration through the years available for each dataset. 
    
How to Access Visualization:

Link to start exploring the Visualization on Tableau's Website:
https://public.tableau.com/views/EnvironmentalVisMap/GlobalWarmingData?:display_count=y&publish=yes&:origin=viz_share_link

Local File also available if you have Tableau Public installed in GlobalWarmingViz folder

User's Guide on how to explore the datasets is included under section "Results" in FinalPaper.pdf

To Execute Process in TempDataProcess folder:
instructions to execute your code, specifications such as OS, database version, ODBC driver version, programming language

Process described in CMSC 461 Report was run on an Ubuntu 18.04.03 Virtual Machine with PostgreSQL version 12.0 installed. I used psycopg2 2.8.3-2 Python 3 module for PostgreSQL as my ODBC in order to connect to my temperature database run my python code, which is also included in the TempDataProcess folder, as well as screenshots with the necessary commands to run all the same code. 
