import csv, os

files = os.listdir("./NITs")

def create_csv(file):
    """
    Assumed format after split:
    ['National', 'Institute', 'of', 'Technology,', 'Tiruchirappalli',
    'Computer', 'Science', 'and', 'Engineering', '(4', 'Years,', 'Bachelor', 'of', 'Technology)',
    'HS', 'OPEN', 'Gender-Neutral', '936', '5164']

    ['National', 'Institute', 'of', 'Technology,', 'Tiruchirappalli',
    'Computer', 'Science', 'and', 'Engineering', '(4', 'Years,', 'Bachelor', 'of', 'Technology)',
    'HS', 'OPEN', 'Female-only', '(including', 'Supernumerary)', '2903', '6687']
    """
    options = []
    for line in file.readlines():
        line_list = line.split()
        
        if "Technology," in line_list:
            tech_idx = line_list.index("Technology,") # some NIT arent named NIT. so do relative indexing from word "Technology"
        else:
            tech_idx = line_list.index("Technology")


        if "female" in line.lower(): # ignore females
            continue
        
        type = line_list[-5]

        if ("Andhra" not in line) and ("Arunachal" not in line) and ("Karnataka" not in line):
            branch = " ".join(line_list[tech_idx + 2 : -5])
            nit = line_list[tech_idx + 1]
        else:
            if "Andhra" in line:
                nit = "Andhra Pradesh"
            elif "Arunachal" in line:
                nit = "Arunachal Pradesh"
            else:
                nit = "Surathkal"

            branch = " ".join(line_list[tech_idx + 3 : -5])
        
        print(nit)
        if type == "HS" and nit != "Tiruchirappalli": # ignore HS if not home state
            continue
        if type in ("GO", "JK", "LA"):
            continue

        opening = line_list[-2]
        closing = line_list[-1]
        
        options.append(["National Institute of Technology " + nit, branch, type, opening, closing])
    return options
    
    with open("NIT_csv/"+os.path.basename(file.name)[:-4] + ".csv", "w", newline="\n") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(options)

all_options = []
for filename in files:
    with open("NITs/"+filename, "r") as file:
        options = create_csv(file)
    all_options.extend(options)

with open("NIT_csv/NIT_combined.csv", "w", newline="\n") as file:
    writer = csv.writer(file)
    writer.writerows(all_options)