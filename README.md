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

Works Cited, Databases Used, and References:

[1]CO2 Data:

Boden, T.A., G. Marland, and R.J. Andres. 2017. Global, Regional, and National Fossil-Fuel CO2 Emissions. Carbon Dioxide Information Analysis Center, Oak Ridge National Laboratory, U.S. Department of Energy, Oak Ridge, Tenn., U.S.A. https://doi.org/10.3334/CDIAC/00001_V2017
Etemad, B., J. Luciani, P. Bairoch, and J.-C. Toutain. 1991. World Energy Production 1800-1985. Librarie DROZ, Switzerland.
Marland, G., and R.M. Rotty. 1984. Carbon dioxide emissions from fossil fuels: A procedure for estimation and results for 1950-82. Tellus 36(B):232-61.
Mitchell, B.R. 1983. International Historical Statistics: The Americas and Australasia 1750-1988. pgs. 522-525. Gale Research Company, Detroit, United States.
Mitchell, B.R. 1992. International Historical Statistics: Europe 1750-1988. pgs. 465-485. Stockton Press, New York, United States.
Mitchell, B.R. 1993. International Historical Statistics: The Americas 1750-1988. pgs. 405-414. Stockton Press, New York, United States.
Mitchell, B.R. 1995. International Historical Statistics: Africa, Asia and Oceania 1750-1988. pgs. 490-497. Stockton Press, New York, United States.

[2]CH4 + N2O Data:

European Commission, Joint Research Centre (JRC)/Netherlands Environmental Assessment Agency (PBL). Emission Database for Global Atmospheric Research (EDGAR), release version 4.3.1 http://edgar.jrc.ec.europa.eu/overview.php?v=431, 2016.
Janssens-Maenhout, G., Crippa, M., Guizzardi, D., Muntean, M., Schaaf, E., Dentener, F., Bergamaschi, P., Pagliari, V., Olivier, J. G. J., Peters, J. A. H. W., van Aardenne, J. A., Monni, S., Doering, U., and Petrescu, A. M. R.: Global Atlas of the three major Greenhouse Gas Emissions for the period 1970-2012, Earth System Science Data, essd-2017-79, submitted, 2017.
Monica Crippa, Greet Janssens-Maenhout, Frank Dentener, Diego Guizzardi, Katerina Sindelarova, Marilena Muntean, Rita Van Dingenen, Claire Granier: Forty years of improvements in European air quality: regional policy-industry interactions with global impacts, Atmos. Chem. Phys., 16, 3825-3841, doi:10.5194/acp-16-3825-2016, 2016.

[3]Deforestation Data:

Food and Agricultural Association of the United Nations. (2019). FAO.org. Retrieved October 3, 2019, from http://www.fao.org/forest-resources-assessment/past-assessments/fra-2015/en/.
Food and Agricultural Association of the United Nations. (2015). Global Forest Resources Assessment 2015 Desk Reference [PDF]. Retrieved from http://www.fao.org/3/a-i4808e.pdf.

[4]Temperature Data:

Climate Change Knowledge Portal. (2018). Metadata of the Climate Change Knowledge Portal. Metadata of the Climate Change Knowledge Portal. World Bank Group.
World Bank Group. (2016). World Bank Climate Change Knowledge Portal. Retrieved October 3, 2019, from https://climateknowledgeportal.worldbank.org/.

Documents:

Bradshaw, C. J. A., Giam, X., & Sodhi, N. S. (2010, May 3). Evaluating the Relative Environmental Impact of Countries. Retrieved October 3, 2019, from https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0010440.
Earth Science Communications Team at NASA's Jet Propulsion Laboratory. (2019, September 30). The Causes of Climate Change. Retrieved October 3, 2019, from https://climate.nasa.gov/causes/.
Hanania, J., Heffernan, B., Jenden, J., Stenhouse, K., & Donev, J. (2018, May 11). Flaring. Retrieved from https://energyeducation.ca/encyclopedia/Flaring
McKinsey Energy Insigts. (n.d.). Bunker fuel. Retrieved from https://www.mckinseyenergyinsights.com/resources/refinery-reference-desk/bunker-fuel/
