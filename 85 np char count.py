import numpy as np


A = np.array(
    [
        ['#summer#time#mood', '#vibe'],
        ['#sport#time', '#good#time'],
        ['#event#summer', '#fast#move'],
    ]
)


print(np.char.count(A,"time"))