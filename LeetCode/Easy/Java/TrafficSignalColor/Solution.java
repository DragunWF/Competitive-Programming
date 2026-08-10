// https://leetcode.com/problems/traffic-signal-color/description/

class Solution {
    public String trafficSignal(int timer) {
        if (timer == 0) {
            return "Green";
        } else if (timer == 30) {
            return "Orange";
        } else if (timer > 30 && timer <= 90) {
            return "Red";
        }
        return "Invalid";
    }
}