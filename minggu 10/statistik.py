import numpy as np
import statistics

print(np.mean([1,3,5,7,9,11,11,13]))
print(np.median([1,3,5,7,9,11,11,13]))
print(statistics.mode([1,3,5,7,9,11,11,13]))
print(np.std([1,3,5,7,9,11,11,13]))
print(np.var([1,3,5,7,9,11,11,13]))
print(np.cov([1,3,5,7,9,11,11,13]))

tinggibadan = [187,155,165,158]
ratatinggibadan = np.mean(tinggibadan)
tengahtinggibadan = np.median(tinggibadan)
print(ratatinggibadan)
print(tengahtinggibadan)