class Solution {
private:
    int _maxDepth(TreeNode* root, int depth) {
        if (!root) {
            return depth;
        }

        return max(_maxDepth(root->left, depth + 1), _maxDepth(root->right, depth + 1));
    }

public:
    int maxDepth(TreeNode* root) {
        return _maxDepth(root, 0);
    }
};