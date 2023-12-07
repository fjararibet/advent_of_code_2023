#include <bits/stdc++.h>
using namespace std;

int main(int argc, char **argv) {
    string n;
    vector<string> v;
    while (getline(cin, n)) {
        v.push_back(n);
    }
    // for (int i = 0; i < v.size(); i++) {
    //     cout << v[i] << endl;
    // }
    
    stringstream ss(v[0]);
    vector<string> seeds_line;
    while(getline(ss, n, ':')) {
        seeds_line.push_back(n);
    }
    vector<string> seeds;
    stringstream sss(seeds_line[1]);
    while(getline(sss, n, ' ')) {
        seeds.push_back(n);
    }
    vector<int> seeds_int;
    for (int i = 1; i < seeds.size(); i++) {
        seeds_int.push_back(stoi(seeds[i]));
    }


}
