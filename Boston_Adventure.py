from graph_search import bfs, dfs
from Red_Line_Stations import red_line_stations
from Boston_Landmarks import Boston_landmarks
from Landmark_Choices import landmark_choices


landmark_string = ""
for letter, landmark in landmark_choices.items():
  landmark_string += "{0} - {1}\n".format(letter, landmark)

stations_under_construction = ['Butler']

def greet():
  print("                        @@@                       ")
  print("         @@@@@@@@@@@@@@     @@@@@@@@@@@@@@        ")
  print("      @@*                                 /@@     ")
  print("    @@              ...........              @@   ")
  print("    @@   @@@@@@@@@@@           @@@@@@@@@@@   @@   ")
  print("    @@  @@         @@@@@@@@@@@@@         @@  @@   ")
  print("   #@   @@              ,@               @@   @(  ")
  print("   @@   @@              ,@               @@   @@  ")
  print("   @@   @#              ,@               &@   @@  ")
  print("   @@  &@                                 @%  @@  ")
  print("   @@  @@               ,@                @@  @@  ")
  print("   @@  @@                                 @@  @@  ")
  print("   @@   @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@   @@  ")
  print("  #@                                           @( ")
  print("  @@     @@@@                         @@@@     @@ ")
  print("  @@   @@    @@                     @@    @@   @@ ")
  print("  @@   @@@  @@(                     %@@  @@&   @@ ")
  print("  @@                                           @@ ")
  print("  @@ @@   @@   @@   @@  .@   @@   @@   @@   @@ @@ ")
  print("  @@ @@   @@   @@   @&   @   @@   @@   @@   @@ @@ ")
  print("   @@@@/////////////////////////////////////@@@@  ")
  print("             @@                     @@            ")
  print("            @@                       @@           ")
  print("      %@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#     ")
  print("         @@                             @@        ")
  print("Welcome to the Red Line Station in Boston, Massachusetts!")
  print("We'll help you find the shortest route between the following Boston landmarks:\n" + landmark_string)

def red_line_route():
  greet()
  new_route()
  goodbye()

def set_start_and_end(start_point, end_point):
  if start_point is not None:
    change_point = input("What would you like to change? You can enter 'o' for 'origin', 'd' for 'destination', or 'b' for 'both': ")
    if change_point == "b":
      start_point = get_start()
      end_point = get_end()
    elif change_point == "o":
      start_point = get_start()
    elif change_point == "d":
      end_point = get_end()
    else:
      print("Oops, that isn't 'o', 'd', or 'b'...")
      set_start_and_end(start_point, end_point)

  else:
    start_point = get_start()
    end_point = get_end()
  return start_point, end_point

def get_start():
  start_point_letter = input("Where are you coming from? Type in the corresponding letter: ")
  if start_point_letter in landmark_choices:
    start_point = landmark_choices[start_point_letter]
    return start_point
  else:
    print("Sorry, that's not a landmark we have data on. Let's try this again...")
    return get_start()

def get_end():
  end_point_letter = input("Ok, where are you headed? Type in the corresponding letter: ")
  if end_point_letter in landmark_choices:
    end_point = landmark_choices[end_point_letter]
    return end_point
  else:
    print("Sorry, that's not a landmark we have data on. Let's try this again...")
    return get_end()

def new_route(start_point = None, end_point = None):
  start_point, end_point = set_start_and_end(start_point, end_point)
  shortest_route = get_route(start_point, end_point)
  
  if shortest_route is not None:
    shortest_route_string = '\n'.join(shortest_route)
    print("The shortest Red Line route from {0} to {1} is:\n{2}".format(start_point, end_point, shortest_route_string))
  else:
    print("Unfortunately, there is currently no path between {0} and {1} due to maintenance.".format(start_point, end_point))
  
  again = input("Would you like to see another route? Enter y/n: ")
  if again == "y":
    see_landmarks()
    return new_route(start_point, end_point)

  return shortest_route

  

def see_landmarks():
  see_landmarks = input("Would you like to see the list of landmarks again? Enter y/n: ")
  if see_landmarks == "y":
    print(landmark_string)


def get_route(start_point, end_point):
  start_stations = Boston_landmarks[start_point]
  end_stations = Boston_landmarks[end_point]
  routes = []
  for start_station in start_stations:
    for end_station in end_stations:
      rail_system = get_active_stations() if stations_under_construction else red_line_stations
      
      if len(stations_under_construction) > 0:
        possible_route = dfs(rail_system, start_station, end_station)
        if possible_route is None:
          return None
      route = dfs(rail_system, start_station, end_station)
      if route:
        routes.append(route)
  shortest_route = min(routes, key = len)
  return shortest_route

def get_active_stations():
  updated_rail = red_line_stations
  for station_under_construction in stations_under_construction:
    for current_station, neighboring_stations in red_line_stations.items():
      if current_station != station_under_construction:
        updated_rail[current_station] -= set(stations_under_construction)
      else:
        updated_rail[current_station] = set([])
  return updated_rail


def goodbye():
  print("Thanks you for using the Red Line in Boston!")




red_line_route()