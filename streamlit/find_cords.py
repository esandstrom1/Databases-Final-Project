def build_cords(org_x, org_y, org_count):
    coordinates = []

    width = 42
    height = 42
    spacer = 5

    count = org_count
    x = org_x
    y = org_y

    for i in range(count):
        coordinates.append([x, org_y])
        # print(f'cordinates: {coordinates}')

        x += width
        y = org_y + height

        # print(f'x_second {x}  y_second {y}')

        coordinates.append([x, y])
        # print(f'cordinates 2: {coordinates}')

        x += spacer

    # print(f'from build cords {coordinates}')
    return (coordinates)


def build_state_with_cords():
    states_dict = {
        'AL': 'Alabama', 'AK': 'Alaska', 'AZ': 'Arizona', 'AR': 'Arkansas', 'CA': 'California',
        'CO': 'Colorado', 'CT': 'Connecticut', 'DE': 'Delaware', 'FL': 'Florida', 'GA': 'Georgia',
        'HI': 'Hawaii', 'ID': 'Idaho', 'IL': 'Illinois', 'IN': 'Indiana', 'IA': 'Iowa',
        'KS': 'Kansas', 'KY': 'Kentucky', 'LA': 'Louisiana', 'ME': 'Maine', 'MD': 'Maryland',
        'MA': 'Massachusetts', 'MI': 'Michigan', 'MN': 'Minnesota', 'MS': 'Mississippi', 'MO': 'Missouri',
        'MT': 'Montana', 'NE': 'Nebraska', 'NV': 'Nevada', 'NH': 'New Hampshire', 'NJ': 'New Jersey',
        'NM': 'New Mexico', 'NY': 'New York', 'NC': 'North Carolina', 'ND': 'North Dakota', 'OH': 'Ohio',
        'OK': 'Oklahoma', 'OR': 'Oregon', 'PA': 'Pennsylvania', 'RI': 'Rhode Island', 'SC': 'South Carolina',
        'SD': 'South Dakota', 'TN': 'Tennessee', 'TX': 'Texas', 'UT': 'Utah', 'VT': 'Vermont',
        'VA': 'Virginia', 'WA': 'Washington', 'WV': 'West Virginia', 'WI': 'Wisconsin', 'WY': 'Wyoming',
        'DC': 'District of Colombia',
    }

    states_2letter_in_map_order = [
        'AK',
        'ME',
        'WI',
        'VT', 'NH',
        'WA', 'ID', 'MT', 'ND', 'MN', 'IL', 'MI',
        'NY', 'MA',
        'OR', 'NV', 'WY', 'SD', 'IA', 'IN', 'OH', 'PA', 'NJ', 'CT', 'RI',
        'CA', 'UT', 'CO', 'NE', 'MO', 'KY', 'WV', 'VA', 'MD', 'DE',
        'AZ', 'NM', 'KS', 'AR', 'TN', 'NC', 'SC', 'DC',
        'OK', 'LA', 'MS', 'AL', 'GA',
        'HI', 'TX', 'FL',
    ]

    # Create a list of full state names in the specified order
    states_in_map_order = [states_dict[state]
                           for state in states_2letter_in_map_order]

    org_state_and_count = {
        'AK': (140, 140, 1),
        'ME': (620, 140, 1),
        'WI': (380, 187, 1),
        'VT': (570, 187, 2),
        'WA': (140, 235, 7),
        'NY': (524, 235, 2),
        'OR': (138, 284, 11),
        'CA': (138, 330, 10),
        'AZ': (187, 380, 8),
        'OK': (282, 427, 5),
        'HI': (138, 475, 1),
        'TX': (282, 475, 1),
        'FL': (524, 475, 1),
    }

    cords = []
    for key, value in org_state_and_count.items():
        cords2 = build_cords(value[0], value[1], value[2])
        for c in cords2:
            cords.append(c)

    # print(cords)
    full_state_name_with_cords = {}
    j = 0

    for i in range(len(states_in_map_order)):
        cord_tup = (cords[j], cords[j+1])
        # print(cord_tup)
        full_state_name_with_cords[states_in_map_order[i]] = cord_tup
        j += 2

    return (full_state_name_with_cords)


def main():
    print(build_state_with_cords())


if __name__ == '__main__':
    main()
