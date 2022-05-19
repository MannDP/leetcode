public class Main {

    static class Palindrome2 {
        public boolean validPalindrome(String s) {
            // test whether the string itself is a palindrome
            if (isPalindrome(s)) {
                return true;
            }
    
            // else find the first "breaking" character, and try to replace it
            for (int i = 0, j = s.length() - 1; i < j; i++, j--) {
                if (s.charAt(i) != s.charAt(j)) {
                    return isPalindrome(removeChar(s, i)) || isPalindrome(removeChar(s, j));
                }
            }

            // we should never get here, but to make the compiler happy
            return false;
        }

        private String removeChar(String s, int idx) {
            String pc1 = idx == 0 ? "" : s.substring(0, idx);
            String pc2 = idx == s.length() - 1 ? "" : s.substring(idx + 1, s.length());
            return pc1 + pc2;
        }
    
        // return whether the string is a palindrome
        private boolean isPalindrome(String s) {
            return (new StringBuilder(s)).reverse().toString().equals(s);
        }
    }
    public static void main(String[] args) {
        Solution s = new Solution();
        // run with -ea flag to enable assertions
        assert s.validPalindrome("aba");
        assert !s.validPalindrome("abc");
        assert s.validPalindrome("abca");
        System.out.println("Passed!");
    }
}