#include <iostream>

using namespace std;

int main() {
    int n, q;
    cin >> n >> q;
    int nums[n];
    int a, b, c;
    int ans = 0;
    for (int k = 0; k < n; k++) {
        cin >> nums[k];
    }
    for (int i = 0; i < q; i++) {
        cin >> a;
        if (a == 1) {
            cin >> b;
            cout << nums[b - 1] << endl;
        } else if (a == 2) {
            cin >> b;
            ans = 0;
            for (int l = 0; l < n; l++) {
                if (b == nums[l]) {
                   ans = l + 1;
                   break; 
                }
            }
            cout << ans << endl;
        } else {
            cin >> b >> c;
            for (int j = b - 1; j < c; j++) {
                cout << nums[j] << " ";
            }
            cout << endl;
        }
    }
    return 0;
}