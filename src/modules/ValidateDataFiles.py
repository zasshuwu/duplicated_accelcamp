from modules.Load import *
import os

data_dir = "../../data/"

files = os.walk(data_dir)

datasets = list(files)[0][1]

wrongly_formated = []

for dataset in datasets[1:]:
    runs = list(os.walk(data_dir+dataset))[0][1]
    print("\n\n==========Runs Found in [{0}]========".format(dataset))
    for j in runs:
        print("Found: " + j)

    print("============================")

    for a in runs:
        print("\n Validating '{0}'... ".format(a))
        found_files = os.listdir(data_dir+dataset+"/"+a)
        not_file = list(filter(lambda x: ((x.split(".")[type_index] != "accel" and
                                           x.split(".")[type_index] != "omega") or
                                          x.split(".")[-1].lower() != "csv" or
                                          len(x.split(".")) != 4
                                          ),
                               found_files))
        for i in not_file:
            print("- " + i + ("(Wrong File Structure)" if len(i.split(".")) != 4
                              else "(Wrong File Format)" if i.split(".")[-1].lower() != "csv"
            else "(Unsupported Type)" if i.split(".")[type_index] != "accel" and i.split(".")[type_index] != "omega"
            else ""
                              ))
        if not_file == []:
            print("No Invalid Files were found")
