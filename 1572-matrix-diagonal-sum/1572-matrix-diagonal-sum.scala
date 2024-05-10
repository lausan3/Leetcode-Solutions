object Solution {
    def diagonalSum(mat: Array[Array[Int]]): Int = {
        val rows = mat.length - 1
        val cols = mat(0).length - 1

        def recurse(sum: Int, r1: Int, c1: Int, r2: Int, c2: Int): Int = {
            if (r1 > rows && c1 > cols && r2 > rows && c2 < 0) return sum

            // Add once if diagonals are intersecting
            val toAdd = if (r1 == r2 && c1 == c2) {
                mat(r1)(c1)
            } else {
                mat(r1)(c1) + mat(r2)(c2)
            }

            recurse(sum + toAdd, r1 + 1, c1 + 1, r2 + 1, c2 - 1)
        }

        recurse(0, 0, 0, 0, cols)
    }
}