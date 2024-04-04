object Solution {
    def containsDuplicate(nums: Array[Int]): Boolean = {
        nums.foldLeft(Set.empty[Int])((acc: Set[Int], x: Int) => 
            if (acc contains x) acc else acc + x).size != nums.length
    }
}