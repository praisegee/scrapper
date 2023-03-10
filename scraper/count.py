"""
  This module is use to check duplicete url 
  link path from the `car_links.txt` file.
  So, to prevent data redundancy.
"""


# load unique values from file if any duplicate data
with open('./docs/car_links.txt', 'r') as f:
  d = set([x.strip() for x in f.readlines()])
  print(len(d))

# write the unique values back to the file
with open('./docs/car_links.txt', 'w') as f:
  for a in list(d):
    f.write(f'{a}\n')

print("Done")