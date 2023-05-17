function twoSum(nums: number[], target: number): number[] {
    const dict = {}

    for (const { index, value } of nums.map((value, index) => ({ index, value }))) {
        const counterpart = target - value

        if (!dict.hasOwnProperty(counterpart)) {
            dict[value] = index
        } else {
            return [dict[counterpart], index]
        }
    }

    return []
};