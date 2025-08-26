class Solution {
public:
    int areaOfMaxDiagonal(vector<vector<int>>& dimensions) {
        double maxDiag = 0;
        int maxArea = 0;

        for (auto& d : dimensions) {
            int l = d[0], w = d[1];
            double diag = sqrt(1.0 * l * l + 1.0 * w * w);
            int area = l * w;

            if (diag > maxDiag || (fabs(diag - maxDiag) < 1e-9 && area > maxArea)) {
                maxDiag = diag;
                maxArea = area;
            }
        }

        return maxArea;
    }
};
