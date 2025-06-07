import pandas as pd

def demographic_data_analyzer():
    #Column Name
    column_names = [
        'age', 'workclass', 'fnlwgt', 'education', 'education-num',
        'marital-status', 'occupation', 'relationship', 'race', 'seX',
        'capital-gain', 'capital-loss', 'hours-per-week', 'native-country', 'salary'
    ]

    #read dataset
    df = pd.read_csv("adult-data.csv", header=None, names=column_names)
    df['age'] = pd.to_numeric(df['age'], errors='coerce')

    #task 1 : count people by race
    race_count = df['race'].value_counts()

    #task 2 : average age of men
    average_age_men = round(df[df['sex'] == 'Male']['age'].mean(), 1)

    #task 3 : percentage of men with bacheloors degree
    men = df[df['sex'] == 'Male']
    men_bachelors = men[men['education'] == 'Bachelors']
    percentage_men_bachelors = round((len(men_bachelors) / len(men)) * 100, 1)

    #task 4 : percentage of people with higher education and high 
    higher_education = df[df['education'].isin(['Bachelors', 'Master', 'Doctorate'])]
    higher_education_rich = higher_education[higher_education['salary']== '>50K']
    percentage_higher_education_rich = round((len (higher_education_rich) / len(higher_education)) * 100, 1)
    #task 5 : percentage of people with lower education and high salary
    lower_education = df[~df['education'].isin(['Bachelors', 'Master', 'Doctorate'])]
    lower_education_rich = lower_education[lower_education['salary'] == '>50K']
    percentage_lower_education_rich = round((len (lower_education_rich) / len(lower_education)) * 100, 1)
    
    #task 6 : minimum working hours per week
    minimum_working_perweek = df['hours-per-week'].min()

    #task 7 : person with minimum working hours per week with salary >50K
    minimum_working_per_week = df['hours-per-week'].min()
    min_workers = df[df['hours-per-week'] == minimum_working_per_week]
    rich_min_workers_count = len(min_workers[min_workers['salary'] == '>50K'])
    total_min_workers = len(min_workers)
    rich_percentage = (rich_min_workers_count / total_min_workers) * 100 if total_min_workers != 0 else 0

    # task 8 : country that have the highest percentage of people that earn >50K and what is that percentage
    country_group = df.groupby('native-country')
    country_counts = country_group.size()
    rich_country_counts = country_group['salary'].apply(lambda x: (x == '>50K').sum())
    rich_percentage_bycountry = (rich_country_counts / country_counts) * 100
    highest_earning_country = rich_percentage_bycountry.idxmax()
    highest_earning_country_percentage = rich_percentage_bycountry.max()

    #task 9 : the most popular occupation in India and who earn more than 50K
    india_rich = df[(df['native-country'] == 'India') & (df['salary'] == '>50K')]
    top_in_occupation = india_rich['occupation'].value_counts().idxmax()

    return {
        "race_count" : race_count,
        "average_age_men" : average_age_men,
        "percentage_men_bachelors" : percentage_men_bachelors,
        "percentage_higher_education_rich" : percentage_higher_education_rich,
        "percentage_lower_education_rich" : percentage_lower_education_rich,
        "minimum_working_perweek" : minimum_working_perweek,
        "rich_percentage" : rich_percentage,
        "highest_earning_country_percentage" : highest_earning_country_percentage,
        "highest_earning_country" : highest_earning_country,
        "top_in_occupation" : top_in_occupation

    }
