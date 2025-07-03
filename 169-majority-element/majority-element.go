func majorityElement(nums []int) int {
    // Moore voting algorithm
	major := nums[0] // Assume that this is majority
	count_of_current_major := 1

	for _, n := range nums[1:] {
		if count_of_current_major == 0 {
			major = n
		}

		if n == major {
			count_of_current_major += 1
		} else {
			count_of_current_major -= 1
		}
	}

	return major
}