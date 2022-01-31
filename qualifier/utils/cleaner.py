import pandas as pd
import os
import numpy as np

from qualifier.utils.helper import add_values, create_code

def clean_housing_inventory_data(house_listing_df):
    # Changing the date column format to yyyy-mm-dd
    house_listing_df['month_date_yyyymm'] = pd.to_datetime(house_listing_df['month_date_yyyymm'], format='%Y%m')

    # Renaming the column `month_date_yyyymm` to `Date`
    house_listing_df.rename(columns={'month_date_yyyymm':'Date'}, inplace=True)

    # Creating new temporary Dataframe with split values of the column
    temp_county_state_df = house_listing_df['county_name'].str.split(",", n =1 , expand = True)

    #Re assigning county_name from the temporary Dataframe
    house_listing_df['county_name'] = temp_county_state_df[0].str.strip()

    #Creating a new column for State
    house_listing_df['state'] = temp_county_state_df[1].str.strip()

    # Selecting Data for Washington State
    wa_house_listing_df = house_listing_df[house_listing_df['state'] == 'wa']
    wa_house_listing_df['county_name'] = wa_house_listing_df['county_name'].str.title()

    # Sorting Records by Date and County Name
    wa_house_listing_df = wa_house_listing_df.sort_values(['Date' , 'county_name'], ascending = (True, True)).reset_index(drop = True)
    
    return wa_house_listing_df

def transform_rental_dataframe(rental_dataframe):
    
    # Getting Date Column Names seperately to create a seperate column for Date
    dates = rental_dataframe.columns[3:]
    
    # Creating new Series to store the type and value of Rental data(eg : City/County)
    col_name = rental_dataframe.columns[0]
    col_values = pd.Series(rental_dataframe.iloc[:,0])
    
    # Creating new DataFrame `col_details` for col_name(City_Name/County_Name) and `FIPS_Code`
    col_details = rental_dataframe.loc[:,[col_name , 'FIPS_Code']]
    
    # Creating a new DataFrame with values as the cross product of `dates` list and `col_values` list
    cross_product_df =  pd.MultiIndex.from_product([dates, col_values], names = ['Date', col_name])
    cross_product_df = pd.DataFrame(index = cross_product_df).reset_index()
    
    # Merging the new DataFrame with `col_details` DataFrame
    result_df = pd.merge(left = cross_product_df, right=col_details, left_on=col_name, right_on=col_name)
    result_df = result_df.sort_values(by=['Date',col_name] , ignore_index = True)
    
    
    rental_dataframe.set_index('FIPS_Code' , inplace=True)
    rental_dataframe = rental_dataframe.replace('     NA', np.NaN)
    
    for index, row in result_df.iterrows():
        date_col = row['Date']
        FIPS_Code = row['FIPS_Code']
        result_df.at[index, 'Average_Rental_Price'] = rental_dataframe.loc[FIPS_Code,date_col]
        
    result_df['Date'] = pd.to_datetime(result_df['Date'], format='%Y_%m')
    # result_df = result_df.fillna(0)
    result_df = result_df.dropna()
    result_df['Average_Rental_Price'] =result_df['Average_Rental_Price'].astype("float")
    return result_df

def transform_building_dataframe(building_df , df_column_type):
    # Getting Date Column Names seperately to create a seperate column for Date
    dates = building_df.columns[1:]
    
    # Creating new Series to store the type and value of Original data(eg : City/County)
    col_name = building_df.columns[0]
    col_values = pd.Series(building_df.iloc[:,0])
    
    # Creating a new DataFrame with values as the cross product of `dates` list and `col_values` list
    result_df =  pd.MultiIndex.from_product([dates, col_values], names = ['Date', col_name])
    result_df = pd.DataFrame(index = result_df).reset_index()
    
    building_df.set_index(col_name , inplace=True)
    
    for index, row in result_df.iterrows():
        col_identifier = row['Date']
        row_identifier = row[col_name]
        result_df.at[index, df_column_type] = building_df.loc[row_identifier,col_identifier]
        
    return result_df 

def transform_labor_emp_dataframe(data_df ,df_type ):
    data_df = data_df.stack()
    data_df = pd.DataFrame(data_df.reset_index())
    data_df.columns = ['Date','FIPS_CODE',df_type+'_NO.']
    data_df['FIPS_CODE'] = data_df['FIPS_CODE'].astype('int64')
    return data_df

def clean_monthly_housing_permits_data(housing_units_df):
    
    housing_units_df['Total_Housing_Units'] = housing_units_df.apply(lambda row : add_values(row['Units'],row['Units.1'], row['Units.2'],row['Units.3']), axis = 1)
    
    housing_units_df = housing_units_df.loc[housing_units_df['State'] == 53]
    # df['DOB'].dt.strftime('%m/%d/%Y')
    housing_units_df['Date'] = pd.to_datetime(housing_units_df['Date'], format='%Y%m')
    # housing_units_df['Date'] = housing_units_df['Date'].dt

    housing_units_df['FIPS_CODE'] = housing_units_df['County'].apply(lambda x: create_code(x))
    housing_units_df.sort_values(by = ['Date','Name'] , inplace=True)
    
    housing_units_df = housing_units_df[['Date','FIPS_CODE','Name','Total_Housing_Units']]
    
    return housing_units_df