import requests
import pandas as pd

def get_data():
    url = 'https://api.adzuna.com/v1/api/jobs/us/search/1'
    app_id = '293f6860'
    app_key = 'fb1541cf812dfa01b6e8848ee380e571'

    params = {
        "app_id": app_id,
        "app_key": app_key,
        "what": "artificial intelligence",
        "where": "united states",
        "results_per_page": 50,
        "content-type": "application/json"
    }

    response = requests.get(url, params=params)
    
    data = response.json()
    jobs = data.get('results', [])
    
    df = pd.DataFrame(jobs)
    
    return df

def check_clean_data(df):
    
    print(df.info())
    print(df.describe())
    print(df.isnull().sum())
    print(df[df['contract_time'].isna()]['contract_time']) # 80 %
    print(df[df['contract_type'].isna()]['contract_type']) # 94 %
    print(df[df['latitude'].isna()]['latitude']) # 6 %
    print(df[df['longitude'].isna()]['longitude']) # 6 %
    df['contract_time'] = df["contract_time"].fillna('Unknown')
    
    column_name = 'longitude'  
    missing_percentage = (df[column_name].isnull().sum() / len(df)) * 100
    print(f"missing data'{column_name}': {missing_percentage:.2f}%")
    print(df[df["contract_time"].isnull()])
    
    
    for i in range(len(df)):
        if pd.isna(df.loc[i, 'contract_type']):
            if df.loc[i, 'salary_is_predicted'] == 0:
                df.loc[i, 'contract_type'] = 'contract'
            else:
                df.loc[i, 'contract_type'] = 'unknown_predicted'
    df['longitude'] = df['longitude'].fillna(df['longitude'].mean())
    df['latitude'] = df['latitude'].fillna(df['latitude'].mean())
    print(df.isnull().sum())
    return df


  

    




