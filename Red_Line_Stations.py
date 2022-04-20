## Red Line Stations list

#Red_Line_Stations

red_line_stations = {
  'ALEWIFE': set(['Davis']),
  'Davis': set(['Porter', 'ALEWIFE']),
  'Porter': set(['Harvard', 'Davis']),
  'Harvard': set(['Porter', 'Central']),
  'Central': set(['Harvard', 'Kendall/MIT']),
  'Kendall/MIT': set(['Central', 'Charles/MGH']),
  'Charles/MGH': set(['Kendall/MIT', 'Park St']),
  'Park St': set(['Charles/MGH', 'Downtown']),
  'Downtown': set(['Park St', 'South Station']),
  'South Station': set(['Downtown', 'Broadway']),
  'Broadway': set(['South Station', 'Andrew']),
  'Andrew': set(['Broadway', 'JFK/UMass']),
  'JFK/UMass': set(['Savin Hall', 'Andrew', 'Savin Hall']),
  'North Quincy': set(['JFK/UMass', 'Wollaston']),
  'Wollaston': set(['North Quincy', 'Quincy Center']),
  'Quincy Center': set(['Wollaston', 'Quincy Adams']),
  'Quincy Adams': set(['Quincy Center', 'BRAINTREE']),
  'BRAINTREE': set(['Quincy Adams']),
  'Savin Hall': set(['JFK/UMass', 'Fields Corner']),
  'Fields Corner': set(['Savin Hall', 'Shawmut']),
  'Shawmut': set(['Fields Corner', 'ASHMONT']),
  'ASHMONT': set(['Cedar Grove', 'Shawmut']),
  'Cedar Grove': set(['ASHMONT', 'Butler']),
  'Butler': set(['Cedar Grove', 'Milton']),
  'Milton': set(['Butler', 'Central Ave']),
  'Central Ave': set(['Milton', 'Valley Rd']),
  'Valley Rd': set(['Central Ave', 'Capen St']),
  'Capen St': set(['Valley Rd']),
  }

