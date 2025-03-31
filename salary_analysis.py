import pandas as pd
import matplotlib.pyplot as plt


def salary_ranges(df):
    
    min_salary_min = df['salary_min'].min()
    max_salary_min = df['salary_min'].max()

    min_salary_max = df['salary_max'].min()
    max_salary_max = df['salary_max'].max()

    min_range_salary_min_salary_max = (min_salary_max - min_salary_min) / min_salary_min * 100
    max_range_salary_min_salary_max = (max_salary_max - max_salary_min) / max_salary_min * 100
    
    return (f"The relative range between min and max of salary_min is: {min_range_salary_min_salary_max:.2f}%\n"    
            f"The relative range between min and max of salary_max is: {max_range_salary_min_salary_max:.2f}%")

def contract_salary_avg(df):
    
    contract_contact_salary = df.groupby('contract_type').agg({
                                    'salary_max': 'mean',
                                    'salary_min': 'mean'
                                    }).round(2)
    
    font1 = {'family':'serif','color':'blue','size':20}
    font2 = {'family':'serif','color':'darkred','size':15}
    
    contract_contact_salary.plot(kind='bar', color=['red', 'green'])
    plt.title('Contract Difference Salary', fontdict=font2)
    plt.xticks(rotation=0)
    plt.show()
    return contract_contact_salary

def salary_comparison_contract_time(df):

    salary_comparison_avg = df.groupby('contract_time').agg({
                                'salary_max': 'mean',
                                'salary_min': 'mean'
                            }).round(2)
    
    font1 = {'family':'serif','color':'blue','size':20}
    font2 = {'family':'serif','color':'darkred','size':15}
    
    salary_comparison_avg.plot(kind='bar', color=['yellow', 'blue'])
    plt.title('Salary Comparison By Job', fontdict=font2)
    plt.xticks(rotation=0)
    plt.show()
    
    return salary_comparison_avg
    



