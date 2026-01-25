class Solution:
    def numberOfPatterns(self, m: int, n: int) -> int:
        jump = [[0 for _ in range(10)] for _ in range(10)]

        # Initialize the jump over numbers for all valid jumps
        jump[1][3] = jump[3][1] = 2
        jump[4][6] = jump[6][4] = 5
        jump[7][9] = jump[9][7] = 8
        jump[1][7] = jump[7][1] = 4
        jump[2][8] = jump[8][2] = 5
        jump[3][9] = jump[9][3] = 6
        jump[1][9] = jump[9][1] = jump[3][7] = jump[7][3] = 5

        visited_numbers = [False] * 10
        total_patterns = 0

        # count corners (1, 3, 7, 9)
        total_patterns += (
            self.count_patterns_from_number(1, 1, m, n, jump, visited_numbers)
            * 4
        )

        # count edges (2, 4, 6, 8)
        total_patterns += (
            self.count_patterns_from_number(2, 1, m, n, jump, visited_numbers)
            * 4
        )

        # count from center (5)
        total_patterns += self.count_patterns_from_number(5, 1, m, n, jump, visited_numbers)

        return total_patterns

    def count_patterns_from_number(
        self,
        current_num: int,
        current_len: int,
        min_len: int, 
        max_len: int,
        jump: List[List[int]],
        visited_numbers: List[bool]
    ):
        if current_len > max_len:
            return 0

        valid_patterns = 0

        if current_len >= min_len:
            valid_patterns += 1
        
        visited_numbers[current_num] = True

        for next_num in range(1, 10):
            jump_over_num = jump[current_num][next_num]

            # try next number if current pattern has num or not a jump move
            if not visited_numbers[next_num] and (
                jump_over_num == 0 or
                visited_numbers[jump_over_num]
            ):
                valid_patterns += self.count_patterns_from_number(
                    next_num,
                    current_len + 1,
                    min_len,
                    max_len,
                    jump,
                    visited_numbers
                )

        # backtrack
        visited_numbers[current_num] = False

        return valid_patterns