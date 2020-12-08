import survey

table = survey.Pregnancies()
table.ReadRecords()
print('Number of pregnancies', len(table.records))

outcomeList = list(filter(lambda x: x.outcome == 1, table.records))
print('Number of babies', len(outcomeList))

firstList = list(filter(lambda x: x.birthord == 1, outcomeList))
otherList = list(filter(lambda x: x.birthord != 1, outcomeList))
print('Number of first babies', len(firstList))
print('Number of others', len(otherList))

firstPrg = sum(map(lambda x: x.prglength, firstList)) / len(firstList)
otherPrg = sum(map(lambda x: x.prglength, otherList)) / len(otherList)

print('First babies', firstPrg)
print('Others', otherPrg)
print('Difference in hours', (firstPrg - otherPrg) * 7 * 24)
