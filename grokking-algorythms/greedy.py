

states_needed = {'mt', 'wa', 'or', 'id', 'nv', 'ut', 'ca','az'}

stations = {}
stations['маяк'] = {'id', 'nv', 'ut'}
stations['русское радио'] = {'wa', 'id', 'mt'}
stations['европа плюс'] = {'or', 'nv', 'ca'}
stations['наше радио'] = {'nv', 'ut'}
stations['авторадио'] = {'az','ca'}
final_stations = set()


while states_needed:
  best_station = None
  states_covered = set()
  for station, states_for_station in stations.items():
    covered = states_needed & states_for_station
    if len(covered) > len(states_covered):
      best_station = station
      states_covered = covered

  states_needed -= states_covered
  final_stations.add(best_station)

print(final_stations)