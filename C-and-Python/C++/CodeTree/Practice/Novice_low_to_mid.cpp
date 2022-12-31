/*Novice low - <다중반복문> - 행에 대해 대칭인 별 출력

아래와 같이 중간 행에 대해 대칭인 모양의 별표를 그리는 프로그램은 어떻게 작성할 수 있을까요?
***
**
*
**
***
*/

// #include<cstdio>
// #include<iostream>
// using namespace std;
// int main()
// {
//     for (int i=1; i<=3; i++){
//         for(int j=3; j>0; j-=i){
//             cout<<"* ";
//         }
//         cout << endl;
//     }
//     for (int i=1; i>-1; i--){
//         for(int j=0; j<3-i; j++){
//             cout<<"* ";
//         }
//         cout << endl;
//     }
//     return 0;
// }

// #include<cstdio>
// #include<iostream>
// using namespace std;
// int main()
// {
//     int n;
//     cin >> n;
//     for (int i=1; i<=n; i++){
//         for (int j=0; j<i; j++){
//             cout << "* ";
//         }
//         cout << endl;
//     }
//     for (int i=1; i<=n; i++){
//         for (int j=n-i; j>0; j--){
//             cout << "* ";
//         }
//         cout << endl;
//     }
//     return 0;
// }



/* Novice low - <다중반복문> 
행과 열
행과 열의 수를 a, b로 입력받아 출력하는 프로그램을 작성해보세요.
입력 형식
정수 a, b를 공백을 사이에 두고 주어집니다.
*/
// #include<cstdio>
// #include<iostream>
// using namespace std;
// int main()
// {
//     int A, B;
//     cin >> A >> B;
//     for (int i=1; i<=A; i++){
//         for (int j=1; j<=B; j++){
//             printf("%d ", i*j);
//         }
//         cout << endl;
//     }
//     return 0;
// }


/* 숫자 삼각형
 정수 n의 값이 주어지면 숫자로 이루어진 삼각형을 출력하는 프로그램을 작성해보세요.
*/
// #include<cstdio>
// #include<iostream>
// using namespace std;
// int main()
// {
//     int n;
//     cin >> n;
//     for (int i=0; i<n; i++){
//         for (int j=0; j<i+1; j++){
//             cout << j+1;
//         }
//         cout << endl;
//     }
// }



/*아스키 코드 (ASCII)
c 언어에서 사용할 수 있는 모든 문자들은 전부 하나의 숫자와 대응되며, 이를 아스키 코드라 부릅니다.

그 중에서도 알파벳 대문자 (A, B, C, ...), 소문자 (a, b, c, ....) 끼리는 연속한 숫자들로 매칭이 되어있습니다.

만약 문자 'A'의 아스키 코드 값이 15였다면, 문자 'B'의 아스키 코드 값은 16이 된다는 것입니다.

c에서 특정 문자의 아스키 코드 값은 해당 문자의 정수형 출력을 이용해 알 수 있습니다. 

실제 문자 'A'의 아스키 코드 값은 65이기 때문에 정수형 변환을 통해, 

즉 'A'의 type 을 int 로 바꾸어 출력하면 65가 출력됩니다.


정수 n의 값이 주어지면 n*n 개 정사각형 모양으로 알파벳을 출력하는 프로그램을 작성해보세요.
*/

// #include<cstdio>
// #include<iostream>
// using namespace std;
// int main()
// {
//     int m;
//     cin >> m;
//     int n = 'A';
//     for (int i=0; i<m; i++){
//         for(int j=0; j<m; j++){
//             cout << (char)n;
//             n+=1;
//         }
//     printf("\n");
//     }
//     return 0;
// }

// #include<iostream>
// using namespace std;
// int main()
// {
//     int n;
//     cin >> n;
//     double sco[n], sum=0, avg;
//     for (int i=0; i<n; i++){
//         cin >> sco[i];
//         sum += sco[i];
//     }
//     avg = sum / n;
//     cout << fixed;
//     cout.precision(1);
//     cout << avg << endl;
//     if (avg >= 4.0) cout << "Perfect";
//     else if(avg<3.0) cout << "Poor";
//     else cout << "Good";
//     return 0;
// }


/*피보나치 - 변형*/
// #include<iostream>
// using namespace std;
// int main()
// {
//     int A,B,temp;
//     cin >> A >> B;
//     cout << A << " " << B << " ";
//     for (int i=0; i<8; i++){
//         temp=(A+B)%10;
//         cout << temp << " ";
//         A=B;
//         B=temp;
//     }
//     return 0;
// }


/*Counting 배열*/
// #include<iostream>
// using namespace std;
// int main()
// {
//     int arr[10] = {1,5,2,2,1,6,3,1,3,4};
//     for(int i=1; i<7; i++){
//         int cnt = 0;
//         for(int j=0; j<10; j++){
//             if (arr[j] == i){
//                 cnt ++;
//             }
//         }
//         cout<<i;
//     }
// }


/*특정 위치의 문자
6개의 문자 배열을 만들고 각각 'L', 'E', 'B', 'R', 'O', 'S'로 초기화한 후에, 
문자 한 개가 주어지면 배열의 위치를 출력하는 프로그램을 작성해보세요. 
배열의 첫 번째 위치는 0번이며 배열에 없는 문자가 주어지면 "None"이라는 메시지를 출력합니다.*/

// #include<iostream>
// using namespace std;
// int main()
// {
//     char word[6] = {'L', 'E', 'B', 'R', 'O','S'};
//     int idx = -1;
//     char A;
//     cin >> A;
//     for (int i=0; i<6; i++){
//         if (word[i] == A){
//             idx = i;
//         }
//     }
//     if (idx == -1){
//         cout << "None";
//     }
//     else cout << idx;
//     return 0;
// }


/*특정 원소의 개수
리스트 ['A', 'P', 'P', 'L', 'E'] 안에 문자 'P'가 몇 번 들어있는지는 어떻게 알 수 있을까요?
cnt라는 변수를 사용해 다음과 같이 코드를 작성해 볼 수 있습니다.
*/

// #include<iostream>
// using namespace std;
// int main()
// {
//     char word[5] = {'A', 'P', 'P', 'L', 'E'};
//     int cnt = 0;
//     for (int i=0; i<5; i++){
//         if(word[i]=='P'){
//             cnt += 1;
//         }
//     }
//     cout << cnt;
//     return 0;
// }



/*개수 세기
정수 n이 주어지면 그 횟수만큼 수가 주어집니다. 
그 중 m이 몇 번 등장하는지 구해 출력하는 프로그램을 작성해보세요.
*/
// #include<iostream>
// using namespace std;
// int main()
// {
//     int n,m,cnt=0;
//     cin >> n >> m;
//     int arr[n]={};
//     for (int i=0; i<n; i++){
//         cin>>arr[i];
//         if(arr[i]==m){
//             cnt++;
//         }
//     }
//     cout << cnt;
//     return 0;
// }



/*문자열 - 문자열 역순출력*/
// #include<iostream>
// #include<string>
// using namespace std;
// int main()
// {
//     string strarr[4];
//     for (int i=0; i<4; i++){
//         cin >> strarr[i];
//     }
//      for (int i=3; i>-1; i--){
//        cout << strarr[i] << endl;
//     }
//     return 0;
// }

/*문자열 - 문자열 역순출력2*/
// #include<iostream>
// #include<string>
// using namespace std;
// int main()
// {
//     string strarr[4];
//     for (int i=0; i<4; i++){
//         getline(cin, strarr[i]);
//     }
//      for (int i=3; i>-1; i--){
//        cout << strarr[i] << endl;
//     }
//     return 0;
// }

/*공백 단위로 문자열 입력받기*/
// #include<iostream>
// #include<string>
// using namespace std;
// int main()
// {
//     string str;
//     string str1[10];
//     int len = 0;
//     for (int i=0; i<10; i++){
//         cin >> str;
//         str1[i] = str;
//         len += str1[i].length();
//     }
//     cout << len;
//     return 0;
// }

/*문자열 순회*/
// #include<iostream>
// #include<string>
// using namespace std;
// int main()
// {
//     string str;
//     cin >> str;
//     for (int i=0; i<str.length(); i++){
//         cout << str[i];
//     }
// }


/*대문자화 소문자화*/
// #include <iostream>
// #include <cctype>
// using namespace std;
// int main() {
// 	char x = 'c';
// 	cout << (char)toupper(x);
// 	return 0;
// }



/*오름 내림차순 정렬*/
// #include <iostream>
// #include <Algorithm>
// using namespace std;
// int main()
// {
//     int n;
//     cin >> n;
//     int *arr = new int[n];
//     for (int i=0; i<n; i++){
//         cin >> arr[i];
//     }
// 	sort(arr, arr+n);
//     for (int i=0; i<n; i++){
//         cout << arr[i] << " ";
//     }
// 	cout << endl;
// 	sort(arr, arr+n, greater<int>());
//     for (int i=0; i<n; i++){
//         cout << arr[i] << " ";
//     }
// }


/*객체-클래스*/
// #include<iostream>
// #include<string>
// using namespace std;
// int main()
// {
//     class Agent
//     {
//         public:
//             string scr; 
//             char place; 
//             int time;
//             Agent(string s, char p, int t){
//                 this -> scr = s;
//                 this -> place = p;
//                 this -> time = t;
//             }
//     };
//     string s1;
//     char p1;
//     int t1;
//     cin >> s1 >> p1 >> t1;
//     Agent agent1 = Agent(s1, p1, t1);
//     cout << "secret code : " << agent1.scr<<endl;
//     cout << "meeting point : " << agent1.place<<endl;
//     cout << "time : " << agent1.time<<endl;
//     return 0;
// }


/*함수 - 숫자로 이루어진 사각형
정수 N의 값이 주어지면 일의자리 숫자로 이루어진 N * N 모양 사각형을 출력하는 프로그램을 작성해보세요. 
이때 정수 n을 전달받아 일의 자리 숫자로 이루어진 정사각형을 출력하는 함수를 작성하고, 
주어진 N을 함수로 전달하여 출력합니다.
*/
// #include<iostream>
// using namespace std;
// void PN(int n)
// {
//     int num = 1;
//     for (int i=0; i<n; i++){
//         for (int j=0; j<n; j++){
//             cout << num << " ";
//             num = (num+1)%10;
//             if(num==0) num++;
//         }
//         cout << endl;
//     }
// }
// int main()
// {
//     int n;
//     cin >> n;
//     PN(n);
//     return 0;
// }




/*함수 - 최대공약수 찾기(유클리드 호제)*/
// #include <iostream>
// using namespace std;
// int MaxG(int n, int m)
// {
//     while (true){
//         if(n==1 || m==1) {
//             cout << 1; 
//             break;
//         }
//         else if (n > m) {
//             n=n%m;
//             if (n==0){
//                 cout << m;
//                 break;
//             } 
//         }
//         else {
//             m=m%n;
//             if (m==0){
//                 cout << n;
//                 break;
//             }
//         }
//     }
// }
// int main()
// {
//     int n,m;
//     cin >> n >> m;
//     MaxG(n,m);
//     return 0;
// }



/*정수의 최솟값
세 정수 a, b, c가 주어지면 그 수를 전달받아 최솟값을 구하여 출력하는 프로그램을 작성해보세요. 
이때 주어진 세 정수 a, b, c를 전달받아 최솟값을 구하는 함수를 작성하고, 
주어진 a, b, c를 함수로 전달하여 출력합니다.
*/
// #include<iostream>
// #include<climits>
// using namespace std;
// int find_min(int a, int b, int c){
//     int temp = INT_MAX, arr[3]={a,b,c};
//     for (int i=0; i<3; i++){
//         if (temp > arr[i]) temp = arr[i];
//     }
//     return temp;
// }
// int main()
// {
//     int a,b,c;
//     cin >> a >> b >> c;
//     cout << find_min(a,b,c);
//     return 0;
// }


/*문제를 top down으로 생각하기
1부터 100 사이의 숫자들 중 3의 배수는 아니면서 5의 배수인 숫자의 개수를 세는 프로그램을 작성해보려 합니다. 
이 문제는 어떻게 푸는 것이 가장 깔끔한 방법일까요?
이 문제를 어떻게 풀지를 큰 단위로 생각해보면 다음과 같습니다.*/
// #include<iostream>
// using namespace std;
// bool MagicNum(int a){
//     if (a>=100 || a<10) return false;
//     if (a%2==0 && (((a-(a%10))/10)+(a%10))%5==0) return true;
//     else return false;
// }
// int main()
// {
//     int n;
//     cin >> n;
//     if (MagicNum(n)) cout << "Yes";
//     else cout << "No";
//     return 0;
// }




/*함수를 이용한 369 게임
a에서 b사이에 숫자에 3, 6, 9 중에 하나가 들어가 있거나 
그 숫자 자체가 3의 배수인 숫자의 개수를 세는 프로그램을 작성해보세요. 
단, 함수를 이용하여 문제를 해결해주세요.
*/
// #include<iostream>
// using namespace std;
// bool contain369(int n){
//     while (n!=0){
//         if((n%10!=0)&&(n%10)%3==0) return true;
//         else n/=10;
//     }
//     return false;
// }
// bool IsTrue(int n){
//     return contain369(n) || (n % 3==0);
// }
// int IsMagicNum(int n, int m){
//     int cnt = 0;
//     for (int i=n; i<=m; i++){
//         if (IsTrue(i)) cnt += 1;
//     }
//     return cnt;
// }
// int main()
// {
//     int a,b;
//     cin >> a >> b;
//     cout << IsMagicNum(a,b);
//     return 0;
// }


/*함수를 이용한 소수 판별
a에서 b사이 소수들의 합을 구해주는 프로그램을 작성해보세요. 
단, 함수를 이용하여 문제를 해결해주세요.
*/
// #include<iostream>
// using namespace std;
// bool is_prime(int n){
//     if (n == 1) return false;
//     for (int i=2; i<n; i++){
//         if (n%i==0) return false;
//     }
//     return true;
// }
// int main()
// {
//     int a,b,sum=0;
//     cin >> a >> b;
//     for (int i=a; i<=b; i++){
//         if (is_prime(i)) sum+=i;
//         else continue;
//     }
//     cout << sum;
//     return 0;
// }



/*함수를 이용한 윤년 판별
y가 주어졌을 때. y년이 윤년인지를 판단하는 프로그램을 작성해보세요. 
단, 함수를 이용하여 문제를 해결해주세요.

윤년의 조건은 다음과 같습니다.

4의 배수라면 윤년입니다.
4의 배수이면서 100의 배수라면 윤년이 아닙니다.
4의 배수이면서 100의 배수지만 또한 400의 배수라면 윤년입니다.
나머지 경우에는 윤년이 아닙니다.*/
/*
#include<iostream>
using namespace std;

bool isleap(int n){
    if (n%4==0){
        if (n%400==0) return true;
        else if (n%100==0) return false;
        else return true;
    }
    // if ((n%4==0 && n%100!=0) || (n%400 ==0)) return true;
    // else return false;
    
}

int main()
{
    int n;
    cin >> n;
    if (isleap(n)==true) cout << "true";
    else cout << "false";
    return 0;
}
*/


/*두 정수 값 교환하기
두 개의 정수 n, m이 주어지면 두 개의 숫자에 있는 값을 교환하여 출력하는 프로그램을 작성해보세요. 
단, a, b를 인자로 하는 함수를 작성하여  두 변수에 담겨있는 값을 교환하고 출력은 함수 호출 이후에 진행하도록 합니다.*/

/*#include<iostream>
using namespace std;

// void swap(int *a, int *b){
//     int temp = *a;
//     *a = *b;
//     *b = temp;
// }

void swap(int &a, int &b){
    int temp = a;
    a = b;
    b = temp;
}

int main()
{
    int n,m;
    cin >> n >> m;
    swap(n,m);
    cout << n << " " << m;
    return 0;
}
*/


/*짝수만 2로 나누기
N개의 원소로 이루어진 배열을 인자로 받아 그 중 짝수인 원소만 2로 나눠주는 함수를 작성하고, 
해당 함수를 호출 한 후 각 원소의 값을 출력하는 프로그램을 작성해보세요. 
단, 값을 반환하지 않는 함수를 이용해 문제를 해결해야 합니다.*/
/*
#include<iostream>
using namespace std;

bool Is2divisible(int n){
    return n%2==0;
}

int main()
{
    int n;
    cin >> n;
    int *arr = new int [n];
    for (int i=0; i<n; i++){
        cin >> arr[i];
        if (Is2divisible(arr[i])) arr[i] /= 2;
    }
    for (int i=0; i<n; i++){
        cout << arr[i] << " ";
    }
    delete [] arr;
    return 0;
}
*/



/*palindrome 여부 판단하기
palindrome이란 문자열을 뒤집었을 때도 동일한 문자열인 경우를 뜻합니다.
소문자 알파벳으로만 이루어진 문자열 A가 주어졌을 때, 
문자열 A가 palindrome인지를 판단하는 프로그램을 작성해보세요. 
단, 함수를 이용하여 문제를 해결해주세요.*/
/*#include <iostream>

using namespace std;

bool IsPalindrome(string &s){
    int len = s.length();
    int s_len = len/2;
    char arr[s_len];
    for(int i=0; i<s_len; i++){
        arr[i] = s[i];
    }
    for(int i=0; i<s_len; i++){
        if (arr[i] != s[len-1-i]) return false;
    }
    return true;   
}

int main()
{
    string str;
    cin >> str;
    if (IsPalindrome(str)) cout << "Yes";
    else cout << "No";
    return 0;
}
*/



/*함수를 이용한 부분문자열의 위치 구하기
주어진 입력 문자열에 대하여 목적 문자열이 부분 문자열로 존재하는 경우, 
부분 문자열의 시작 인덱스를 출력하는 코드를 작성해보세요. 
단, 함수를 이용하여 문제를 해결해주세요. 인덱스는 0부터 시작한다고 가정합니다.
*/

/*#include<iostream>
#include<string>
using namespace std;

string str = "codetree";
int idx=0;

bool IsPartial(string s){
    string new_s;
    cin >> new_s;
    int a=s.length(), b = new_s.length();
    for (int i=0; i<a; i++){
        if (s.substr(i,b) == new_s){
            idx = i;
            return true;
        }
    }
    return false;
}

int main()
{
    string str;
    cin >> str;
    if (IsPartial(str)) cout << idx;
    else cout << -1;
}
*/


/*객체 - Next Level
"아이디", "레벨"을 같이 저장할 수 있는 형태(c언어의 경우 구조체를, 다른 언어의 경우 class)를 정의하고, 
2개의 객체를 선언한 후, 하나의 객체는 아이디에 "codetree", 레벨에 "10"으로 각각 초기화하고 
다른 객체는 새롭게 입력받은 값을 넣어 입출력 예제와 같이 출력하는 프로그램을 작성해보세요.*/
/*#include <iostream>
#include <cstdio>
using namespace std;

int main()
{
    class ID{
        public:
            string id; 
            int lv;
            ID(string a = "codetree", int b = 10){
                this -> id = a;
                this -> lv = b;
            }
    };

    ID id1 = ID();
    string a1;
    int b1;
    cin >> a1 >> b1;
    ID id2 = ID(a1, b1);

    cout << "user" <<" "<< id1.id << " " << "lv" <<" "<<id1.lv << endl;
    cout << "user" <<" "<< id2.id << " " << "lv" <<" "<<id2.lv << endl;
  
    return 0;
}
*/

/*
#include<iostream>
#include<tuple>
using namespace std;
    
class Agent{
    public:
        char cn;
        int score;
        Agent(char c, int s){
            this -> cn = c;
            this -> score = s;
        }
Agent() {}
};
    
int main()
{
    
    Agent agents[5];
    for (int i=0; i<5; i++){
        char a;
        int b;
        cin >> a >> b;
        agents[i].cn = a; agents[i].score = b;
    }
    int idx, min = agents[0].score;
    for (int i=0; i<5; i++){
        if(min >= agents[i].score){
            min = agents[i].score;
            idx = i;
        } 
    }
    cout <<agents[idx].cn<<" "<< min;
    return 0;
}*/


/*코드네임
5명의 코드네임과 점수를 입력받아 점수가 제일 낮은 요원의 정보를 출력하는 프로그램을 작성해보세요. 
단, c언어의 경우 구조체를, 다른 언어의 경우 class를 이용하여 
각 사람의 정보를 담은 객체를 5개 만들어 문제를 해결해주세요.*/

/*클래스 사용 버전
#include<iostream>
#include<tuple>
#include<string>
using namespace std;
    
class Agent{
    public:
        char cn;
        int score;
        Agent(char c, int s){
            this -> cn = c;
            this -> score = s;
        }
Agent() {}
};

int main()
{
    Agent agents[5];
    for (int i=0; i<5; i++){
        char a;
        int b;
        cin >> a >> b;
        agents[i].cn = a; agents[i].score = b;
    }
    int idx;
    int min = agents[0].score;
    for (int i=0; i<5; i++){
        if(min > agents[i].score){
            min = agents[i].score;
            idx = i;
        } 
    }
    cout <<agents[idx].cn<<" "<< min;
    return 0;
}
*/
/*튜플 사용 버전
#include<iostream>
#include<tuple>
#include<string>
using namespace std;
    
int main()
{
    tuple<char, int> Agent[5];
    for (int i=0; i<5; i++){
        char a; int b;
        cin >> a >> b;
        Agent[i] = make_tuple(a,b);
    }

    int idx, min=get<1>(Agent[0]);
    for (int i=0; i<5; i++){
        int temp = get<1>(Agent[i]);
        if(min >= temp){
            min = temp;
            idx = i;
        }
    }
    char c= get<0>(Agent[idx]);
    cout << c <<" "<< min;
    return 0;
}
*/




/*객체정렬 - 키를 기준으로 정렬*/
/*#include<iostream>
#include<tuple>
#include<algorithm>
#include<functional>

using namespace std;

#define MAX_N 100

class People{
    public:
        string Name;
        int Height, Weight;
        People(string n, int h, int w){
            this -> Name = n;
            this -> Height = h;
            this -> Weight = w;
        }
    People(){}
};

bool cmp(const People &a, const People &b){
    return a.Height < b.Height;
}

int main()
{
    int n;
    cin >> n;
    People parr[MAX_N];


    for (int i=0; i<n; i++){
        string name;
        int height, weight;
        cin >> name >> height >> weight;
        parr[i].Name = name; parr[i].Height = height; parr[i].Weight = weight;
    }

    sort(parr, parr+n, cmp);
    for (int i=0; i<n; i++){
        cout << parr[i].Name <<" "<<parr[i].Height<<" "<<parr[i].Weight<<endl;
    }
    return 0;
}
*/


/*국영수 순이지
n이 주어지고, n명인 학생수의 이름과 국어, 영어, 수학 세 과목의 점수가 주어지면 
국어, 영어, 수학 순서대로 우선순위로 하여 과목 점수가 높은 학생부터 출력하는 프로그램을 작성해보세요.*/
/*#include<iostream>
#include<tuple>
#include<string>
#include<algorithm>
using namespace std;
class Student{
    public:
        string name1;
        int kor1, eng1, math1;
        Student(string n, int k, int e, int m){
            this -> name1 = n;
            this -> kor1 = k;
            this -> eng1 = e;
            this -> math1 = m;
        }
    Student(){}
};

bool cmp(const Student &a, const Student &b){
    if(a.kor1==b.kor1){
        if(a.eng1==b.eng1){
            return a.math1>b.math1;
        }
        return a.eng1>b.eng1;
    }
    return a.kor1>b.kor1;
}
int main()
{
    int n;
    cin >> n;
    Student students[n];
    for (int i=0; i<n; i++){
        string name2;
        int kor2, eng2, math2;
        cin >> name2 >> kor2 >> eng2 >> math2;
        students[i].name1 = name2; students[i].kor1 = kor2; students[i].eng1 = eng2; students[i].math1 = math2;
    }
    sort(students, students+n, cmp);
    for (int i=0; i<n; i++){
        cout<<students[i].name1<<" "<<students[i].kor1<<" "<<students[i].eng1<<" "<<students[i].math1<<endl;
    }
    return 0;
}
*/


/*개인정보
5명의 이름, 키, 몸무게가 주어지면 이름순으로 정렬하여 출력하고, 
키가 큰 순으로 정렬하여 출력하는 프로그램을 작성해보세요. 
단, 동일한 이름과 키가 주어지지 않는다고 가정해도 좋습니다*/
/*#include<iostream>
#include<algorithm>
#include<string>

using namespace std;

class Student{
    public:
        string name1;
        int height1;
        double weight1;
        Student(string n, int h, double w){
            this -> name1 = n;
            this -> height1 = h;
            this -> weight1 = w;
        }
    Student(){}
};

bool cmp1(const Student &a, const Student &b){
    return a.name1 < b.name1;
}

bool cmp2(const Student &a, const Student &b){
    return a.height1 > b.height1;
}


#define s_num 5

int main()
{
    Student students[s_num];
    for (int i=0; i<s_num; i++){
        string name;
        int height;
        double weight;
        cin >> name >> height >> weight;
        students[i].name1 = name; students[i].height1 = height; students[i].weight1 = weight;
    }
    cout << "name" << endl;
    sort(students, students+s_num, cmp1);
    for (int i=0; i<s_num; i++){
        cout << fixed;
        cout.precision(1);
        cout << students[i].name1 << " " << students[i].height1 << " " << students[i].weight1<<endl;
    }
    cout << endl << "height"<<endl;
    sort(students, students+s_num, cmp2);
    for (int i=0; i<s_num; i++){
        cout << fixed;
        cout.precision(1);
        cout << students[i].name1 << " " << students[i].height1 << " " << students[i].weight1<<endl;
    }
    return 0;
}
*/




/*키, 몸무게를 기준으로 정렬
n명의 이름, 키, 몸무게가 주어지면 키를 기준으로 오름차순으로 정렬하여 출력하는 프로그램을 작성해보세요. 
단, 키가 동일한 경우에는 몸무게가 더 큰 사람이 먼저 나오도록 정렬해야 합니다. 
키, 몸무게가 둘 다 동일한 경우는 없다고 가정해도 좋습니다.*/


// #include<iostream>
// #include<algorithm>
// #include<string>

// using namespace std;

// class Student{
//     public:
//         string name1;
//         int height1;
//         int weight1;
//         Student(string n, int h, int w){
//             this -> name1 = n;
//             this -> height1 = h;
//             this -> weight1 = w;
//         }
//     Student(){}
// };


// bool cmp(const Student &a, const Student &b){
//     if (a.height1==b.height1)
//         return a.weight1 > b.weight1;
//     return a.height1 < b.height1;
// }

// int main()
// {
//     int n;
//     cin >> n;
//     const int a = n;
//     Student students[a];
//     for (int i=0; i<a; i++){
//         string name;
//         int height;
//         int weight;
//         cin >> name >> height >> weight;
//         students[i].name1 = name; students[i].height1 = height; students[i].weight1 = weight;
//     }
//     sort(students, students+a, cmp);
//     for (int i=0; i<a; i++){
//         cout << students[i].name1 << " " << students[i].height1 << " " << students[i].weight1<<endl;
//     }

//     return 0;
// }


/* 흐른 시간 계산 */
/*#include<iostream>
#include<cstdlib>
using namespace std;

int main()
{
    int a=2, b=5, c=4, d=1;
    // cin >>a>>b>>c>>d;
    cout << abs((60*a+b)-(60*c+d));
    return 0;
}*/


/*Date to Date
2011년 m1월 d1일로부터 2011년 m2월 d2일까지는 총 몇 일이 있는지를 계산하는 프로그램을 작성해보세요. 2011년은 윤년이 아닌 해이기 때문에 2월은 28일까지 있습니다.*/
/*#include<iostream>
using namespace std;


int main()
{
    int month[12] = {31,28,31,30,31,30,31,31,30,31,30,31};
    int m1,d1,m2,d2,cnt=0;
    cin >>m1>>d1>>m2>>d2;
    for (int i=m1-1; i<m2-1; i++){
        cnt += month[i];
    }
    cnt = cnt-d1+d2+1;
    cout << cnt;
    return 0;
}*/
/*함수 사용 버전
#include<iostream>
using namespace std;

int Days(int m1, int d1, int m2, int d2){
    int month[12] = {31,28,31,30,31,30,31,31,30,31,30,31};
    int cnt=0;
    for (int i=m1-1; i<m2-1; i++){
    cnt += month[i];
    }
    cnt = cnt-d1+d2+1;
    return cnt;
}

int main()
{
    // int month[12] = {31,28,31,30,31,30,31,31,30,31,30,31};
    int m1,d1,m2,d2;
    cin >>m1>>d1>>m2>>d2;
    // for (int i=m1-1; i<m2-1; i++){
    //     cnt += month[i];
    // }
    // cnt = cnt-d1+d2+1;
    // cout << cnt;
    cout << Days(m1,d1,m2,d2);
    return 0;
}*/



/*2진수로 변환하기
십진수 n이 주어지면 0과 1로만 이루어진 2진수로 그 수를 변환하여 출력하는 프로그램을 작성해보세요.*/
/*#include<iostream>
#include<string>
#include<algorithm>
using namespace std;

void ToBinary(int num){
    string str = to_string(num);
    int arr[20], i=0;
    if (num == 0) cout << 0;
    while (num!=0){
        arr[i] = num%2;
        num /= 2;
        i++;
    }
    reverse(arr,arr+i);
    for(int j=0; j<i; j++){
        cout<<arr[j];
    }
}

int main()
{
    int n;
    cin >> n;
    ToBinary(n);
}*/


/*10진수로 변환하기
0과 1로 이루어진 2진수로 어떤 수가 주어지면 그 수를 십진수로 변환하여 출력하는 프로그램을 작성해보세요.*/
/*#include<iostream>
#include<algorithm>
#include<string>
#include<cmath>

using namespace std;

int power(int n, int m){    //직접 구현한 제곱함수 (cmath에 pow라는 똑같은 것이 있다.)
    int result = 1;
    if (m == 0) return 1;
    for (int i=0; i<m; i++){
        result *= n;
    }
    return result;
}

int To_Binary(int num){
    int arr[20], sum=0, i=0;
    while (num !=0){
        int front = num%2;
        sum += front*power(2,i);
        i++;
        num /= 10;
    }
    return sum;
}

int main()
{
    int binary;
    cin >> binary;
    cout <<To_Binary(binary);

    return 0;
}
*/



/*블럭쌓는 명령2
1번 칸부터 N번째 칸까지 총 N개의 칸이 있습니다. 
이 중 Ai에서 Bi까지 각각 블럭을 1씩 쌓으라는 명령이 K번 주어집니다. 
명령을 다 수행한 이후 1번 칸부터 N번 칸까지 쌓인 블럭의 수 중 최댓값을 출력하는 프로그램을 작성해보세요.*/

// #include<iostream>
// #include<algorithm>
// using namespace std;
// int main()
// {
//     int N, K;
//     cin >> N >> K;
//     int arr[N+1]={};
//     for (int i=0; i<K; i++){
//         int a,b;
//         cin >> a >> b;
//         for (int j=a; j<b+1; j++){
//             arr[j] += 1;
//         }
//     }
//     int mnum = arr[0];
//     for (int i=1; i<N+1; i++){
//         if (mnum < arr[i]){
//             mnum = arr[i];
//         }
//     }
//     cout << mnum;
// }




/*사각형의 총 넓이 2
2차 평면 위에 N개의 직사각형이 주어집니다. 이 직사각형들이 만들어내는 총 넓이를 구하는 프로그램을 작성해보세요.*/
// #include <iostream>
// using namespace std;
// #define OFFSET 100
// #define MAX_R 200
// int main()
// {
//     int arr_2d[MAX_R+1][MAX_R+1]={};
//     int n;
//     cin >> n;
//     for (int i=0; i<n; i++){
//         int x1,y1,x2,y2;
//         cin >> x1 >> y1 >> x2 >> y2;
//         x1 += OFFSET; y1 += OFFSET; x2 += OFFSET; y2 += OFFSET;
//         for (int x=x1; x<x2; x++){
//             for (int y=y1; y<y2; y++){
//                 arr_2d[x][y] = 1;
//             }
//         }
//     }
//     int cnt = 0;
//     for (int x=0; x<=MAX_R; x++){
//         for (int y=0; y<=MAX_R; y++){
//             if (arr_2d[x][y] == 1) cnt++;
//         }
//     }
//     cout << cnt;
//     return 0;
// }

/*겹치지 않는 사각형의 넓이
좌표평면위에 직사각형 A, B를 먼저 붙이고 그 위에 직사각형 M을 붙였습니다. 
아직 남아있는 (M으로 덮이지 못한) 직사각형 A, B의 넓이의 합을 구하는 프로그램을 작성해보세요. 
단, 직사각형 A, B는 겹치지 않게 주어진다고 가정해도 좋습니다.*/

// #include <iostream>

// using namespace std;

// #define OFFSET 1000
// #define MAX_R 2000

// int main()
// {
//     int n=3, area=0;
//     int arr_2d[MAX_R+1][MAX_R+1]={};
//     for (int i=1; i<=n; i++){
//         int x1,y1,x2,y2;
//         cin >> x1 >> y1 >> x2 >> y2;
//         x1 += OFFSET; y1 += OFFSET; x2 += OFFSET; y2 += OFFSET;
//         for (int x=x1; x<x2; x++){
//             for (int y=y1; y<y2; y++){
//                 arr_2d[x][y] = i;
//             }
//         }
//     }

//     for (int x=0; x<=MAX_R; x++){
//         for (int y=0; y<=MAX_R; y++){
//             if (arr_2d[x][y] == 1 || arr_2d[x][y] == 2) area++;
//         }
//     }
//     cout << area;
//     return 0;
// }




/*방향에 맞춰 이동
(0, 0)에서 시작하여 총 N번 움직여보려고 합니다. 
N번에 걸쳐 움직이려는 방향과 움직일 거리가 주어졌을 때, 최종 위치를 출력하는 프로그램을 작성해보세요.
단, dx, dy 테크닉을 활용하여 문제를 해결해주세요.*/

/*#include <iostream>

using namespace std;


int main()
{
    int dx[4] = {1,-1,0,0}, dy[4] = {0,0,-1,1};
    int n, x=0, y=0;
    cin >> n;
    for (int i=0; i<n; i++){
        char drt; int dist, drt_num;
        cin >> drt >> dist;

        if (drt == 'E') drt_num = 0;
        else if (drt == 'W') drt_num = 1;
        else if (drt == 'S') drt_num = 2;
        else if (drt == 'N') drt_num = 3;

        x += (dx[drt_num]*dist); y += (dy[drt_num]*dist);
    }
    cout << x << " " << y;
    return 0;
}
*/






/*되돌아오기
(0, 0)에서 시작하여 총 N번 움직여보려고 합니다. 
N번에 걸쳐 움직이려는 방향과 움직일 거리가 주어지고, 1초에 한 칸씩 움직인다고 했을 때, 
몇 초 뒤에 처음으로 다시 (0, 0)에 돌아오게 되는지를 판단하는 프로그램을 작성해보세요.
*/

// #include <iostream>
// using namespace std;
// #define dir_size 4
// int main()
// {
//     int dx[dir_size]={1,-1,0,0}, dy[dir_size]={0,0,-1,1};
//     int N, x=0, y=0, cnt=0, temp=0;;
//     cin >> N;
//     int a = N;
//     while (true){
//         char drt; int dist, dir_num;
//         cin >> drt >> dist;
//         temp++;
//         if (drt == 'E') dir_num = 0;
//         else if (drt == 'W') dir_num = 1;
//         else if (drt == 'S') dir_num = 2;
//         else if (drt == 'N') dir_num = 3;
//         for (int i=0; i<dist; i++){
//             cnt++;
//             x += dx[dir_num]; y += dy[dir_num];
//             if (x==0 && y==0) {
//                 cout << cnt << endl;
//                 break;              //이 부분에서 중첩 반복문을 한 번에 탈출하고 싶습니다.
//             }
//         }
//         if (x==0 && y==0) {
//             break;
//         }
//         if (temp == a){
//             cout << -1;
//             break;
//         }
//     }
//     return 0;
// }


/*#include<iostream>
using namespace std;

void func1(int *n, int *m){
    if(*n>*m){
        *n += 25; *m *= 2;
    }
    else
    {
        *m += 25; *n *= 2;
    }
    return;
}

int main()
{
    int a,b;
    cin >> a >> b;
    func1(&a,&b);
    cout << a << " " << b;
    return 0;
}
*/

/*
#include<iostream>

using namespace std;

void absolute(int &num){
    if (num < 0) {
        num = 0-num;
    }
    return;
}

int main()
{
    int n;
    cin >> n;
    int *arr = new int [n];
    for (int i=0; i<n; i++){
        int a;
        cin >> a;
        absolute(a);
        arr[i] = a;
    }

    for (int i=0; i<n; i++){
        cout << arr[i] << " ";
    }
    delete[] arr;
    return 0;
}*/



// #include<iostream>

// using namespace std;

// int arr1[25];

//  void func1(int a){
//     int idx = 0;
//     while(true){
//         arr1[idx] = a;
//         if (a==1){
//             arr1[idx]==a;
//             break;
//         }
//         else if(a %2==0) a /= 2;
//         else a-=1; 
//         idx++;
//     }
//     return;
// }
 

// int main()
// {
//     int n,m,i=0,sum=0;
//     cin >> n >> m;
//     int *arr2 = new int [n];
//     func1(m);

//     for(int i=0; i<n; i++){
//         cin >> arr2[i];
//     }

//     while(arr1[i]!=0){
//         sum += arr2[arr1[i]-1];
//         i++;
//     }
//     cout<<sum;
//     delete[] arr2;
//     return 0;
// }


/*#include<iostream>
#include<string>
using namespace std;

int main()
{
    int x=0, y=0;
    string dir;
    cin >> dir;
    int curr_dir = 3;
    int dx[4] = {1,0,-1,0}, dy[4] = {0,-1,0,1};
    for(int i=0; i<dir.length(); i++){
        char c_dir = dir[i];
        if (c_dir == 'L')
            curr_dir = (curr_dir+3)%4;
        else if (c_dir == 'R')
            curr_dir = (curr_dir+1)%4;
        else{
            x += dx[curr_dir];
            y += dy[curr_dir];
        }
    }
    cout << x << " " << y;
    return 0;
}*/



// #include<iostream>
// #include<string>

// using namespace std;

// int main()
// {  
//     int n, arr[101][101];
//     cin >> n;
//     for (int i=0; i<n; i++){
//         for (int j=0; j<n; j++){
//             cin >> arr[i][j];
//         }
//     }   
//     int cell = 0;
//     for(int i=0; i<n; i++)
//         for(int j=0; j<n; j++)
//             if(Adajacent(i,j) >= 3)
//                 cell++;
//     cout << cell;
//     return 0;
// }




// #include<iostream>
// #include<string>

// using namespace std;

// int main()
// {
//     bool flag = false;
//     int dx[4] = {1,0,-1,0}, dy[4] = {0,-1,0,1}, x=0,y=0, dir=3;
//     int nx,ny;
//     string str;
//     cin >> str;
//     int *arr = new int[str.length()];
//     for (int i=0; i<str.length(); i++){
//         arr[i] = (char) str[i];
//     }
//     for (int i=0; i<str.length(); i++){
//         if(str[i] == 'L') dir = (dir +3)%4;
//         else if(str[i] == 'R') dir = (dir+1)%4;
//         else {
//             x+= dx[dir];
//             y+= dy[dir];
//         }
//         if (x ==0 && y==0){
//             cout << i+1;
//             flag = true;
//             break;
//         }
//     }
//     if (flag == false) cout << -1;
//     return 0;
// }


/*코드캠프 - 초급반 기말고사*/
//1.청소한 구역의 길이
/*#include<iostream>
#include<algorithm>
using namespace std;

#define OFFSET 100
#define MAX_R 200

int main()
{
    int a, b, c, d;
    cin >> a >> b >> c >> d;
    a+=OFFSET;
    b+=OFFSET;
    c+=OFFSET;
    d+=OFFSET;
    int arr[MAX_R+1]={};
    for (int i=a; i<b; i++){
        arr[i] = 1;
    }
    for (int j=c; j<d; j++){
        arr[j] = 1;
    }
    
    int mnum=0;
    for (int k=1; k<MAX_R+1; k++){
        if (arr[k]==1) mnum++;
    }
    cout << mnum;
    return 0;
}*/



//2.바이러스 검사에 필요한 최소 검사요원 수
#include<iostream>
#include<algorithm>

using namespace std;

int leader,member;
int check(int a){
    int remain;
    a -= leader;
    if (a<1) return 0;
    if(a%member!=0) remain = (a/member)+1;
    else remain = a/member;
    return remain;
}

int main()
{
    int n;
    long long tester=0;
    cin >> n;
    int *cus_arr = new int[n];
    for (int i=0; i<n; i++){
        cin >> cus_arr[i];
    }
    cin >> leader >> member;
    for (int i=0; i<n; i++){
        if (cus_arr[i]==0) continue;
        tester += (1+ check(cus_arr[i])); 
    }
    cout << tester;
    delete[] cus_arr;
    return 0;
}



// #include<iostream>
// #include<string>

// using namespace std;

// int main()
// {
//     string A,B;
//     int cnt=0;
//     cin >> A >> B;
//     for(int i=0; i<A.length()-1; i++){
//         if(A.substr(i,B.length())==B){
//             cnt+=1;
//         }
//     }
//     cout << cnt;
//     return 0;
// }






// #include <iostream>
// #include <algorithm>

// #define N 2
// #define MAX_R 2000
// #define OFFSET 1000

// using namespace std;

// int x1[N], y1[N];
// int x2[N], y2[N];

// int checked[MAX_R + 1][MAX_R + 1];

// int main() {
//     // 입력
//     for(int i = 0; i < N; i++) {
//         cin >> x1[i] >> y1[i] >> x2[i] >> y2[i];
        
//         // OFFSET을 더해줍니다.
//         x1[i] += OFFSET;
//         y1[i] += OFFSET;
//         x2[i] += OFFSET;
//         y2[i] += OFFSET;
//     }
    
//     // 직사각형에 주어진 순으로 1, 2 번호를 붙여줍니다.
//     // 격자 단위로 진행하는 문제이므로
//     // x2, y2에 등호가 들어가지 않음에 유의합니다.
//     for(int i = 0; i < N; i++)
//         for(int x = x1[i]; x < x2[i]; x++)
//             for(int y = y1[i]; y < y2[i]; y++)
//                 checked[x][y] = i + 1;
    
//     // 1, 2 순으로 붙였는데도
//     // 아직 숫자 1로 남아있는 곳들 중 최대 최소 x, y 값을 전부 계산합니다.
//     int min_x = MAX_R, max_x = 0, min_y = MAX_R, max_y = 0;
//     bool first_rect_exist = false;
//     for(int x = 0; x <= MAX_R; x++)
//         for(int y = 0; y <= MAX_R; y++)
//             if(checked[x][y] == 1) {
//                 first_rect_exist = true;
//                 min_x = min(min_x, x);
//                 max_x = max(max_x, x);
//                 min_y = min(min_y, y);
//                 max_y = max(max_y, y);
//             }
    
//     // 넓이를 계산합니다.
//     int area;
//     // Case 1. 첫 번째 직사각형이 전혀 남아있지 않다면 넓이는 0입니다.
//     if(!first_rect_exist)
//         area = 0;
//     // Case 2. 첫 번째 직사각형이 남아있다면, 넓이를 계산합니다.
//     else
//         area = (max_x - min_x + 1) * (max_y - min_y + 1);

//     cout << area;
//     return 0;
// }









