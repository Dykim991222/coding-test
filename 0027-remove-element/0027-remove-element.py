class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        '''
        숫자 배열 nums, 숫자 val
        nums 안에서 값이 val과 같은 모든 원소를 제자리에서 제거
        제거 끝나고 val이 아닌 원소개수 : k
        nums[:k]는 val이 아닌 값들이 위치해야됨.
        '''

        k = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k+=1

        return k
        