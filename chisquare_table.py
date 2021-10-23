import scipy.stats as stats
#first player
my_rolls_expected = [46.5, 46.5, 46.5, 46.5, 46.5, 46.5]
my_rolls_actual =  [59, 63, 37, 38, 32, 50]
print(stats.chisquare(my_rolls_actual, my_rolls_expected))

#Second player
opp_rolls_expected = [50.5,50.5,50.5,50.5,50.5,50.5]
opp_rolls_actual =  [39,39,46,54,53,72]
print(stats.chisquare(opp_rolls_actual, opp_rolls_expected))
