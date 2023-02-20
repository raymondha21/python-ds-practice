def mode(nums):
    """Return most-common number in list.

    For this function, there will always be a single-most-common value;
    you do not need to worry about handling cases where more than one item
    occurs the same number of times.

        >>> mode([1, 2, 1])
        1

        >>> mode([2, 2, 3, 3, 2])
        2
    """
    current_most = {}
    for num in nums:
        current_most[num] = current_most.get(num,0) + 1
    
    current_most = max(current_most.values())

    for (num,freq) in counts.items():
        if freq == max_value:
            return num