import scala.collection.mutable.Map

object Solution {
    def twoSum(nums: Array[Int], target: Int): Array[Int] = {
        val indexMap: Map[Int, Int] = Map()

        def recurse(currIndex: Int): Array[Int] = {
            if (currIndex >= nums.size) Array()

            if (indexMap.contains(target - nums(currIndex)) == true) return Array(currIndex, indexMap(target - nums(currIndex)))
            else indexMap += (nums(currIndex) -> currIndex)

            recurse(currIndex + 1)
        }
        
        recurse(0)
    }
}