import pandas as pd
import matplotlib.pyplot as plt

def count_jobs_per_location(df):
    
    df['city'] = df['location'].apply(lambda x: x['area'][-1])
    count_jobs = df.groupby('city')['id'].count().sort_values(ascending=False)

    return count_jobs

def salary_increase_by_region(df):
     
    df['city'] = df['location'].apply(lambda x: x['area'][-1])

    df['mean_salary'] = (df['salary_max'] + df['salary_min']) / 2

    max_salary_per_location = df.groupby('city')['mean_salary'].mean().sort_values(ascending=False).head(10)

    font1 = {'family':'serif','color':'blue','size':20}
    font2 = {'family':'serif','color':'darkred','size':15}

    max_salary_per_location.plot(kind='bar')
    plt.title('Top 10 States by Average Maximum Salary', fontdict=font2)
    plt.xlabel('State', fontdict=font1)
    plt.ylabel('Average Salary', fontdict=font1)
    plt.xticks(rotation=45)
    plt.show()                           
    
    return max_salary_per_location

def visual_graph_summary(df):
    
    plt.scatter(x=df['longitude'], y=df['latitude'], c=df['salary_max'], cmap='viridis')
    plt.title('Salary Display By Region')
    plt.xlabel('Longitude')
    plt.ylabel('Latitude')
    plt.colorbar()
    plt.show()

            

    

    

