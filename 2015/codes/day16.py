def read_data_from_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    return lines

def parse_aunts_sue(data):
    aunts_sue = []
    for line in data:
        sue_number, attributes = line.strip().split(": ", 1)
        sue_number = int(sue_number.split()[1])
        attributes_dict = {}
        for attr in attributes.split(", "):
            key, value = attr.split(": ")
            attributes_dict[key] = int(value)
        aunts_sue.append({'number': sue_number, 'attributes': attributes_dict})
    return aunts_sue

file_path = "../inputs/day16"
data_from_mfcsam = {
    'children': 3,
    'cats': 7,
    'samoyeds': 2,
    'pomeranians': 3,
    'akitas': 0,
    'vizslas': 0,
    'goldfish': 5,
    'trees': 3,
    'cars': 2,
    'perfumes': 1
}

lines = read_data_from_file(file_path)
aunts_sue = parse_aunts_sue(lines)

def find_matching_sue(data_from_mfcsam, aunts_sue):
    for aunt in aunts_sue:
        match = True
        for key, value in data_from_mfcsam.items():
            if key in aunt['attributes']:
                if key in ['cats', 'trees']:
                    if aunt['attributes'][key] <= value:
                        match = False
                        break
                elif key in ['pomeranians', 'goldfish']:
                    if aunt['attributes'][key] >= value:
                        match = False
                        break
                elif aunt['attributes'][key] != value:
                    match = False
                    break
        if match:
            return aunt['number']

matching_sue_number = find_matching_sue(data_from_mfcsam, aunts_sue)
print(f"The gift is from Aunt Sue #{matching_sue_number}")
