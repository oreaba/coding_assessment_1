def exercise1(person, people):
    affiliated_teams = []
    for p in people:
        if p.is_team: # we are only interested in checking teams that the individual belongs
            for m in p.members:
                # teams could have nested members
                # i.e. a team could be a sub-set of another team
                if m.is_team:
                    sub_team = [s_t.id for s_t in m.members]
                    if person.id in (sub_team):
                        affiliated_teams.append(p)
                else:
                    if m.displayname == person.displayname:
                        affiliated_teams.append(p)
    
    return affiliated_teams


def get_members(team):
    
