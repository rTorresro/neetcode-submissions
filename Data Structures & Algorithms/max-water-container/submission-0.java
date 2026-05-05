class Solution {
    public int maxArea(int[] height) {
        int rightHalf = height.length - 1;
        int leftHalf = 0;
        int maxArea = 0; 

        while (leftHalf < rightHalf) {

            // Calculate area 
            // Keep track of biggest area 
            // If the current area is bigger than the biggest area, biggest area = current area 
            
            int area = 0; 


            int width = rightHalf - leftHalf;

            if (height[leftHalf] < height[rightHalf]) {
                area = height[leftHalf] * width; 
            } else {
                area = height[rightHalf] * width; 
            }

            if (area > maxArea) {
                maxArea = area; 
            }

            if (height[leftHalf] < height[rightHalf]) {
                leftHalf++; 
            } else {
                rightHalf--; 
            }

             
        }

        return maxArea; 

    }
}