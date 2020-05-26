# your code goes here
s = input()

raw_votes = s.split(" ")
winner = ""
votes = {}


def get_key(case):
    match = []
    for key, value in votes.items():
        if value == case:
            match.append(key)

    return match


for candidate in raw_votes:
    if candidate not in votes:
        votes[candidate] = 1
    else:
        votes[candidate] += 1

vote_list = list(votes.values())
vote_list.sort(reverse=True)
finalists = get_key(vote_list[0])
finalists.sort()
print(finalists[0], votes[finalists[0]])
