# ONLY EDIT FUNCTIONS MARKED CLEARLY FOR EDITING

import numpy as np

# modify this function, and create other functions below as you wish
def question01(portfolios):
  # need to optimise lots, dont go over same numbers etc.
  for p1 in portfolios:
        for p2 in portfolios:
            total = p1 ^ p2
            if total > answer:
                answer = total

  return answer
