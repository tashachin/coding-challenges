def  lemur(branches):
    """Return number of jumps needed."""

    assert branches[0] == 0, "First branch must be alive"
    assert branches[-1] == 0, "Last branch must be alive"

    # given a bunch of 0s and 1s, i have to return the num of jumps it takes the lemur
    # to reach the last branch (last 0)
    # she can only hop a distance of two branches max
    # 0 - 0 - 1 - 0 - 0 - 1 - 0
    # >>> 4
    # in a simpler problem, if there were ONLY 0s, the max num is half the 0s
    # 0 - 0 - 0 - 0
    # >>> 2
    # if i add the 1s, how does the logic change?
    # 0 - 1 - 0 - 1 - 0 - 1 - 0
    # >>> 3
    # HINT: there will never be two 1s in a row
    # one-to-three dead branches have the impact of one additional hop
    # every three dead branches should add one hop
    # 0 - 1 - 0 - 0 - 1 - 0 - 0 - 1 - 0 - 1 - 0
    # >>> 6
    # 0 - 0 - 0 - 0 - 0 - 0 - 0
    # >>> 3
    # in this case, though, the 1s doubled the hops BECAUSE of their placement
    # the lemur can't hop two at a time because it has to scoot over one and then bound over the branch
    # if the pattern goes 0, 1, 0, 1 the dead branches add one hop
    # if the pattern goes 0, 1, 0, 0, 1, the dead branches double the hops
    # How do I check for both cases?
    # HINT: Involves loops and lists.

    if len(branches) < 2:  # If she's already where she needs to be, return zero jumps
        return 0

    if 1 not in set(branches):  # Let's handle our simplest case where no dead branches are involved
        return len(branches) / 2