var summaryRanges = function(nums) {
    let re = [];
    for(let i=0;i<nums.length;i++){
        let start = nums[i];
        while(i+1<nums.length && nums[i]+1 == nums[i+1]){
            i++;
        }
        if(start != nums[i]){
            re.push(start+"->"+nums[i]);
        }
        else{
            re.push(""+start);
        }
    }
    return re;
};
