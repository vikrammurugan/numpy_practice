import numpy as np


A = np.array(
    [['PLW CDR 11B TEN', 'AMC LPP'], ['CDR PKO KGH', 'CCC QMK']],
    dtype=np.str_,
)

print(np.char.split(A))
