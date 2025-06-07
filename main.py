from demographic_data_analyzer import demographic_data_analyzer

result = demographic_data_analyzer()
result_race_count = result["race_count"]
result_avg_of_men = result["average_age_men"]
result_percentage_bachelors = result["percentage_men_bachelors"]
result_percentage_higher_education_rich = result["percentage_higher_education_rich"]
result_percentage_lower_education_rich = result["percentage_lower_education_rich"]
result_minimum_working_hours_perweek = result["minimum_working_perweek"]
result_rich_percentage = result['rich_percentage']
result_highest_earning_country = result['highest_earning_country']
result_highest_earning_country_percentage = result['highest_earning_country_percentage']
result_top_in_occupation = result['top_in_occupation']

print("race_count:")
print(result_race_count)
print("Average age of men:")
print(result_avg_of_men)
print("percentage_bachelors_men")
print(result_percentage_bachelors)
print("result_percentage_higher_education_rich")
print(result_percentage_higher_education_rich)
print("percentage_low_education_rich")
print(result_percentage_lower_education_rich)
print("minimum working hours perweek")
print(result_minimum_working_hours_perweek)
print("rich_percentage")
print(result_rich_percentage)
print('highest_earning_country')
print(result_highest_earning_country)
print('highest_earning_country_percentage')
print(result_highest_earning_country_percentage)
print('top_in_occupation')
print(result_top_in_occupation)