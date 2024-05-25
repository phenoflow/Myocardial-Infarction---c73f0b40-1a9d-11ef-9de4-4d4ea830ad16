# Rosa Parisi, Martin K Rutter, Mark Lunt, Helen S Young, Deborah PM Symmons, Christopher EM Griffiths, Darren M Ashcroft, 2024.

import sys, csv, re

codes = [{"code":"410.1","system":"icd9"},{"code":"410.9","system":"icd9"},{"code":"410.6","system":"icd9"},{"code":"410.4","system":"icd9"},{"code":"410.2","system":"icd9"},{"code":"410.3","system":"icd9"},{"code":"410.7","system":"icd9"},{"code":"410.82","system":"icd9"},{"code":"410.81","system":"icd9"},{"code":"410.92","system":"icd9"},{"code":"410.8","system":"icd9"},{"code":"410.91","system":"icd9"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('myocardial-infarction-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["myocardial-infarction-specified---secondary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["myocardial-infarction-specified---secondary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["myocardial-infarction-specified---secondary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
