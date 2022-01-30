import pandas as pd
import os
import numpy as np

from qualifier.utils.cleaner import *

def read_housing_inventory_data():
    # Reading Housing List prices from `Resources/RDC_Inventory_Core_Metrics_County_History.csv`
    house_listing_df = pd.read_csv('Resources/RDC_Inventory_Core_Metrics_County_History.csv')

    # Sorting Records by Date and County Name
    wa_house_listing_df = clean_housing_inventory_data(house_listing_df)

    return wa_house_listing_df

def read_rental_inventory():
    # Reading Housing List prices from `Resources/RDC_Inventory_Core_Metrics_County_History.csv`
    rental_county_df = pd.read_csv("Resources/rental_growth_county.csv")
    rental_city_df = pd.read_csv("Resources/rental_growth_city.csv")

    rental_county_df['County_Name'] = (rental_county_df['County_Name'].str.split(" ", n =1 , expand = True))[0]
    rental_city_df['City_Name'] = (rental_city_df['City_Name'].str.split(",", n =1 , expand = True))[0]
    
    rental_county_df = transform_rental_dataframe(rental_county_df)
    rental_city_df = transform_rental_dataframe(rental_city_df)

    return [rental_county_df , rental_city_df]

def read_building_completion_data():
    # Reading Building Completion Units Data from 
    building_completion_county_df = pd.read_csv("Resources/building_completion_units_county_wise.csv" , thousands=',')
    building_completion_city_df = pd.read_csv("Resources/building_completion_units_city_wise.csv" , thousands=',')

    building_completion_county_df['COUNTIES'] = (building_completion_county_df['COUNTIES'].str.split(" ", n =1 , expand = True))[0]
    
    # Calling `custom_dataframe_transform` function on `building_completion_county_df` DataFrame and `building_completion_city_df` DataFrame

    df_column_type = 'Units_Completed'
    building_completion_county_df = transform_building_dataframe(building_completion_county_df , df_column_type)
    building_completion_city_df = transform_building_dataframe(building_completion_city_df , df_column_type)
    
    return [building_completion_county_df, building_completion_city_df]

def read_building_permits_data():
    building_permit_county_df = pd.read_csv("Resources/building_permit_county_wise.csv" , thousands=',')
    building_permit_city_df = pd.read_csv("Resources/building_permit_city_wise.csv" , thousands=',')

    building_permit_county_df['COUNTIES'] = (building_permit_county_df['COUNTIES'].str.split(" ", n =1 , expand = True))[0]
    
    # Calling `custom_dataframe_transform` function on `building_permit_county_df` DataFrame and `building_permit_city_df` DataFrame
    df_column_type = 'Units_Permitted'
    building_permit_county_df = transform_building_dataframe(building_permit_county_df , df_column_type)
    building_permit_city_df = transform_building_dataframe(building_permit_city_df , df_column_type)
    
    return [building_permit_county_df, building_permit_city_df]

def read_labor_data():
    wa_labor_force_df = pd.read_csv('Resources/wa_labor_force_by_county.csv',
                                 index_col=0,infer_datetime_format=True,
                                  parse_dates=True
                                 )

    # Calling `labor_emp_transform` function for DataFrame
    wa_labor_force_df = transform_labor_emp_dataframe(wa_labor_force_df, "LABOR")
    return wa_labor_force_df

def read_employment_data():
    wa_employment_df = pd.read_csv('Resources/wa_employment_by_county.csv',
                                 index_col=0,infer_datetime_format=True,
                                  parse_dates=True)

    # Calling `labor_emp_transform` function for DataFrame
    wa_employment_df = transform_labor_emp_dataframe(wa_employment_df, "EMP")
    return wa_employment_df

def read_monthly_housing_permits_data():
    dir_name = 'Resources/housing_data'
    file_names = os.listdir(dir_name)
    main_df = pd.DataFrame()
    total_rows = 0

    for file_name in file_names:
        if not file_name.startswith('.'):
            df = pd.read_csv(dir_name + '/' + file_name,header=[1],index_col=None)
            total_rows += len(df)
            main_df = main_df.append(df, ignore_index=True)
        
    wa_housing_units_data = clean_monthly_housing_permits_data(main_df)
    return wa_housing_units_data

def read_geo_codes():
    geocode_df = pd.read_csv("Resources/wa_county_geocodes.csv")
    return geocode_df