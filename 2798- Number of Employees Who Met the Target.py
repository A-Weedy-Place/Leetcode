def numberOfEmployeesWhoMetTarget(self, hours, target):
    """
    :type hours: List[int]
    :type target: int
    :rtype: int
    """
    n = 0
    for i in hours:
        if i >= target:
            n += 1
    return n 