class Solution {
public:
    void func(int index, vector<int>& ds, vector<int> nums, vector<vector<int>>& ans) {
        if(index==nums.size()) {
            ans.push_back(ds);
            return;
        }
        ds.push_back(nums[index]);
        func(index+1, ds, nums, ans);
        ds.pop_back();
        while(index+1 < nums.size() && nums[index]==nums[index+1])
            index++;
        func(index+1, ds, nums, ans);
    }
    
    vector<vector<int>> subsetsWithDup(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        vector<vector<int>> ans;
        vector<int> ds={};
        func(0, ds, nums, ans);
        sort(ans.begin(), ans.end());
        return ans;
    }
};
