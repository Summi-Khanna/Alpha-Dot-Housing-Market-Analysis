# Alpha Dot Housing Market Analysis

There are roughly 12 million Single-Family Rentals (SFRs) in the United States. They represent more than one-third of all rented housing and have an aggregate market value of approximately `$`4.5 trillion dollars. Until recently, these assets were predominantly owned by individuals or small investors. In the last decade, however, SFRs have emerged as an important asset class for Real Estate Investment Trusts (REITs). They are now attracting attention (and dollars) from large and institutional investors. Most SFR REITs are focused on a handful of primary markets in the American sunbelt (the Southeast and the Southwest), missing out on opportunities for potentially higher returns in more supply-constrained secondary markets in the North, Midwest, and West Coast. With this project, Alpha Dot is developing tools to systematically analyze residential markets across the country to support smart SFR portfolio design for performance and risk mitigation. 

Alpha Dot has assembled data on housing supply, demand, and returns from the private sector and government sources to spot trends and inflection points in residential markets across the country. This Minimum Viable Product (MVP) is a proof of concept demonstrating that data are available with broad enough coverage, at a granular enough geographic levels, and periodicity with high enough frequency to use for timely nationwide automated analysis. This notebook demonstrates the following types of visualizations for data exploration:<br>

 - Interactive line and bar charts for time series analysis
 - Maps for spatial analysis
 - A correlogram to explore the relationship between variables

This project uses an analysis of recent trends in the Washington state housing market to demonstrate the application of these tools to the investment research use case. Alpha Dot's analysis focuses on the impacts of the recent demand shock to urban housing markets in Washington state as the pandemic-induced micro depression of 2020 caused a sharp drop in employment, household formation, and rents. In most counties and cities, house prices plateaued in 2020. Both home prices and rents, however, climbed rapidly in 2021 during the surge of migration that followed. Generally, suburbs and rural areas saw more rapidly rising house prices and rent than urban centers, as new opportunities to work from home allowed workers to move to more affordable areas.

Ultimately, the goal of this MVP is to answer the question below.

```An investor is interested in adding one or more Washington houses to an SFR portfolio. The investor wants to know whether it is recommendable, and if so, what returns can be expected and in which county he or she should invest?```

To answer this question, Alpha Dot constructed an estimate of monthly SFR returns by county. Total returns to SFR assets have two components: rental yields and house-price appreciation. We estimated monthly gross rental yield by dividing average house listing price by average rent. We estimated monthly price appreciation gains with the month-to-month percent change in median listing price per square foot. These two series are added together to calculate the total yield. Then we multiply the total return by 12 to annualize it. 

## Data Sources

 - Construction Survey data from the U.S. Census Bureau
 - Housing market data from Realtor.com
 - Rental market data from ApartmentListing.com
 - City Affordability Index from the U.S. Census Bureau
 - Employment and Labor Force data from the Bureau of Labor Statistics
 - Geocoding data from OpenDataSource


# Future Scope

 - Create the SFR returns index for US Counties
 - Create the SFR returns index for US Cities
 - Develop Risk Measures
 - Develop Supply and Demand indices
 - Create an interactive dashboard for SFR investors

---

## Technologies

It supports Python 3.7 and above and has been constructed in the jupyter lab notebook named ```Housing_Market_Analysis.ipynb```

Additionally, the following packages/libraries are used to run the analysis:

- [pandas](https://pypi.org/project/pandas/) - for analyzing data
- [numpy](https://pypi.org/project/numpy/) - for numerical operations
- [pyviz](https://pypi.org/project/pyviz/) - for visualizing data
- [geoviews](https://pypi.org/project/geoviews/) - for visualizing geospatial data
- [seaborn](https://github.com/mwaskom/seaborn/) - for visualizing correlation between variables


---

## Installation Guide

Before running the application first install the following dependencies:

```
  pip install pandas
  pip install jupyterlab 
  pip install numpy
  pip install hvplot
  pip install pyviz
  pip install geoviews
  pip install seaborn

```
---

## Usage

To view the analysis, navigate to the file named ```Housing_Market_Analysis.ipynb``` notebook in the [Alpha Dot repository directory](https://github.com/Summi-Khanna/Alpha-Dot-Housing-Market-Analysis) Or you can navigate to the live version in the jupyter lab directly opening from your terminal using the clone link in terminal.

For better understanding, a small [presentation file has been attached here](https://drive.google.com/file/d/1eyWH3LByyr7QWapSkPS0A64Q1MSmQ7Be/view?usp=sharing) which presents the overall picture of this project.

---

## Contributors
 
Team Leader:
- Rachael Donham 
  Email : rachaeldonham@gmail.com <br>
  LinkedIn : [https://www.linkedin.com/in/rachaeldonham/](https://www.linkedin.com/in/rachaeldonham/)

Team Members:

- Summi Khanna  
  Email : sam.summo2812@gmail.com <br>
  LinkedIn : [https://www.linkedin.com/in/summi-khanna-004a60187/](https://www.linkedin.com/in/summi-khanna-004a60187/)

- Rupika Ranjan Babu  
  Email : rupika10@gmail.com <br> 
  LinkedIn : [https://www.linkedin.com/in/rupika-r-125616a8/](https://www.linkedin.com/in/rupika-r-125616a8/)

- Nomi Enkhbold
  Email : nomienk28@gmail.com <br> 
  LinkedIn : [https://www.linkedin.com/in/nomin-enkhbold-2199191a8/](https://www.linkedin.com/in/nomin-enkhbold-2199191a8/)

---

## License

MIT License

Copyright (c) 2022 Rachael Donham, Summi Khanna, Rupika Rajan Babu, Nomi Enkhbold

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

---
