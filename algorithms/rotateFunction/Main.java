public class Main {
    public static void main(String[] args) {
        int[] input = new int[] { -2147483648, -2147483648 };
        int[] input2 = new int[] { 4, 3, 2, 6 };
        System.out.println(maxRotateFunction(input));
        System.out.println(maxRotateFunction(input2));
    }

    public static int maxRotateFunction(int[] nums) {
        int arrSum = 0;
        int max = 0;
        for (int i = 0; i < nums.length; i++) {
            arrSum += nums[i];
            max += i * nums[i];
        }

        int fk = max;
        int idxToRemove = nums.length - 1;
        for (int i = 1; i < nums.length; i++) {
            fk = fk + arrSum - nums.length * nums[idxToRemove];
            --idxToRemove;
            if (fk > max) {
                max = fk;
            }
        }

        return max;
    }
}
