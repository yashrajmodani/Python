#
# def generate_report(title,*args,**kwargs):
#     print(f"Report Title:{title}")
#     print("================================")
#     print("\n")
#     print("Report Sections:")
#     print("-------------------")
#
#     for i in range(1, len(args)):
#         print(f"Sections: ", {args[i]})
#
#
#     print("\n")
#     print("-------------------")
#
#     # for keys, values in (kwargs)
#
#
#
# generate_report("Monthly sales Report","Introduction: Overview of sales performance","Data Analysis:Breakdown of sales data by region","Market Trends: Analysis of current market trends ",author = "John Doe",date = "sep 2024",conclusion = "Overall,sales have increased by 15% compared to previous month.",skip_sections = [2])
#
#
#
#
# #
# def generate_report(title, *args, **kwargs):
#     print(f'Report Title: {title}')
#     print("===============================================")
#     print(f"Author: {kwargs['author']}")
#     print(f"Date: {kwargs['date']}")
#     print("\n")
#
#     print("Report Sections: ")
#     print("-----------------------------")
#     for i in range(0, len(args)):
#         print(f"Section {i} : {args[i]}")
#
#     print("\n")
#     print("-----------------------------")
#
#     print("Conclusion")
#     print("-----------------------------")
#     print(kwargs["conclusion"])
#
#
#
# generate_report("Monthly sales report", "Introduction: Overview of sales performance.", "Data Analysis: Breakdown of sales data by region.", "Market Trends: Analysis of current market Trends.", author = "John Doe", date = "September 2024", conclusion = "Overall, sales have increased by 15% compared to the previous month.")



def generate_report(title,*args,**kwargs):
    print(f"Report Title: {title}")
    print("===============================================")

    print(f'Author: {kwargs['author']}')
    print(f'Date: {kwargs['date']}')
    # print("\n")

    print("===========================================")

    print('Report Sections:')
    print('==========================================')
    for i in range(len(args)):
        print(f'Section {i}: {args[i]}')

    print("\n")
    print("===========================================")

    print('Conclusion:')
    print(kwargs['conclusion'])

    print('==============================================')

generate_report("Monthly sales report", "Introduction: Overview of sales performance.", "Data Analysis: Breakdown of sales data by region.", "Market Trends: Analysis of current market Trends.", author = "John Doe", date = "September 2024", conclusion = "Overall, sales have increased by 15% compared to the previous month.")

