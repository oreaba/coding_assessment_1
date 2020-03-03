def exercise1(person, people):
    affiliated_teams = []
    for p in people:
        if p.is_team:
            for m in p.members:
                if m.is_team:
                    sub_team = [s_t.id for s_t in m.members]
                    if person.id in (sub_team):
                        affiliated_teams.append(p)
                else:
                    if m.displayname == person.displayname:
                        affiliated_teams.append(p)
    
    return affiliated_teams

