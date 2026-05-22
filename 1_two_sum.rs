// https://leetcode.com/problems/two-sum/description/

use std::collections::HashMap;

struct Solution;

impl Solution {
    pub fn two_sum(nums: Vec<i32>, target: i32) -> Vec<i32> {
        let mut seen = HashMap::new();

        for (index, num) in nums.iter().enumerate() {
            let complement = target - num;

            if let Some(&previous_index) = seen.get(&complement) {
                return vec![previous_index as i32, index as i32];
            }

            seen.insert(*num, index);
        }

        vec![]
    }
}

fn main() {
    let nums = vec![2, 7, 11, 15];
    let target = 9;

    println!("{:?}", Solution::two_sum(nums, target));
}

#[cfg(test)]
mod tests {
    use super::Solution;

    #[test]
    fn finds_two_sum_examples() {
        assert_eq!(Solution::two_sum(vec![2, 7, 11, 15], 9), vec![0, 1]);
        assert_eq!(Solution::two_sum(vec![3, 2, 4], 6), vec![1, 2]);
        assert_eq!(Solution::two_sum(vec![3, 3], 6), vec![0, 1]);
    }
}
