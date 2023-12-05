

def build_dict(org_x, org_y, org_count):
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

  print(coordinates)

def main():
  states_in_map_order = [
    'Alaska', 'Maine',
    'Wisconsin', 'Vermont', 'New Hampshire',
    'Washington', 'Idaho', 'Montana', 'North Dakota', 'Minnesota',
    'Oregon', 'Michigan',
    'New York', 'Massachusetts', 'Rhode Island', 'Connecticut', 'Wyoming', 'Iowa', 'Illinois', 'Indiana',
    'Ohio', 'Pennsylvania', 'New Jersey', 'Delaware', 'Maryland', 'Nevada', 'Utah', 'Colorado', 'Nebraska', 'South Dakota',
    'Kansas', 'Missouri', 'Kentucky', 'West Virginia', 'Virginia', 'California', 'Arizona', 'New Mexico', 'Oklahoma', 'Texas',
    'North Carolina', 'Tennessee', 'Arkansas', 'Louisiana', 'Mississippi', 'Alabama', 'Georgia', 'South Carolina', 'Florida', 'Hawaii'
  ]

  states_2letter_in_map_order = [
    'AK', 'ME',
    'WI', 'VT', 'NH',
    'WA', 'ID', 'MT', 'ND', 'MN' 'IL', 'MI',
    'NY', 'MA',
    'OR', 'NV', 'WY', 'SD', 'IA', 'IN', 'OH', 'PA', 'NJ', 'CT', 'RI',
    'CA', 'UT', 'CO', 'NE', 'MO', 'KY', 'WV', 'VA', 'MD', 'DE',
    'AZ', 'NM', 'KS', 'AR', 'TN', 'NC', 'SC', 'DC',
    'OK', 'LA', 'MS', 'AL' 'GA',
    'HI', 'TX', 'FL',
    ]

  print(len(states_2letter_in_map_order))


if __name__ == '__main__':
  main()