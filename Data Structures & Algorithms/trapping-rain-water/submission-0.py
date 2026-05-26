class Solution:
    def trap(self, height: List[int]) -> int:
        # water gets trapped if the next bar is same height or more than the same height
        # find the next bar that is either at the same or higher height
        # two pointers to find area

        # water in each bar = closest wall - height of bar (less than wall)

        i = 0
        j = len(height) - 1

        area = 0

        maxl = i
        maxr = j

        while i < j:
            if height[i] < height[j]:
                if height[maxl] > height[i]:
                    area += height[maxl] - height[i]
                else:
                    maxl = i
                i += 1
            else:
                if height[maxr] > height[j]:
                    area += height[maxr] - height[j]
                    j -= 1
                else:
                    maxr = j
                    j -= 1

        return area
            

        