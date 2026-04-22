class Solution:
    def trap(self, height: List[int]) -> int:
        mxLeft = []
        mx = 0
        for h in height:
            mx = max(mx, h)
            mxLeft.append(mx)
        
        mxRight = []
        mx = 0
        for h in height[::-1]:
            mx = max(mx, h)
            mxRight.append(mx)
        mxRight = mxRight[::-1]

        vol = 0
        for i in range(len(height)):
            vol += min(mxLeft[i], mxRight[i]) - height[i]
            print(vol)
        
        return vol