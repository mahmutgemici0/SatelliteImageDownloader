'''
Download satellite images from lat and lon coordinates.

'''
import os
import csv
import lib.GoogleMapDownloader as gmd

meta_data = csv.reader(open("datasets_positive/#Database_structure.csv"), delimiter=',')

for meta_row in meta_data:
    print(meta_row)
    if meta_row[0] == ('file_name'):
        continue
    line_count = 1
    print(meta_row[0])

    folder_name = "raw_data/{}".format(meta_row[5].strip())
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)
    with open('datasets_positive/{}'.format(meta_row[0],meta_row[5])) as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        for row in csvreader:
            if line_count == 1:
                line_count +=1
            else:

                file_name = "{}/{}_{:04d}.png".format(folder_name, meta_row[4].strip(), line_count)

                image = gmd.run_example(latitude = float(row[int(meta_row[2])]),
                                        longitude = float(row[int(meta_row[3])]),
                                        img_size = 1000,
                                        map_size = 5000,
                                        file_name = file_name)   

                print('line: {} \t name: {}'.format(line_count, file_name))
                line_count += 1

print('done')
