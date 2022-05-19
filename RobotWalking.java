import java.util.*;

public class RobotWalking {
    public static void main(String[] args) {
        int[] commands1 = new int[] { 4, -1, 3 };
        int[][] obstacles1 = new int[][] {};
        int[] commands2 = new int[] { 4, -1, 4, -2, 4 };
        int[][] obstacles2 = new int[][] { { 2, 4 } };

        System.out.println(robotSim(commands1, obstacles1));
        System.out.println(robotSim(commands2, obstacles2));
    }

    public static int robotSim(int[] commands, int[][] obstacles) {
        int x = 0, y = 0;
        int maxDist = 0;
        int stepX = 0;
        int stepY = 1;
        Set<List<Integer>> obstaclesSet = new HashSet<>();
        for (int[] obstacle : obstacles) {
            List<Integer> o = List.of(obstacle[0], obstacle[1]);
            obstaclesSet.add(o);
        }

        for (int command : commands) {
            switch (command) {
                case -1:
                    // turn right
                    if (stepX != 0) {
                        stepY = (stepX == 1) ? -1 : 1;
                        stepX = 0;
                    } else {
                        stepX = (stepY == 1) ? 1 : -1;
                        stepY = 0;
                    }
                    break;
                case -2:
                    // turn left
                    if (stepX != 0) {
                        stepY = (stepX == 1) ? 1 : -1;
                        stepX = 0;
                    } else {
                        stepX = (stepY == 1) ? -1 : 1;
                        stepY = 0;
                    }
                    break;
                default:
                    for (int i = 0; i < command; i++) {
                        int newX = x + stepX;
                        int newY = y + stepY;
                        List<Integer> nextStep = List.of(newX, newY);
                        if (obstaclesSet.contains(nextStep)) {
                            break;
                        }
                        x = newX;
                        y = newY;
                    }
                    maxDist = Math.max(maxDist, x * x + y * y);
            }
        }

        return maxDist;
    }
}
