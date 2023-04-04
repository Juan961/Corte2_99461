from typing import List

countries_name:List[str] = []

countries_companies = {  }

def read_data():
    """
        0 Index
        1 Organization Id
        2 Name
        3 Website
        4 Country
        5 Description
        6 Founded
        7 Industry
        8 Number of employees
    """

    file = open('./data/organization_data.csv', 'r')

    columns = file.readline().replace("\n", "").split(",")

    companies = file.readlines()

    file.close()

    # Get the total countries in a list and sort them by their name
    for company_str in companies:
        company = company_str.replace("\n", "").split(",")

        if company[4] not in countries_name:
            countries_name.append(company[4])

    countries_name.sort(key=str.lower)

    # Create a dicctionary with every country and their companies
    for country_name in countries_name:
        if not countries_companies.get(country_name):
            countries_companies[country_name] = []

    for k, v in countries_companies.items():
        for company_str in companies:
            company = company_str.replace("\n", "").split(",")

            if company[4] == k:
                countries_companies[k].append({
                    "name": company[2],
                    "website": company[3],
                    "country": company[4],
                    "description": company[5],
                    "founded": int(company[6]),
                    "industry": company[7],
                    "number_of_employees": int(company[8]),
                }) 


def get_country_by_id(country_index):
    country = ""

    for index, (key, _) in enumerate(countries_companies.items()):
        if index == country_index:
            country = key
            break

    return country


def get_major_company_by_country_name(country_name):
    country_companies = countries_companies[country_name]
    
    max_number = 0
    company_max = {  }

    for company in country_companies:
        if company.get("number_of_employees") > max_number:
            max_number = company.get("number_of_employees")
            company_max = company
 
    return company_max


def get_minor_company_by_country_name(country_name):
    country_companies = countries_companies[country_name]

    min_number = 99999999999999
    company_min = {  }

    for company in country_companies:
        if company.get("number_of_employees") < min_number:
            min_number = company.get("number_of_employees")
            company_min = company
 
    return company_min


def get_average_employees_by_country_name(country_name):
    country_companies = countries_companies[country_name]

    employees_count = 0

    for company in country_companies:
        employees_count += company.get("number_of_employees")

    total_companies = get_total_companies_by_country_name(country_name)

    return round((employees_count / total_companies), 2)


def get_total_companies_by_country_name(country_name):
    country_companies = countries_companies[country_name]

    return len(country_companies)
