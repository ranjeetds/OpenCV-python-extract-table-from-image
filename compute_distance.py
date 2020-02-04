import pandas as pd
import numpy as np
import copy

def _if_one(val):
    boolean = False
    if val == 1:
        boolean = True
    return boolean 

def get_nearest_less(row, i_start, j_start):
    nearest_elements = []
    counter_less = 0
    i_less, j_less = i_start, j_start
    j_l_f = 0
    counter = 0
    while j_less > 0:
        counter_less += 1
        j_less = j_less - 1
        if row[j_less] == 1:
            # print(j_less)
            j_l_f = j_less
            nearest_elements.append([i_start, j_l_f])
            counter = counter_less
            break
    return nearest_elements, counter

def get_nearest_more(row, i_start, j_start):
    nearest_elements = []
    counter_more = 0
    i_more, j_more = i_start, j_start
    j_m_f = 0
    counter = 0
    while j_more < len(row) - 1:
        counter_more += 1
        j_more = 1 + j_more
        if row[j_more] == 1:
            j_m_f = j_more
            nearest_elements.append([i_start, j_m_f])
            counter = counter_more
            break
    return nearest_elements, counter

    
def get_nearest_horizontal(row, i_start, j_start):
    _nless, _cless = get_nearest_less(row, i_start, j_start)
    _nmore, _cmore = get_nearest_more(row, i_start, j_start)
    # print("Cless, Cmore ", _cless, _cmore, _nless, _nmore)
    if _cless < _cmore or _cless == 0:
        nearest_elements = _nmore
        counter = _cmore
        # print(counter)
    elif _cless > _cmore or _cmore == 0:
        nearest_elements = _nless
        counter = _cless
    else:
        nearest_elements = []
        for i in _nless:
            nearest_elements.append(i)
        for i in _nmore:
            nearest_elements.append(i)
        counter = _cless
    # print(counter)
    return nearest_elements, counter

if __name__ == "__main__":

    df = pd.read_csv('output.csv')
    
    _bldg = np.array(df)

    i_start, j_start = map(int, input("Enter start location : ").split(' '))

    i_start = df.shape[0] - 1 - i_start

    _count = 0
    _ct = 0
    while i_start != 0:
        # print('start ',_count, i_start, j_start)
        _bool = _if_one(_bldg[i_start][j_start])

        if not _bool:
            _nearest, _cnt = get_nearest_horizontal(_bldg[i_start], i_start, j_start)
            # print("Nearest, cnt ", _nearest, _cnt)
            if _ct ==0:
                _count = _count + _cnt -1
            _ct = _ct + 1
            _c_old = _count
            for i in _nearest:
                _c_itr = 0
                i_start, j_start = i[0], i[1]
                i_start -= 1
                _c_itr += 1
                _n_nxt, _c_nxt = get_nearest_horizontal(_bldg[i_start], i_start, j_start)
                _c = _count + _c_itr + _c_nxt
                if i == 0:
                    _c_old = _c
                    _c = 0
            # print("_c_old, _c ", _c_old, _c)
            if _c_old < _c:
                i_start, j_start = _nearest[0][0], _nearest[0][1]
                _count = 1 + _count
                # print(_count)
            if _c_old > _c:
                i_start, j_start = _nearest[1][0], _nearest[1][1]
                _count = 1 + _count
                _c_old = _c
        else:
            i_start = i_start -1
            _count = 1 + _count
        # print('End ',_count, i_start, j_start)
        # print(_bldg[i_start][j_start])

print("Shortest distance to top floor is :: ", _count)
