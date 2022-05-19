public class ValidBoomerang {
    static class Solution {
        public boolean isBoomerang(int[][] points) {
            int[] p0 = points[0];
            int[] p1 = points[1];
            int[] p2 = points[2];

            // distinctness check
            if (isSame(p0, p1) || isSame(p1, p2) || isSame(p0, p2)) {
                return false;
            }
            
            // special case vertical line
            if (p0[0] == p1[0] && p1[0] == p2[0]) {
                return false;
            }

            // sort the points
            if (p0[0] <= p1[0]) {
                if (p0[0] <= p2[0]) {
                    if (p1[0] <= p2[0]) {
                        // do nothing
                    } else {
                        p1 = points[2];
                        p2 = points[1];
                    }
                } else {
                    // 2 0 1
                    p0 = points[2];
                    p1 = points[0];
                    p2 = points[1];
                }
            } else if (p1[0] <= p2[0]) {
                if (p0[0] <= p2[0]) {
                    // 1 0 2
                    p0 = points[1];
                    p1 = points[0];
                } else {
                    // 1 2 0
                    p0 = points[1];
                    p1 = points[2];
                    p2 = points[0];
                }
            } else {
                // 2 1 0
                p0 = points[2];
                p2 = points[0];
            }

            // else get slope and compute normally
            double slope = (double)(p1[1] - p0[1]) / (double)(p1[0] - p0[0]);
            int delta = p2[0] - p0[0];
            if (p0[1] + delta * slope == p2[1]) {
                return false;
            }

            return true;
        }

        private boolean isSame(int[] a, int[] b) {
            return a[0] == b[0] && a[1] == b[1];
        }
    }

    public static void main(String[] args) {
        Solution solution = new Solution();
        
        int[][] case1 = {{1, 1}, {2, 3}, {3, 2}};
        int[][] case2 = {{1, 1}, {2, 2}, {3, 3}};
        assert solution.isBoomerang(case1);
        assert !solution.isBoomerang(case2);

        System.out.println("Passed");
    }
}