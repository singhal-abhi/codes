#include<iostream.h>

using namespace std;

/*
 * Complete the 'maximumPower' function below.
 *
 * The function is expected to return an INTEGER.
 * The function accepts STRING s as parameter.
 */

int maximumPower(string s) {
    int i,l=s.length(),m=0;
    int j=l;
    while(j)
    {
        for(i=0;i<l;i++)
            if(s[i]!='0')
             break;
        if(i>m)
            m=i;
        j--;
    }
    if(m==l)
        return -1;
    return m;
}

int main()
{
    ofstream fout(getenv("OUTPUT_PATH"));

    string s;
    getline(cin, s);

    int result = maximumPower(s);

    fout << result << "\n";

    fout.close();

    return 0;
}
