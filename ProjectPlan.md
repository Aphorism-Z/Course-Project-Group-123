
## Team Responsibilities: 

**Owen** will focus on the datasets and their limitations. He will organize the downloaded data, describe the sources and indicators, check data quality, and review licenses and ethical concerns. 

**Xingyi** will manage the project timeline and track gaps that need further work or team discussion, coordinate team tasks and help clean and combine the datasets. 

**Alexander** will focus on the project overview and research questions. Guide the analysis, help create visualizations, and summarize the findings. 


## Timeline: 

**October 22**: Complete and commit the project plan on GitHub.  

**October 29**: Organize the downloaded datasets and document their sources, indicator definitions, file formats, and applicable licenses. Calculate SHA-256 checksums to record file integrity and establish a clear folder structure for raw data, cleaned data, scripts, documentation, and results. Responsible: Owen 

**November 5**: Check the accuracy, completeness, timeliness, and consistency of each dataset. Look for missing values, duplicate records, differences in available years, and records representing regions or income groups. Based on these checks, we will choose the years to study and decide how to clean the data. Responsible: Owen 

**November 12**: Complete the initial cleaning and integration scripts. Organize each dataset so that each row represents one country in one year, then combine the three datasets using country codes and years. Record the changes we make and identify records that do not match. Responsible: Xingyi 

**November 17**: Check the accuracy, completeness, timeliness, and consistency of the combined dataset. Look for duplicate records, check which countries and years remain after combining the data, and summarize the data. Update the project plan and draft the status report. Each member will write a short summary of their contributions. Responsible: Xingyi, Alexander 

**November 19**: Finish the status report and commit all work completed so far to GitHub.  

**November 26**: Finish the basic statistical analysis and visualizations. We will create a run-all script that runs the separate scripts in order, from data acquisition through analysis. We will also list the required software packages and versions. Responsible: Xingyi, Alexander 

**December 2**: Finish the data dictionary, machine-readable metadata, references, licenses, and all required sections of the final README. We will download a fresh copy of the repository and test the full workflow, fixing any problems that prevent it from running. Responsible: All members. 

**December 6**: Review the results, documentation, file links, and each member’s contributions. Check the project against the final submission checklist and confirm that running the workflow produces the reported results. Responsible: All members 

**December 8**: Commit to GitHub, submit URL. 

## Gaps: 
We still need to select the years to include in our analysis. Although the three datasets have year columns, some countries may not have data for all three indicators in the same years. We will compare their coverage before selecting the study period. 

We also need to decide how to handle missing values and which countries to include. We will check how many records would be removed if we only use records with all three indicators available. We also need to confirm how to identify regional and income-group records so that they are kept separate from individual countries.  

Another question is how to interpret GDP in our analysis. The selected dataset measures total GDP in current US dollars, which reflects the size of an economy rather than average income per person. We will discuss how this affects our research questions and the conclusions we can draw. 

Finally, we may need further guidance on workflow automation and machine-readable metadata as these topics are covered in class.
