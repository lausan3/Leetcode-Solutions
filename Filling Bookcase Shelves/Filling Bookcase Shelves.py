class Solution:
    def minHeightShelves(self, books: List[List[int]], shelfWidth: int) -> int:
        """
        Brute Force recursive solution:

        For each book, we have the choice to put it on the first shelf of the height or 
         greater, or start a new shelf otherwise.

        Combine this with DP and you have the solution.

        Time: O(N * W) where W is the shelf width because there's a chance to have each book
         on the same shelf.
        Space: O(N * W) for the memo array.
        """
        memo = [[0 for _ in range(shelfWidth + 1)] for _ in range(len(books))] 

        def backtrack(i: int, remaining_shelf_width: int, max_height: int) -> int:
            if i >= len(books):
                return max_height
            if memo[i][remaining_shelf_width] != 0:
                return memo[i][remaining_shelf_width]

            width, height = books[i]

            # for every shelf, put it on the shelf if there's space and can fit.
            exist_shelf = float('inf')
            if width <= remaining_shelf_width:
                exist_shelf = backtrack(i + 1, remaining_shelf_width - width, max(max_height, height))

            # create new shelf
            new_shelf = backtrack(i + 1, shelfWidth - width, height) + max_height

            memo[i][remaining_shelf_width] = min(new_shelf, exist_shelf)
            return memo[i][remaining_shelf_width]

        return backtrack(0, shelfWidth, 0)