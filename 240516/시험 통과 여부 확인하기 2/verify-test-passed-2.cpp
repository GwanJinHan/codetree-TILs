#include <iostream>
using namespace std;
int main() {
    int std_num;
    int score_sum;
    int cnt = 0;
    int t = 0;

    cin >> std_num;

    for (int i = 0; i < std_num; i++) {
        score_sum = 0;
        for (int j = 0; j < 4; j++) {
            cin >> t;
            score_sum += t; 
        }
        if (score_sum / 4 >= 60) {
            cnt += 1;
            cout << "pass" << endl;
        } else {
            cout << "fail" << endl;
        }
    }
    
    cout << cnt;
    return 0;
}