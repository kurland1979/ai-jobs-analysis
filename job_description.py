import pandas as pd
import matplotlib.pyplot as plt

def common_role(df):
    
    top_role =  df.groupby('title').size().sort_values(ascending=False).head(7)

    font1 = {'family':'serif','color':'blue','size':20}
    font2 = {'family':'serif','color':'darkred','size':15}

    top_role.plot(kind='bar',color=['red','green','blue','yellow','black','magenta','cyan'], figsize=(16,8))
    plt.title('Top Role', fontdict=font1)
    plt.xlabel('Roles', fontdict=font2)
    plt.ylabel('Count', fontdict=font2)
    plt.xticks(rotation=90)
    plt.show()

    return top_role

def pattern_between_position_salary(df):
    
    top_role =  df['title'].value_counts().head(7).index

    filter_top_role = df[df['title'].isin(top_role)]

    salary_role = filter_top_role.groupby('title')['salary_max'].mean().sort_values(ascending=False).round(2).head(7)

    overall_avg = df['salary_max'].mean()
    salary_role_status = salary_role.apply(lambda x: 'above' if x > overall_avg else 'below')

    top_7_role_df = pd.DataFrame({
                    'mean_salary': salary_role,
                    'salary_vs_avg': salary_role_status
                        })


    return top_7_role_df

    