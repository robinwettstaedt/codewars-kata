"""
You are looking for teammates for an oncoming intellectual game in which you will have to answer some questions.

It is known that each question belongs to one of the n categories. A team is called perfect if for each category there is at least one team member who knows it perfectly.

You don't know any category well enough, but you are going to build a perfect team. You consider several candidates, and you are aware of the categories each of them knows perfectly. There is no restriction on the team size, but smaller teams gain additional bonus points. Thus, you want to build a perfect team of minimal possible size. Find this size (and don't forget to count yourself!) or determine that it is impossible to form a perfect team from the candidates you have.

Input/Output
[input] integer n representing the number of categories

1 ≤ n ≤ 10.

[input] 2D integer array candidates

For each valid i, candidates[i] is an array of different integers representing indices of the categories which the ith candidate knows perfectly.

0 ≤ candidates.length ≤ 10,

0 ≤ candidates[i].length < n,

0 ≤ candidates[i][j] < n.

[output] an integer

The minimal possible size of the perfect team, or -1 ( or Nothing or a similar empty value ) if you can't build it.
"""



def perfect_team_of_minimal_size(n, candidates):
    
    if candidates is None: 
        return -1
    
    number_of_candidates = len(candidates)
    
    combinations = {1:[]}
    
    current_skills = []
    
    index = 1
    
    for candidate_number, candidate_skills in enumerate(candidates):
        for skill in candidate_skills:
            if skill not in current_skills:
                current_skills.append(skill for skill in candidate_skills)
                combinations[index] += [candidate_number]
                
                
    values = combinations.values() 
        
    best_combination = min(len(value) for value in values)
    
    return best_combination + 1