from typing import List


class Business:
    def __init__(self, 
        name: str,
        website: str,
        description: str,
        foundation: int,
        industry: str,
        employees: int
    ) -> None:
        self.name = name
        self.website = website
        self.description = description
        self.foundation = foundation
        self.industry = industry
        self.employees = employees


class Country:
    def __init__(self, name: str, companies: List[Business]) -> None:
        self.name = name
        self.companies = companies


    def add_business(self, business:Business):
        self.companies.append(business)


    def get_major_company(self) -> Business | None:
        max_number = 0
        company_max:Business|None = None

        for company in self.companies:
            if company.employees > max_number:
                max_number = company.employees
                company_max = company
    
        return company_max


    def get_minor_company(self) -> Business| None:
        company_max = self.get_major_company()
        if company_max == None: raise Exception("Error country is not valid")

        min_number = company_max.employees
        company_min:Business|None = None

        for company in self.companies:
            if company.employees < min_number:
                min_number = company.employees
                company_min = company
    
        return company_min


    def get_average_employees(self) -> float:
        employees_count = 0

        for company in self.companies:
            employees_count += company.employees

        total_companies = self.get_total_companies()

        return round((employees_count / total_companies), 2)


    def get_total_companies(self):
        return len( self.companies )
