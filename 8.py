
import numpy as np
from matplotlib import pyplot as plt

with open ("settings.txt", "r") as settings:
    tmp = [float(i) for i in settings.read().split("\n")]

volt = np.loadtxt("data.txt", dtype = int)
volt = volt/256 * 3.3
fig, ax = plt.subplots(figsize=(16, 10), dpi=400)

with open ("settings.txt", "r") as settings:
    dT = float(settings.readline())

tmp = np.arange(0, len(volt)*dT, dT)

xmax = np.argmax(tmp)*dT
qmax = volt.argmax()

str1 = "Время зарядки =" + str(qmax*dT) + "с" 
str2 = "Время разрядки =" + (str((len(volt)-qmax)*dT)) + "с"

ax.set_title("Процесс заряда и разряда конденсатора в RC-цепочке")
ax.set_xlabel("Время, с")
ax.set_ylabel("Напряжение, В")

ax.plot(tmp, volt, color = 'steelblue', label="V(t)", marker = '*', markevery =15)
ax.minorticks_on()

ax.grid(which='major', color = 'k', linewidth = 0.5)
ax.grid(which='minor', color = 'k', linestyle = ':')

ax.legend()
ax.set(xlim=(0, xmax + 4), ylim=(0, 3.3))

plt.text(0.3*len(tmp)*dT, 2, str1)
plt.text(0.3*len(tmp)*dT, 1.5, str2)

ax.set_facecolor('mediumaquamarine')

fig.savefig("graph.svg")
plt.show()
