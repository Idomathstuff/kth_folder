def compress(uncompressed):
    """Compress a string to a list of output symbols."""

    # Build the dictionary.
    dict_size = 256
    global dictionary
    dictionary = dict((chr(i), i) for i in range(dict_size))
    # in Python 3: dictionary = {chr(i): i for i in range(dict_size)}

    w = ""
    result = []
    for c in uncompressed:
        wc = w + c # c0 = A, wc = A |c1 = B, wc = AB | c2 = A, wc = ABA
        if wc in dictionary:
            w = wc # c_0 = A, w = A | c_1 = B, pass | c_2 = A, w = ABA|
        else:
            result.append(dictionary[w])  # c_1 = B, w = A, append(65) | c = A,  

            dictionary[wc] = dict_size
            dict_size += 1
            w = c #

    # Output the code for w.
    if w: # only runs after loop is done
        result.append(dictionary[w]) 
    return result



def decompress(compressed):
    """Decompress a list of output ks to a string."""
    from io import StringIO

    # Build the dictionary.
    dict_size = 256
    dictionary = dict((i, chr(i)) for i in range(dict_size))
    # in Python 3: dictionary = {i: chr(i) for i in range(dict_size)}

    # use StringIO, otherwise this becomes O(N^2)
    # due to string concatenation in a loop
    result = StringIO()
    w = chr(compressed.pop(0))
    result.write(w)
    for k in compressed:
        if k in dictionary:
            entry = dictionary[k]
        elif k == dict_size:
            entry = w + w[0]
        else:
            raise ValueError('Bad compressed k: %s' % k)
        result.write(entry)

        # Add w+entry[0] to the dictionary.
        dictionary[dict_size] = w + entry[0]
        dict_size += 1

        w = entry
    return result.getvalue()

st = 'B'*50


a = compress(st)
inv_map = {dictionary[k]: k  for k in dictionary.keys()}
# print(inv_map)
for x in a:
    print(inv_map[x],end='')
print(a)

