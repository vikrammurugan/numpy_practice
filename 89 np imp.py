import numpy as np
 
np.set_printoptions(linewidth=150)
stocks_startswith_P = np.array(
    [
        [
            'PEKAO',
            'PLPEKAO00016',
            '176379000',
            '9619710660',
            '6.185',
            '5.27',
            '9',
        ],
        [
            'PGE',
            'PLPGER000010',
            '796776000',
            '3561588720',
            '2.290',
            '2.88',
            '18',
        ],
        [
            'PGNIG',
            'PLPGNIG00014',
            '1624608000',
            '6072784704',
            '3.905',
            '1.56',
            '12',
        ],
        [
            'PKNORLEN',
            'PLPKN0000018',
            '289049000',
            '17701360760',
            '11.382',
            '12.44',
            '8',
        ],
        [
            'PKOBP',
            'PLPKO0000016',
            '857593000',
            '18807014490',
            '12.093',
            '10.49',
            '9',
        ],
        [
            'PLAY',
            'LU1642887738',
            '114151000',
            '3696209380',
            '2.377',
            '1.47',
            '16',
        ],
        [
            'PZU',
            'PLPZU0000011',
            '568305000',
            '17515160100',
            '11.262',
            '6.64',
            '6',
        ],
    ],
    dtype='<U12',
)
 
print(np.round(stocks_startswith_P[:, 4].astype(float).sum(), 2))