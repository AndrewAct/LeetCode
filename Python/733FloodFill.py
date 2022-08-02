class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        row = len(image)
        col = len(image[0])
        cur_color = image[sr][sc]
        print(cur_color)
        # if (image[sr][sc] == color) return image
        
        def fill(sr, sc):
            if sr not in range(row): return 
            if sc not in range(col): return 
            if image[sr][sc] == color: return 
            if image[sr][sc] != cur_color: return 
            
            image[sr][sc] = color 
            
            fill(sr+1,sc)
            fill(sr-1,sc)
            fill(sr,sc+1)
            fill(sr,sc-1)
        fill(sr,sc)
        return image