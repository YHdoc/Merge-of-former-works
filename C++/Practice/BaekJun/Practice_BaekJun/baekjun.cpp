//���� 1157��
// #include<iostream>
// #include<string>
// #include<cstring>
// using namespace std;
// #define MAX_R 26 
// int main()
// {
//     int word[MAX_R]={};
//     string anyword;
//     cin >> anyword;
//     for(int i=0; i<anyword.length(); i++){
//         anyword[i] = (char)tolower(anyword[i]);
//         int idx = anyword[i]-97;
//         word[idx]+=1;
//     }
//     // for (int i=0; i<MAX_R; i++){
//     //     cout << word[i];
//     // }
//     // cout << endl;
//     int minA = 0, cnt = 0;
//     for (int i=0; i<MAX_R; i++){
//         if(word[minA]<word[i]) minA = i;
//     }
//     // cout<<minA<<endl;
//     for (int i=0; i<=MAX_R; i++){
//         // cout<<i<<" ";
//         if(i==minA) continue;
//         else if(word[minA]==word[i]){
//             cout<<'?'; break;
//         }
//         if(i==MAX_R) cout << (char)(minA+65);
//     }
//     return 0;
// }


//���� 1152��
/*#include<iostream>
#include<string>
using namespace std;

int main()
{
    string str;
    getline(cin, str);
    int StrLen = str.length(), cnt=0;
    for(int i=0; i<StrLen; i++){
        if((char)str[i]==' ') cnt++;
    }
    if((char)str[StrLen-1]==' ') cnt-=1;
    if((char)str[0]==' ') cnt-=1;
    cout << cnt+1;

    return 0;
}*/

//���� 2908��
/*
#include<iostream>
#include<string>
#include<algorithm>

using namespace std;

int main()
{
    int a,b;
    cin>>a>>b;
    string str_a = to_string(a), str_b = to_string(b);
    reverse(str_a.begin(), str_a.end()); reverse(str_b.begin(), str_b.end());
    a=stoi(str_a); b=stoi(str_b);
    if (a>b) cout<<a;
    else cout<<b;
    
    return 0;
}*/

//���� 5622��
/*#include<iostream>
#include<string>
#include<typeinfo>

using namespace std;

int main()
{
    string DialNum; cin >> DialNum;
    int NumLength = DialNum.length();
    // char *DNumArr = new char[NumLength];

    // for (int i=0; i<NumLength; i++){
    //     DNumArr[i] = (char)DialNum[i];
    // }
    int TimeRequired=0;
    for (int i=0; i<NumLength; i++){
        if (DialNum[i]=='A'||DialNum[i]=='B'||DialNum[i]=='C') TimeRequired += 3;
        else if(DialNum[i]=='D'||DialNum[i]=='E'||DialNum[i]=='F') TimeRequired += 4;
        else if(DialNum[i]=='G'||DialNum[i]=='H'||DialNum[i]=='I') TimeRequired += 5;
        else if(DialNum[i]=='J'||DialNum[i]=='K'||DialNum[i]=='L') TimeRequired += 6;
        else if(DialNum[i]=='M'||DialNum[i]=='N'||DialNum[i]=='O') TimeRequired += 7;
        else if(DialNum[i]=='P'||DialNum[i]=='Q'||DialNum[i]=='R'||DialNum[i]=='S') TimeRequired += 8;
        else if(DialNum[i]=='T'||DialNum[i]=='U'||DialNum[i]=='V') TimeRequired += 9;
        else if(DialNum[i]=='W'||DialNum[i]=='X'||DialNum[i]=='Y'||DialNum[i]=='Z') TimeRequired += 10;
    }
    cout << TimeRequired;
    // delete[] DNumArr;
    return 0;
}*/

/*#include <iostream>
#include<vector>
#include<cmath>
using namespace std;

int main() {
	iostream::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);
	int arr[26] = { 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 7, 8, 8, 8, 8, 9, 9, 9, 10, 10, 10, 10 };
	int sum = 0;
	string s;

	cin >> s;

	for (int i = 0; i < s.length(); ++i) {
		int index = s[i] - 65;
		sum += arr[index];
	}

	cout << sum << endl;

	
	return 0;
}*/



//���� 1076��
/*#include<iostream>
using namespace std;
int CtoN(string ColorN);
int main()
{
    // int black=0,brown=1,red=2,orange=3,yellow=4,green=5,blue=6,violet=7,grey=8,white=9;
    int ColorList[10]={0,1,2,3,4,5,6,7,8,9};
    long long sum=0;
    string ColorName;
    for (int i=0; i<3; i++){
        cin>>ColorName;
        if (i==0) sum+=10*CtoN(ColorName);
        else if (i==2) {
            for (int j=0; j<CtoN(ColorName); j++) sum*=10;
        }
        else sum+=CtoN(ColorName);
    }
    cout << (long long)sum;
}
int CtoN(string ColorN){
    if (ColorN=="black") return 0;
    else if (ColorN=="brown") return 1;
    else if (ColorN=="red") return 2;
    else if (ColorN=="orange") return 3;
    else if (ColorN=="yellow") return 4;
    else if (ColorN=="green") return 5;
    else if (ColorN=="blue") return 6;
    else if (ColorN=="violet") return 7;
    else if (ColorN=="grey") return 8;
    else if (ColorN=="white") return 9;
    else return -1;
}*/

/*�ٸ� ����� Ǭ ���
#include <iostream>
#include <math.h>
using namespace std;

string om[10] = {"black", "brown", "red", "orange", "yellow", "green", "blue", "violet", "grey", "white"};
int value(string x) {
    for(int j=0;j<10;j++) {
        if(om[j] == x) {
            return j;
        }
    }
    return -1;
}
int main() {
    string x;
    long long int sum=0;
    cin>>x;
    sum+=value(x)*10;
    cin>>x;
    sum+=value(x);
    cin>>x;
    int dec=value(x);
    if(dec!=0) sum*=pow(10, dec);
    cout<<sum;
}*/





//���� 1100��

/*2���� �迭 fill �� �õ��ߴٰ� �׸��� ��
#include<iostream>
#include<algorithm>
using namespace std;

#define MAX 8

void Change(char a);

int main()
{
    //2���� �迭�� �̿��� Ǯ���
    char ChessField[8][8]={};
    fill(&ChessField[0][0], &ChessField[MAX-1][MAX], '.');//fill�Լ��� ����� 8x8 �԰��� ü������ '.'���� ��� �ʱ�ȭ
    char ChessStones;
    for (int i=0; i<8; i++){
        for (int j=0; j<8; j++){
            cin >> ChessStones;
            ChessField[i][j]=ChessStones;
            Change(ChessStones);// �Էµ� ���� ���� ü���� ���¸� �ٲ��ִ� �Լ�
        }
    }
}
void Change(char a)
{
    if (a=='.')
}*/

/*���� ver1
#include<iostream>
using namespace std;
#define MAX 8
int main()
{
    char A[MAX][MAX], S;
    int sum = 0;
    for (int i=0; i<MAX; i++){
        for(int j=0; j<MAX; j++){
            cin>>S;
            A[i][j]=S;
            if(i%2==0 && j%2==0 && A[i][j]=='F') sum+=1;
            else if(i%2==1 && j%2==1 && A[i][j]=='F') sum+=1;
        }
    }
    cout << sum;
    return 0;
}*/

//���� ver2
/*#include<iostream>
using namespace std;
#define MAX 8
int main()
{
    char A[MAX][MAX], S;
    int sum = 0;
    for (int i=0; i<MAX; i++){
        for(int j=0; j<MAX; j++){
            cin>>S;
            A[i][j]=S;
            if((i%2==j%2 && A[i][j]=='F')||(i%2==j%2 && A[i][j]=='F')) sum+=1;
        }
    }
    cout << sum;
    return 0;
}


//�ٸ� ����� § �ڵ�
#include<cstdio>
int c=0;
char s[9];
int main()
{
    for(int i=1;i<=8;++i)
    {
        scanf("%s",s);
        for(int j=1;j<=8;++j)
        {
            if(i%2==j%2&&s[j-1]=='F') ++c;
        }
    }
    printf("%d",c);
    return 0;
}*/


//===========================================================






//���� 1159��

// #include<iostream>
// #include<string>
// using namespace std;
// #define MAX 150
// int main()
// {
//     int num;
//     char Nm;
//     bool serial=false;
//     string aths[MAX],names;
//     int arr[26]={0,};
//     cin>>num;
//     for (int i=0; i<num; i++){
//         cin>>names;
//         aths[i]=names;
//         arr[aths[i][0]-97]+=1;
//     }
//     for (int i=0; i<26; i++){
//         if (arr[i]>=5){
//             Nm=(char)(i+97);
//             cout<<Nm;
//             serial=true;
//         }
//     }
//     if (serial==false) cout<<"PREDAJA";
//     return 0;
// }

/*#include <iostream>
#include <map>
using namespace std;

int N;
map<char, int> m;

int main(){

    cin>>N;


    for(int i=0; i<N; i++){
        string str; cin>>str;
        m[str[0]]++;
    }


    bool check=false;
    for(char i='a'; i<='z'; i++){
        if(m[i]>=5) {
            cout<<i;
            check=true;
        }
    }

    if(!check) cout<<"PREDAJA";

}*/



//���� 1173��
#include<iostream>

using namespace std;
int main()
{
    int N,m,M,T,R;
    int X,Ttime=0; 
    //X�� ���� �ɹڼ�, N�� ��ð�(��), m�� �ּҽɹڼ�, M�� �ִ�ɹڼ�, T�� ������ �ɹڼ�, R�� ������ �ƹڼ�
    cin >> N >> m >> M >> T >> R;
    
    X=m;
    //�ʱ�ƹ� X�� m

    if (X+T>M){
        cout << -1;
        return 0;
    }
    for(int i=0; i<N; i++){
        // Ttime++;
        if(X+T<=M) {
            X+=T;
            Ttime++;
        }
        else{
            X-=R;
            if(X-R<m) X=m;
            Ttime++;
        }
    }
    cout << Ttime <<'\n';
    return 0;
}

#include <iostream>
using namespace std;
int N, m, M, T, R;
int cnt, currentPulse, time;
int main(){
    cin >> N >> m >> M >> T >> R;
    currentPulse = m;
    if(currentPulse + T > M){
        cout << -1 << '\n';
        return 0;
    } 
    for(int cnt = 0; cnt < N;){
        time++;
        if(currentPulse + T <= M){
            currentPulse += T;
            cnt++;
        }
        else {
            currentPulse -= R;
            if(currentPulse < m) currentPulse = m;
        }
    }
    cout << time <<'\n';
}