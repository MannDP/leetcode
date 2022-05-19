class Solution {
public:
	vector<int> twoSum(vector<int>& nums, int target) {
		vector<int> indices = {};
		map<int, int> valueIndexMap;
		for (int i = 0; i < nums.size(); i++) {
			int value = nums[i];
			int diff = target - value;
			if (valueIndexMap.count(diff)) {
				int firstIndex = valueIndexMap[diff];
				if (valueIndexMap[diff] != i) {
					indices.emplace_back(firstIndex);
					indices.emplace_back(i);
					break;
				}
			}
			valueIndexMap[value] = i;
		}
		return indices;
	}
};
