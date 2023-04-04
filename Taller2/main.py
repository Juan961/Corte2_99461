from data import read_data

from data import get_country_by_id
from data import get_major_company_by_country_name
from data import get_minor_company_by_country_name
from data import get_average_employees_by_country_name
from data import get_total_companies_by_country_name

from exceptions import OutOfRange

def main():
    try:
        read_data()

        continue_menu = True

        while continue_menu:
            try:
                country_index = int(input("Enter the country index (-1 to exit): "))

                if country_index == -1:
                    continue_menu = False
                    continue

                if country_index > 243 or country_index < 1 : raise OutOfRange()

                # Adjust to index 0
                country_index -= 1

                country_name = get_country_by_id(country_index)

                print(f"País: { country_name }")
                print("")

                major_company = get_major_company_by_country_name(country_name)
                print(f"Empresa con el mayor número de empleados")
                print("")
                print(f"- Empresa: { major_company.get('name') }")
                print(f"- Website: { major_company.get('website') }")
                print(f"- Descripción: { major_company.get('description') }")
                print(f"- Fundación: { major_company.get('founded') }")
                print(f"- Industria: { major_company.get('industry') }")
                print(f"- # Empleados: { major_company.get('number_of_employees') }")

                print("")

                minor_company = get_minor_company_by_country_name(country_name)
                print(f"Empresa con el menor número de empleados")
                print("")
                print(f"- Empresa: { minor_company.get('name') }")
                print(f"- Website: { minor_company.get('website') }")
                print(f"- Descripción: { minor_company.get('description') }")
                print(f"- Fundación: { minor_company.get('founded') }")
                print(f"- Industria: { minor_company.get('industry') }")
                print(f"- # Empleados: { minor_company.get('number_of_employees') }")

                print("")

                average_employees = get_average_employees_by_country_name(country_name)
                print(f"Average employees: { average_employees }")

                total_companies = get_total_companies_by_country_name(country_name)
                print(f"Total companies: { total_companies }")

                print("")

            except OutOfRange:
                print("Error: Please enter a country index between 1 and 243")
                continue

    except Exception as e:
        print(e)

if __name__ == "__main__":
    main()
