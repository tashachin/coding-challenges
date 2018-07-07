def counting_sort(the_list, max_value):
    """A basic implementation of counting sort."""
 
    # Creates an array that checks num of instances of any int up through max_value
    num_counts = [0] * (max_value + 1)
    
    # Increments count on first pass through input list
    for item in the_list:
        num_counts[item] += 1 

    sorted_list = []

    for item, count in enumerate(num_counts):
        print "this is the status of num_counts:", num_counts
        print "enumerating item:", item, "enumerating count:", count

        for _ in xrange(count):
            sorted_list.append(item)

    return sorted_list