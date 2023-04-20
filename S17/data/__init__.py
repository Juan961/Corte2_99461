from typing import List

from models import Business, Country


countries_name:List[str] = []
countries_companies = {  }


def read_data():
    """
        2 Name
        3 Website
        4 Country
        5 Description
        6 Founded
        7 Industry
        8 Number of employees
    """

    file = open('./data/organization_data.csv', 'r')

    # Not use columns name
    file.readline().replace("\n", "").split(",")

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
            countries_companies[country_name] = Country(country_name, [])

    for company_name, company_object in countries_companies.items():
        for company_str in companies:
            company = company_str.replace("\n", "").split(",")

            if company[4] == company_name:
                countries_companies[company_name].add_business(Business(
                    company[2],
                    company[3],
                    company[5],
                    int(company[6]),
                    company[7],
                    int(company[8]),
                ))


def get_country_by_id(country_index) -> Country|None:
    for index, (country_name, country) in enumerate(countries_companies.items()):
        if index == country_index:
            return country
