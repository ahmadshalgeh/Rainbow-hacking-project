#project rainbow (hack az tarigh sha256)
#in barnameh chand hash az voroodi migirad va an hara be adad tabdil mikonad
import hashlib
import csv
from itertools import count
dict_hash_ha = {}
dict_javab_ha = {}

def hash_password_hack(input_file_name, output_file_name):
    for i in range(1000,10000):
        hashe_adad = hashlib.sha256(str(i).encode()).hexdigest()
        dict_hash_ha[hashe_adad] = str(i)
    
    with open(input_file_name)as csv_file:
        csvfile = csv.reader(csv_file)
        for row in csvfile:
            dict_javab_ha[row[0]] = dict_hash_ha[row[1]]




    with open(output_file_name, 'w')as out:
        count = 0
        for i in dict_javab_ha:
            count += 1
            if count == 1:
                out.write(i + ',' + dict_javab_ha[i])
            else:
                out.write('\n' + i + ',' + dict_javab_ha[i])



input = 'C:/Users/Ahmad/tamrinhay_maktabkhooneh/project_hak_rainbow.csv'
output = 'C:/Users/Ahmad/tamrinhay_maktabkhooneh/khoroogi_hack_rainbow.csv'

hash_password_hack(input, output)