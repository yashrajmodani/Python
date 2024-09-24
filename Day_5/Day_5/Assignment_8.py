#file handling



def generate_report(title,*args,**kwargs):
    
    with open("file.txt",'w')as file:
        file.write('''
            Report Title:{title}
            ================================
            Report Sections:
            ------------------
        
            for i in range(1, len(args)):
                print(f"Sections: ", {args[i]})


            
            -------------------
                
            
            Report Title:{title}
            ================================
            
            Report Sections:
            -------------------")
    
            for i in range(1, len(args)):
                print(f"Sections: ", {args[i]})
            ------------------- ''')

    # for keys, values in (kwargs)



generate_report("Monthly sales Report","Introduction: Overview of sales performance","Data Analysis:Breakdown of sales data by region","Market Trends: Analysis of current market trends ",author = "John Doe",date = "sep 2024",conclusion = "Overall,sales have increased by 15% compared to previous month.",skip_sections = [2])





