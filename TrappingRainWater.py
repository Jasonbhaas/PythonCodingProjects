class Solution:
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        l=0
        r= len(height) -1
        level = min(height[l], height[r])
        water = 0


        while(l<r):
            if (height[l] <= height[r]):
                lowerEdge = height[l]
                l += 1
            else:
                lowerEdge = height[r]
                r -= 1

            if lowerEdge > level:
                level = lowerEdge
            water += level - lowerEdge

        return water