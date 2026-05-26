class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # calculate maximum area
        # max area = distance between indices * smallest height
        # two pointers from right and left 
        # calculate area for every 2 pointer 
        # get max area

        start = 0
        end = len(heights) - 1

        max_area = 0

        while (start < end):
            dist = end - start
            if (heights[start] < heights[end]):
                area = dist * heights[start]
                start = start + 1
            else:
                area = dist * heights[end]
                end = end - 1
            if (area > max_area):
                max_area = area
                

        return max_area
            

        