from eazy.filters import FilterFile
import matplotlib.pyplot as plt
import fsps

res = FilterFile(file='needed_curves', path='')
print(len(res.filters))
fig = plt.figure(figsize=(21,9))
for i in res:
    plt.plot(i.wave, i.throughput)

plt.grid()
plt.xscale('log')
plt.show()