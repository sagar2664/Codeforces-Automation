#include <bits/stdc++.h>
using namespace std;
#define int long long
const int mod = 1e9 + 7;
#define endl '\n'

void solve()
{
    int n;
    cin >> n;
    int arr[n];
    for (int i = 0; i < n; i++)
        cin >> arr[i];
    sort(arr, arr + n);
    int ans = 0;
    for (int i = 0; i < n; i++)
    {
        if(arr[i]==0)
        continue;
        else if (arr[i] == 1)
        {
            if (i < n - 1)
                arr[i + 1] -= 1;
            ans++;
        }
        else
            ans++;
    }
    cout << ans << endl;
}

signed main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);

    int _t;
    cin >> _t;
    while (_t--)
        solve();
}