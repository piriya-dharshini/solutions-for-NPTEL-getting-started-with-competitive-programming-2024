#include <bits/stdc++.h>
#include<iostream>
#include<map>
#include<set>
#include<algorithm>
#include<vector>
#include<string>
#define loop(i,a,b) for(long long i = a; i<b; i++)
#define ll long long
#define mod 1000000007
#define END std::cout<<endl
using namespace std;


void decode()
{
    long long t ;
    cin>>t;
    while (t--)
    {
        long long n,m ;
        cin>>n>>m ;
    
        long long A[n] ;
        vector<pair<long long,long long>> v(m) ;

    loop(i,0,n)
    {
        cin>>A[i] ;
    }

    loop(i,0,m)
    {
        long long x ;
        cin>>x ;
        v[i].first = x ;
    }

    loop(i,0,m)
    {
        long long x ;
        cin>>x ;
        v[i].second = x ;
    }

    sort(A,A+n) ;
    reverse(A,A+n) ;
    sort(v.begin(), v.end()) ;
    reverse(v.begin(), v.end()) ;

    long long tr = 0 , oc = 0 ;
    long long i = 0 , j = 0 ;
    while(i < n && j < m )
    {
        long long x = A[i] ;
        long long y = v[j].first ;
        long long z = v[j].second ;

        if(z > 0)
        {
            oc+= abs(x-y) ;
            tr += min(x,y) ;
            v[j].second -= 1 ;
            i++ ;
        }
        else
        {
            j++ ;
        }
    }

    cout<<tr<<" "<<oc<<endl;

    }
    
}

int main()
{
     decode(); 
 
}