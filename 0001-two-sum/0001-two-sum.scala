import scala.collection.mutable.Map

object Solution {
    def twoSum(nums: Array[Int], target: Int): Array[Int] = {
        val indexMap: Map[Int, Int] = Map()
        val numsLength = nums.size

        // Scala's for loop counters are inclusive??
        for (x <- 0 to numsLength - 1) {
            val num = nums(x)
            val counterpart = target - num

            if (indexMap.contains(counterpart) == true) return Array(x, indexMap(counterpart))
            else indexMap += (num -> x)
        }

        Array()
    }
}