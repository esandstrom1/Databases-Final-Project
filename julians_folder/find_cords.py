

def build_cords(org_x, org_y, org_count):
  coordinates = []

  width = 53
  height = 53
  spacer = 5

  count = org_count
  x = org_x
  y = org_y

  origin = [x,y]

  for i in range(count):
    coordinates.append(origin)

    x_second = origin[0] + width
    y_second = origin[1] + height

    coordinates.append([x_second, y_second])

    origin[0] += width + spacer

  return(coordinates)

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
    'AK', 'ME',
    'WI', 'VT', 'NH',
    'WA', 'ID', 'MT', 'ND', 'MN', 'IL', 'MI',
    'NY', 'MA',
    'OR', 'NV', 'WY', 'SD', 'IA', 'IN', 'OH', 'PA', 'NJ', 'CT', 'RI',
    'CA', 'UT', 'CO', 'NE', 'MO', 'KY', 'WV', 'VA', 'MD', 'DE',
    'AZ', 'NM', 'KS', 'AR', 'TN', 'NC', 'SC', 'DC',
    'OK', 'LA', 'MS', 'AL', 'GA',
    'HI', 'TX', 'FL',
  ]

  # Create a list of full state names in the specified order
  states_in_map_order = [states_dict[state] for state in states_2letter_in_map_order]

  org_state_and_count = {
    'AK': (165,165,1),
    'ME': (742,165,1),
    'WI': (455,224,1),
    'VT': (685,224,2),
    'WA': (165,280,7),
    'NY': (627,280,2),
    'OR': (165,338,11),
    'CA': (165,395,10),
    'AZ': (224,454,8),
    'OK': (340,511,5),
    'HI': (165,570,1),
    'TX': (340,570,1),
    'FL': (627,570,1),
  }

  cords = []
  for key, value in org_state_and_count.items():
    cords2 = build_cords(value[0], value[1], value[2])
    for c in cords2:
      cords.append(c)

  full_state_name_with_cords = {}
  j = 0
  for i in range(len(states_in_map_order)):
    cord_tup = (cords[j], cords[j+1])
    full_state_name_with_cords[states_in_map_order[i]] = cord_tup
    j+=2

  return(full_state_name_with_cords)

def main():
  print(build_state_with_cords())

if __name__ == '__main__':
  main()