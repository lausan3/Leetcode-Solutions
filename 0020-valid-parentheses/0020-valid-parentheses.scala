object Solution {

    def isValid(s: String): Boolean = {
        val mappings: Map[Char, Char] = Map(
            ('}' -> '{'),
            (']' -> '['),
            (')' -> '(')
        )

        def recurse(str: String, stk: List[Char]): Boolean = {
            if (str.length <= 0) return stk.isEmpty

            val char = str.charAt(0)

            if (!mappings.contains(char)) recurse(str.substring(1), char :: stk)
            else if (stk.nonEmpty && stk.head == mappings(char)) recurse(str.substring(1), stk.drop(1))
            else false
        }

        recurse(s, List.empty)
    }
}