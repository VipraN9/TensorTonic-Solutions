import numpy as np

# def pad_sequences(seqs, pad_value=0, max_len=None):
#     """
#     Returns: np.ndarray of shape (N, L) where:
#       N = len(seqs)
#       L = max_len if provided else max(len(seq) for seq in seqs) or 0
#     """
    # n = len(seqs)
    # if max_len!=None :
    #     l = max_len
    #     for seq in seqs:
    #         d = l - len(seq)
    #         if d>=0:
    #             for i in range (d):
    #                 seq.append(pad_value)
    #         else:
    #             for i in range(d):
    #                 seq = np.delete(seq, -1)
    #     return seqs
    # else:
    #     l = max(len(seq) for seq in seqs)
    #     for seq in seqs:
    #         d = l - len(seq)
    #         for i in range (d):
    #             seq.append(pad_value)
    #     return seqs


def pad_sequences(seqs, pad_value=0, max_len=None):
    if not seqs:
        return np.empty((0, 0), dtype=int)

    # 1. Determine target length (L)
    if max_len is None:
        L = max(len(s) for s in seqs) if seqs else 0
    else:
        L = max_len

    N = len(seqs)
    result = np.full((N, L), pad_value, dtype=int)

    for i, seq in enumerate(seqs):
        if len(seq) == 0 or L == 0:
            continue
        
        # Take the smaller of the sequence length or max_len
        trunc_len = min(len(seq), L)  #calculate how much of the sequence will actually fit. If the sequence is length 10 but our grid only allows length 5, trunc_len becomes 5.
        result[i, :trunc_len] = seq[:trunc_len]  #This selects row i and the first few slots (from start to trunc_len).
        #seq[:trunc_len]: This takes the first few numbers from your original sequence.The Assignment (=): It "pastes" the numbers from your list directly into the grid.


    return result

    # Your code here
    pass