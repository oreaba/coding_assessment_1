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


member_names_list = []
member_list = []
def get_members(team):
    length = len(team.members)

    for m in range(length):
        if type(team.members[m].members) is list: # if the team has a team sub-set in members, loop inside the sub-sets
            get_members(team.members[m])

        else:
            if team.members[m].displayname in member_names_list: # break from the loop if team sub-sets are starting to repeat
                break

            else:
                member_names_list.append(team.members[m].displayname)
                member_list.append(team.members[m])
    
    return member_list    
