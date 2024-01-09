var reduce = function(nums, fn, init) {
    acc = init;
    for(let i=0;i<nums.length;i++){
        acc = fn(acc,nums[i]);
    }
    return acc;
};
