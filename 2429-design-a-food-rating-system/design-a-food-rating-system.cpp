class FoodRatings {
public:
    FoodRatings(vector<string>& foods, vector<string>& cuisines, vector<int>& ratings) {
        int n = foods.size();
        for (int i = 0; i < n; i++) {
            string food = foods[i];
            string cuisine = cuisines[i];
            int rating = ratings[i];
            
            foodToCuisine[food] = cuisine;
            foodToRating[food] = rating;
            cuisineToSet[cuisine].insert({-rating, food});
        }
    }
    
    void changeRating(string food, int newRating) {
        string cuisine = foodToCuisine[food];
        int oldRating = foodToRating[food];
        
        cuisineToSet[cuisine].erase({-oldRating, food});
        foodToRating[food] = newRating;
        cuisineToSet[cuisine].insert({-newRating, food});
    }
    
    string highestRated(string cuisine) {
        return cuisineToSet[cuisine].begin()->second;
    }
    
private:
    unordered_map<string, string> foodToCuisine;
    unordered_map<string, int> foodToRating;
    unordered_map<string, set<pair<int, string>>> cuisineToSet;
};
