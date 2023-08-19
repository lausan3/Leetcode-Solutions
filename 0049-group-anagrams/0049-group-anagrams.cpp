class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        map<string, vector<string>> anagrams;

        for (int i = 0; i < strs.size(); i++) {
            // group strings/anagrams together by counting the letters in the string
            vector<int> charCount(26);
            for (int c = 0; c < strs[i].size(); c++) {
                charCount[strs[i][c] - 'a']++;
            }

            // get key to string's name in dictionary
            string key = "";
            for (int j = 0; j < charCount.size(); j++) {
                key.append(to_string(charCount[j]) + '#');
            }

            // push string to its place in the map
            anagrams[key].push_back(strs[i]);
        }

        // get final result vector by pushing the sorted strings
        vector<vector<string>> result;
        for (auto it = anagrams.begin(); it != anagrams.end(); it++) {
            result.push_back(it->second);
        }


        return result;
    }
};