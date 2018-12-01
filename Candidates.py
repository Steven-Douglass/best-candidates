# This program uses Python lists which can contain elements of different types

def Candidates(voterOpinions, candidatesList):
    topScore = 0        # The current top score of the program
    currentScore = 0    # The score of the candidate being compared
    name = ""           # The name of the current candidate
    bestCandidates = [] # The list of the best candidates

    # clearCandidates() will erase all candidates that have been saved as potential best candidates.
    # This will occur if a new best candidate with a higher score is found.
    def clearCandidates():
        for i in range(0, len(bestCandidates)):
            bestCandidates[i] = 0
    
    # calculateScore will take two choices and determine if they agree, disagree, or are neutral
    def calculateScore(voterChoice, candidateChoice):
        score = 0
        if voterChoice - candidateChoice == 0 and voterChoice != 0:
            score += 1
        elif abs(voterChoice - candidateChoice) == 2:
            score -= 1
        return score

    # Calculate the score of the first candidate and use that as the topScore
    for i in range(0, len(voterOpinions)):
        currentScore += calculateScore(voterOpinions[i], candidatesList[0][i + 1])
    topScore = currentScore

    # Iterate through the list of candidates
    for candidate in candidatesList:
        name = candidate[0] # Store the name of the current candidate
        currentScore = 0    # Reset the current score to 0 for the current candidate

        # Calculate the overall score for the current candidate
        for i in range(0, len(voterOpinions)):
            currentScore += calculateScore(voterOpinions[i], candidate[i + 1])

        # Compare the overall score of the candidate to our top score
        if currentScore > topScore:
            clearCandidates()           # Erase the list of best candidates
            topScore = currentScore     # Set the new top score
            bestCandidates.append(name) # Add the current candidate to the empty best candidates list
        elif currentScore == topScore:
            bestCandidates.append(name) # Add the current candidate to the current best candidates list

    # Print the best candidates
    for bestCandidate in bestCandidates:
        print(bestCandidate)

Candidates([0, 0, 0, 1, 1, 1, -1, -1, -1, 1], [ ["Adams", 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                                                ["Grant", -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
                                                ["Polk", 1, -1, 1, -1, 1, -1, 1, -1, 1, -1],
                                                ["Jackson", 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],
                                                ["Taft", 0, -1, 0, -1, 0, -1, 0, -1, 0, -1],
                                                ["Ford", 1, 1, 1, 1, 0, 0, 0, 0, 0, 0],
                                                ["Madison", 0, 0, 0, 1, -1, 0, 0, -1, 1, 1]
                                                ])
                              
Candidates([0, 0, 0, 1, 1, 1, -1,  -1, -1, 1], [["1", 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                                                ["2", -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1],
                                                ["3", 1,  -1,   1,  -1,   1,  -1,   1,  -1,   1,  -1],
                                                ["4", 1,   0,   1,   0,   1,   0,   1,   0,   1,   0],
                                                ["5", 0,  -1,   0,  -1,   0,  -1,   0,  -1,   0,  -1],
                                                ["6",  1,   1,   1,   1,   0,   0,   0,   0,   0,   0],
                                                ["7",  0,   0,   0,   1,  -1,   0,   0,  -1,   1,   1]])