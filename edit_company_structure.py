import os
import json

def create_available_company_list():
    '''
    Grabs list of JSON files from company_structs directory and lists them for the user

    Returns: list of 
    '''
    if os.path.exists("company_structs"):
        companies = sorted(os.scandir("company_structs"))
        index = 0
        print("\nLISTING AVAILABLE JSON FILES:")
        print("-----------------------------")
        for company_file in companies:
            print("%s - %s"%(index, company_file.name))
            index += 1
        print("\n")
        return companies
    else:
        print("ERROR: No company_structs folder detected")
        return []


if __name__ == "__main__":
    create_available_company_list()