def compactify(word, b, k):
    """ `word` is a integer whose bits form a sequence of b-bit strings.
    Each string is a (b-1)-bit integer (or garbage) followed by 1 check bit.
    Compactifies the integers with check bits 1 into the right hand
    side of the word.

    Maybe currently only works if garbage is always 0? Easy to change that.

    Testcase:
    compactify(0b0001001100000101000001110000000000001001000000001011,4,13)"""
    def pp(thing):
        ''' Pretty print a word as an array of its b-bit integers.
        For debugging purposes. '''
        L = []
        for i in xrange(k):
            L.append(int(thing % (2**b)))
            thing /= (2**b)
        return L[::-1]
    print pp(word)
    if 2**b <= k: print "Warning: maybe not enough space."
    allOnes = ((1<<k*b) - 1)/((1<<b) - 1) # has 1 in each check bit spot
    checkToInt = (1<<b) - 1 # checkToInt * allOnes = 1 at every bit
    intPlaces = word & allOnes
    valley = ~word
    valleyPlaces = valley & allOnes
    COUNT = valleyPlaces * allOnes
    print pp(COUNT), "COUNT"
    powerOf2 = 1
    stage = 0
    allOnesShift = allOnes
    while powerOf2 < k:
        # currently valleys are divisible by powerOf2
        MASK = (COUNT & allOnesShift) >> stage
        MASK <<= b # or MASK &= (allOnes & word)
        MASK *= checkToInt
        word = ((word & MASK) >> (b*powerOf2)) | (word & ~MASK)
        stage += 1
        allOnesShift <<= 1
        powerOf2 <<= 1
        print pp(MASK), "Mask"
        print pp(word)
