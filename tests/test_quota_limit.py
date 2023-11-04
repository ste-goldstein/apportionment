from apportionment.methods import quota
import numpy as np

nan = np.nan

votes  = [50, 200, 300, 400, 500]
seats = 145
limits = [nan, 12,  nan,  nan,  nan]

quota_regular = quota(votes, seats)
quota_limited = quota(votes, seats, limits=limits)
quota_limited_sum = sum(quota_limited)

votes  = [200, 50, 300, 400, 500]
seats = 145
limits = [nan, nan,  25,  nan,  nan]

quota_regular = quota(votes, seats)
quota_limited = quota(votes, seats, limits=limits)
quota_limited_sum = sum(quota_limited)