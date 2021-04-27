import json
import csv

# filename = 'test'
# filename = 'cut'
filename = 'file1'

def flatten_json(y):
    out = {}

    def flatten(x, name=''):
        if type(x) is dict:
            for a in x:
                flatten(x[a], name + a + '_')
        elif type(x) is list:
            i = 0
            for a in x:
                flatten(a, name + str(i) + '_')
                i += 1
        else:
            out[str(name[:-1])] = str(x)

    flatten(y)
    return out

# Read JSON data
with open(filename + '.json') as json_file:
    restaurant_data = json.load(json_file)

# Convert JSON to CSV
n=0
final_data = []
for d in restaurant_data:
    if 'restaurants' in d:
        for r in d['restaurants']:
            final_data.append(flatten_json(r['restaurant']))
    else:
        n=n+1
print(len(final_data)/20)
print(n)
# Write to CSV file
# isHeaderSet = False
csv_file = open(filename + '.csv', 'w', encoding='utf-8')
csv_writer = csv.writer(csv_file)

for d in final_data:
    # if not isHeaderSet:
    #     csv_writer.writerow(d.keys())
    #     isHeaderSet = True
    csv_writer.writerow(d.values())

csv_file.close()
