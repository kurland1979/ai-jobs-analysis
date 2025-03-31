import pandas as pd
import matplotlib.pyplot as plt

def max_jobs_per_company(df):
    df['name'] = df['company'].apply(lambda x: x['display_name'])

    count_jobs = df.groupby('name')['id'].count().sort_values(ascending=False).head(3)

    font1 = {'family':'serif','color':'blue','size':20}
    font2 = {'family':'serif','color':'darkred','size':15}

    count_jobs.plot(kind='bar', color=['red','green','blue'])
    plt.title('Top 3 Companies with Most Job Postings',fontdict=font1)
    plt.xlabel('Company Name',fontdict=font2)
    plt.ylabel('Count',fontdict=font2)
    plt.xticks(rotation=20)
    plt.show()

    return count_jobs

def membership_pattern(df):
    
    df['name'] = df['company'].apply(lambda x: x['display_name'])

    type_salary = df.groupby('name').agg({
                        'salary_max': 'count',
                        'salary_min': 'count'
                            }).sort_values(by='salary_max',ascending=False).head(3)
    
    return type_salary

def contract_type_per_company(df):
    
    df['name'] = df['company'].apply(lambda x: x['display_name'])

    contract_type = df.groupby(['name', 'contract_type']).size().sort_values(ascending=False)

    
    return contract_type

