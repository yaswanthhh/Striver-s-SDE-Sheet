class Solution
{
public:
    void func(int index, int sum, vector<int> arr, int N, vector<int>& res) {
        if(index == N) {
            res.push_back(sum);
            return;
        }
        //If picked
        func(index+1, sum+arr[index], arr, N, res);
        //if not picked dont add sum just increment index
        func(index+1, sum, arr, N, res);
    }
    
    vector<int> subsetSums(vector<int> arr, int N)
    {
        vector<int> res;
        func(0, 0, arr, N, res);
        sort(res.begin(), res.end());
        return res;
    }
};
