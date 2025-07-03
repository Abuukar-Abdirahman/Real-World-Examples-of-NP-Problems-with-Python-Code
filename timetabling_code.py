# Timetabling using Graph Coloring - Greedy Algorithm (Python)
def is_valid(schedule, conflicts):
    for c1, c2 in conflicts:
        if schedule.get(c1) == schedule.get(c2):
            return False
    return True

courses = ['Math', 'CS', 'Bio']
conflicts = [('Math', 'CS'), ('Math', 'Bio')]
schedule = {'Math': 1, 'CS': 2, 'Bio': 2}

print("Valid Schedule:", is_valid(schedule, conflicts))
