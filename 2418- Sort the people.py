class Solution(object):
    def sortPeople(self, names, heights):
        result = []

        while heights:
            max_index = heights.index(max(heights))
            result.append(names[max_index])

            # remove used elements
            heights.pop(max_index)
            names.pop(max_index)

        return result
