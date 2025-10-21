class Solution(object):
    def leftRightDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        leftSum = [0]
        rightSum = [0]
        answer = []
        for i in range(len(nums)-1):
            leftSum.append(leftSum[-1] + nums[i])
        for i in range(len(nums)-1,0,-1):
            rightSum.append(rightSum[-1] + nums[i])
        rightSum.reverse()
        for i in range(len(nums)):
            answer.append(abs(leftSum[i]-rightSum[i]))
        return answer 