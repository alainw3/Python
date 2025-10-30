if __name__ == '__main__':
    records=[]
    scores=[]
    for _ in range(int(input())):
        name = input()
        score = float(input())
        
        records.append([name,score])
        scores.append(score)
        
    #print(records)
    second_lowest_score = sorted(set(scores))[1]
    #print(second_lowest_score)
    #students_second_lowest = sorted([x  for  x in records if x[1] == second_lowest_score])
    students_second_lowest = sorted(filter(lambda x : x[1]==second_lowest_score,records ))
    #print(students_second_lowest)
    for x in students_second_lowest:
        print(x[0])