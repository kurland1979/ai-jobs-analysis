from get_data import get_data, check_clean_data
from contract_analysis import contract_type_analysis, contract_time_analysis, trelationship_between_values
from salary_analysis import salary_ranges, contract_salary_avg, salary_comparison_contract_time
from geographic_analysis import count_jobs_per_location, salary_increase_by_region, visual_graph_summary
from company_analysis import max_jobs_per_company, membership_pattern,contract_type_per_company
from job_description import common_role, pattern_between_position_salary

if __name__=='__main__':
    data_df = get_data()
    check_clean_data(data_df)  
    df = check_clean_data(get_data())
    
    print(contract_type_analysis(df))
    print("Most AI job listings are classified as 'unknown_predicted',"
    " suggesting missing or unreported contract data."
    " This indicates that employers often do not specify the contract type,"
    " which may reflect incomplete or inconsistent data collection.")

    print(contract_time_analysis(df))
    print(trelationship_between_values(df))
    print("There is a strong association between undefined contract types and predicted salaries."
    " Most jobs labeled as 'unknown_predicted' also have their salary predicted,"
    " suggesting that missing contract information correlates with missing salary data."
    " In contrast, jobs with a defined contract type, such as 'permanent' or 'contract',"
    " tend to report actual salaries more frequently.")

    print(salary_ranges(df))
    print(contract_salary_avg(df))
    print("Across all contract types,"
    " the average maximum salary is consistently higher than the average minimum salary, as expected."
    " Notably, jobs categorized as 'permanent' show the highest average maximum salary among all contract types,"
    " suggesting that permanent roles tend to offer higher pay compared to contract or undefined positions.")

    print(salary_comparison_contract_time(df))
    print("In part-time positions, the average minimum and maximum salaries are identical,"
    " indicating fixed pay levels regardless of the salary range reported. In full-time roles,"
    " there is a slight increase in average maximum salary over the minimum,"
    " suggesting some salary variation. For jobs with an unknown contract time,"
    " both minimum and maximum salaries are identical, likely due to missing or standardized data.")

    print(count_jobs_per_location(df))
    print(salary_increase_by_region(df))
    print("Job postings are fairly evenly distributed across cities,"
    " with only a slight increase in postings in a few specific locations."
    " As such, a visual chart was not necessary for this part."
    " However, when analyzing average salaries by city, "
    "the top 10 cities show a noticeable difference in mean salary levels."
    " This suggests that while job availability is broadly spread,"
    " salary potential varies more significantly by location.")

    print(visual_graph_summary(df))
    print("This geographic scatter plot visually confirms earlier findings,"
    " showing that while jobs are distributed across the country, "
    "higher salaries tend to cluster in specific regions.")


    print(max_jobs_per_company(df))
    print(membership_pattern(df))

    print(contract_type_per_company(df))
    print("A small group of companies dominates AI job postings in the U.S. market. "
    "These same companies consistently appear across all salary and contract type analyses,"
    " indicating their significant role in shaping employment patterns in the AI sector.")

    print(common_role(df))
    print(pattern_between_position_salary(df))
    print("The analysis of job titles revealed the top 7 most frequently posted AI-related roles."
    " To assess whether popularity correlates with compensation,"
    " we compared the average salary of these roles to the overall average salary in the dataset."
    " The results show that the top 3 most posted positions also offer above-average salaries,"
    " indicating a strong alignment between job market demand and financial incentives."
    " The remaining roles, while still popular, offer salaries below the overall average,"
    " suggesting that not all in-demand positions are equally rewarding.")

    

    

    
