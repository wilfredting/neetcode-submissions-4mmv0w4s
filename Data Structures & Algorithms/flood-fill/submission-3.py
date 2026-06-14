class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        COLOR = image[sr][sc]

        if COLOR == color:
            return image

        ROWS, COLS = len(image), len(image[0])

        def dfs(row, col):
            if (
                min(row, col) < 0
                or row >= ROWS
                or col >= COLS
                or image[row][col] != COLOR
            ):
                return

            image[row][col] = color

            dfs(row + 1, col)
            dfs(row - 1, col)
            dfs(row, col + 1)
            dfs(row, col - 1)

        dfs(sr, sc)

        return image
