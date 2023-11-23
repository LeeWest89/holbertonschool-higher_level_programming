#!/usr/bin/node
const num = process.argv.slice(2);

if (num.length === 0 || num.length === 1) {
  console.log(0);
} else {
  const nums = [];
  for (let i = 0; i < num.length; i++) {
    nums.push(parseInt(num[i], 10));
  }
  for (let i = 0; i < nums.length - 1; i++) {
    for (let j = 0; j < nums.length - i - 1; j++) {
      if (nums[j] < nums[j + 1]) {
        const temp = nums[j];
        nums[j] = nums[j + 1];
        nums[j + 1] = temp;
      }
    }
  }
  console.log(nums[1]);
}
