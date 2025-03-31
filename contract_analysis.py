import pandas as pd
import matplotlib.pyplot as plt


def contract_type_analysis(df):
    
    count_contract_type = df['contract_type'].value_counts(normalize=True) 

    my_labels = ['unknown_predicted','contract','permanent']
    myexplode = [0.2, 0, 0]
    plt.pie(count_contract_type, labels=my_labels,explode=myexplode, shadow=True, autopct='%1.1f%%')
    plt.title('Contract Analysis')
    plt.legend()
    plt.show()
    
    return count_contract_type

def contract_time_analysis(df):
    
    count_contract_time = df['contract_time'].value_counts(normalize=True)

    my_labels = ['Unknown','full_time','part_time']
    myexplode = [0.2, 0, 0]
    plt.pie(count_contract_time, labels=my_labels,explode=myexplode, shadow=True, autopct='%1.1f%%')
    plt.title('Contract Time Analysis',  loc='right', pad=20)
    plt.legend(loc='lower right')
    plt.show()

    return count_contract_time

def trelationship_between_values(df):
    
    contract_salary = pd.crosstab(df['contract_type'], df['salary_is_predicted'], normalize=True) 

    font1 = {'family':'serif','color':'blue','size':20}
    font2 = {'family':'serif','color':'darkred','size':15}

    ax = contract_salary.plot(kind='bar', width=(0.8))

    for bar in ax.containers:
        ax.bar_label(bar, fmt='%.1f%%')

    plt.title('Cross Rreferencing Of Salary Types', fontdict=font1)
    plt.xlabel('Types Of Contracts', fontdict=font2)
    plt.ylabel('Relative Crossover',fontdict=font2)
    plt.xticks(rotation=0)
    plt.show()

    return contract_salary









