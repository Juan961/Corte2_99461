from data import read_data
from data import get_country_by_id

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

                country = get_country_by_id(country_index)

                if country == None: raise Exception("Error country is not valid")

                print(f"País: { country.name }\n")

                major_company = country.get_major_company()
                if major_company == None: raise Exception("Error country is not valid")

                print(f"Empresa con el mayor número de empleados\n")
                print(f"- Empresa: { major_company.name }")
                print(f"- Website: { major_company.website }")
                print(f"- Descripción: { major_company.description }")
                print(f"- Fundación: { major_company.foundation }")
                print(f"- Industria: { major_company.industry }")
                print(f"- # Empleados: { major_company.employees }\n")

                minor_company = country.get_minor_company()
                if minor_company == None: raise Exception("Error country is not valid")

                print(f"Empresa con el menor número de empleados\n")
                print(f"- Empresa: { minor_company.name }")
                print(f"- Website: { minor_company.website }")
                print(f"- Descripción: { minor_company.description }")
                print(f"- Fundación: { minor_company.foundation }")
                print(f"- Industria: { minor_company.industry }")
                print(f"- # Empleados: { minor_company.employees }\n")

                average_employees = country.get_average_employees()
                print(f"Average employees: { average_employees }")

                total_companies = country.get_total_companies()
                print(f"Total companies: { total_companies }\n")

            except OutOfRange:
                print("Error: Please enter a country index between 1 and 243")
                continue

    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
