import time
import pyautogui

def auto_type_code(code: str, delay: float = 0.05):
    """
    Simulate typing code at the current cursor position.
    """
    print("You have 5 seconds to place the cursor where you want the code to be typed...")
    time.sleep(5)  # Give time to move cursor to desired location

    for line in code.splitlines():
        pyautogui.write(line, interval=delay)
        pyautogui.press("enter")

if __name__ == "__main__":
    cpp_code = r"""#include <bits/stdc++.h>
using namespace std;

// LeetCode 70. Climbing Stairs
class Solution {
public:
    int climbStairs(int n) {
        if (n <= 2) return n;
        vector<int> dp(n+1, 0);
        dp[1] = 1;
        dp[2] = 2;
        for (int i = 3; i <= n; i++) {
            dp[i] = dp[i-1] + dp[i-2];
        }
        return dp[n];
    }
};

int main() {
    Solution sol;
    cout << sol.climbStairs(5) << endl; // Example: Output = 8
    return 0;
}"""
    auto_type_code(cpp_code, delay=0.05)

