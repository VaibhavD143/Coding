#include<bits/stdc++.h>
using namespace std;

int main()
{
    int n;
    cin>>n;
    vector<int> lst(n+1);
    lst[0]=-1;
    for(int i=1; i<n+1; i++)
    {
        cin>>lst[i];
    }
    lst.push_back(-1);
    n=lst.size();
    vector<vector<int> > dp(n, vector<int>(n,0));

    for(int l=3; l<n+1; l++)
    {
        for(int i=0; i<n-l+1; i++)
        {
            int j=i+l-1;
            dp[i][j]=0;
            int mx=max(lst[i], lst[j]);
            int mn=min(lst[i], lst[j]);

            if(mn==-1) mn=0;
            if(mx==-1) mx=1;
            for(int k=i+1; k<j; k++)
            {
                int q= dp[i][k]+dp[k][j]+(lst[k]*mx)+mn;
                dp[i][j]=max(dp[i][j], q);
            }
       
        }
    }
    // for(int i=0; i<dp.size(); i++)
    // {
    //     for(int j=0; j<dp[0].size(); j++)
    //     {
    //         cout<<dp[i][j]<<" ";
    //     }

    //     cout<<endl;
    // }
    cout<<dp[0][n-1]<<endl;
    return 0;
}
