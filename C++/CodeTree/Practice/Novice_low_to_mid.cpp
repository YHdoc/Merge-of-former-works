/*Novice low - <���߹ݺ���> - �࿡ ���� ��Ī�� �� ���

�Ʒ��� ���� �߰� �࿡ ���� ��Ī�� ����� ��ǥ�� �׸��� ���α׷��� ��� �ۼ��� �� �������?
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



/* Novice low - <���߹ݺ���> 
��� ��
��� ���� ���� a, b�� �Է¹޾� ����ϴ� ���α׷��� �ۼ��غ�����.
�Է� ����
���� a, b�� ������ ���̿� �ΰ� �־����ϴ�.
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


/* ���� �ﰢ��
 ���� n�� ���� �־����� ���ڷ� �̷���� �ﰢ���� ����ϴ� ���α׷��� �ۼ��غ�����.
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



/*�ƽ�Ű �ڵ� (ASCII)
c ���� ����� �� �ִ� ��� ���ڵ��� ���� �ϳ��� ���ڿ� �����Ǹ�, �̸� �ƽ�Ű �ڵ�� �θ��ϴ�.

�� �߿����� ���ĺ� �빮�� (A, B, C, ...), �ҹ��� (a, b, c, ....) ������ ������ ���ڵ�� ��Ī�� �Ǿ��ֽ��ϴ�.

���� ���� 'A'�� �ƽ�Ű �ڵ� ���� 15���ٸ�, ���� 'B'�� �ƽ�Ű �ڵ� ���� 16�� �ȴٴ� ���Դϴ�.

c���� Ư�� ������ �ƽ�Ű �ڵ� ���� �ش� ������ ������ ����� �̿��� �� �� �ֽ��ϴ�. 

���� ���� 'A'�� �ƽ�Ű �ڵ� ���� 65�̱� ������ ������ ��ȯ�� ����, 

�� 'A'�� type �� int �� �ٲپ� ����ϸ� 65�� ��µ˴ϴ�.


���� n�� ���� �־����� n*n �� ���簢�� ������� ���ĺ��� ����ϴ� ���α׷��� �ۼ��غ�����.
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


/*�Ǻ���ġ - ����*/
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


/*Counting �迭*/
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


/*Ư�� ��ġ�� ����
6���� ���� �迭�� ����� ���� 'L', 'E', 'B', 'R', 'O', 'S'�� �ʱ�ȭ�� �Ŀ�, 
���� �� ���� �־����� �迭�� ��ġ�� ����ϴ� ���α׷��� �ۼ��غ�����. 
�迭�� ù ��° ��ġ�� 0���̸� �迭�� ���� ���ڰ� �־����� "None"�̶�� �޽����� ����մϴ�.*/

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


/*Ư�� ������ ����
����Ʈ ['A', 'P', 'P', 'L', 'E'] �ȿ� ���� 'P'�� �� �� ����ִ����� ��� �� �� �������?
cnt��� ������ ����� ������ ���� �ڵ带 �ۼ��� �� �� �ֽ��ϴ�.
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



/*���� ����
���� n�� �־����� �� Ƚ����ŭ ���� �־����ϴ�. 
�� �� m�� �� �� �����ϴ��� ���� ����ϴ� ���α׷��� �ۼ��غ�����.
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



/*���ڿ� - ���ڿ� �������*/
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

/*���ڿ� - ���ڿ� �������2*/
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

/*���� ������ ���ڿ� �Է¹ޱ�*/
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

/*���ڿ� ��ȸ*/
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


/*�빮��ȭ �ҹ���ȭ*/
// #include <iostream>
// #include <cctype>
// using namespace std;
// int main() {
// 	char x = 'c';
// 	cout << (char)toupper(x);
// 	return 0;
// }



/*���� �������� ����*/
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


/*��ü-Ŭ����*/
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


/*�Լ� - ���ڷ� �̷���� �簢��
���� N�� ���� �־����� �����ڸ� ���ڷ� �̷���� N * N ��� �簢���� ����ϴ� ���α׷��� �ۼ��غ�����. 
�̶� ���� n�� ���޹޾� ���� �ڸ� ���ڷ� �̷���� ���簢���� ����ϴ� �Լ��� �ۼ��ϰ�, 
�־��� N�� �Լ��� �����Ͽ� ����մϴ�.
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




/*�Լ� - �ִ����� ã��(��Ŭ���� ȣ��)*/
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



/*������ �ּڰ�
�� ���� a, b, c�� �־����� �� ���� ���޹޾� �ּڰ��� ���Ͽ� ����ϴ� ���α׷��� �ۼ��غ�����. 
�̶� �־��� �� ���� a, b, c�� ���޹޾� �ּڰ��� ���ϴ� �Լ��� �ۼ��ϰ�, 
�־��� a, b, c�� �Լ��� �����Ͽ� ����մϴ�.
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


/*������ top down���� �����ϱ�
1���� 100 ������ ���ڵ� �� 3�� ����� �ƴϸ鼭 5�� ����� ������ ������ ���� ���α׷��� �ۼ��غ��� �մϴ�. 
�� ������ ��� Ǫ�� ���� ���� ����� ����ϱ��?
�� ������ ��� Ǯ���� ū ������ �����غ��� ������ �����ϴ�.*/
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




/*�Լ��� �̿��� 369 ����
a���� b���̿� ���ڿ� 3, 6, 9 �߿� �ϳ��� �� �ְų� 
�� ���� ��ü�� 3�� ����� ������ ������ ���� ���α׷��� �ۼ��غ�����. 
��, �Լ��� �̿��Ͽ� ������ �ذ����ּ���.
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


/*�Լ��� �̿��� �Ҽ� �Ǻ�
a���� b���� �Ҽ����� ���� �����ִ� ���α׷��� �ۼ��غ�����. 
��, �Լ��� �̿��Ͽ� ������ �ذ����ּ���.
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



/*�Լ��� �̿��� ���� �Ǻ�
y�� �־����� ��. y���� ���������� �Ǵ��ϴ� ���α׷��� �ۼ��غ�����. 
��, �Լ��� �̿��Ͽ� ������ �ذ����ּ���.

������ ������ ������ �����ϴ�.

4�� ������ �����Դϴ�.
4�� ����̸鼭 100�� ������ ������ �ƴմϴ�.
4�� ����̸鼭 100�� ������� ���� 400�� ������ �����Դϴ�.
������ ��쿡�� ������ �ƴմϴ�.*/
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


/*�� ���� �� ��ȯ�ϱ�
�� ���� ���� n, m�� �־����� �� ���� ���ڿ� �ִ� ���� ��ȯ�Ͽ� ����ϴ� ���α׷��� �ۼ��غ�����. 
��, a, b�� ���ڷ� �ϴ� �Լ��� �ۼ��Ͽ�  �� ������ ����ִ� ���� ��ȯ�ϰ� ����� �Լ� ȣ�� ���Ŀ� �����ϵ��� �մϴ�.*/

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


/*¦���� 2�� ������
N���� ���ҷ� �̷���� �迭�� ���ڷ� �޾� �� �� ¦���� ���Ҹ� 2�� �����ִ� �Լ��� �ۼ��ϰ�, 
�ش� �Լ��� ȣ�� �� �� �� ������ ���� ����ϴ� ���α׷��� �ۼ��غ�����. 
��, ���� ��ȯ���� �ʴ� �Լ��� �̿��� ������ �ذ��ؾ� �մϴ�.*/
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



/*palindrome ���� �Ǵ��ϱ�
palindrome�̶� ���ڿ��� �������� ���� ������ ���ڿ��� ��츦 ���մϴ�.
�ҹ��� ���ĺ����θ� �̷���� ���ڿ� A�� �־����� ��, 
���ڿ� A�� palindrome������ �Ǵ��ϴ� ���α׷��� �ۼ��غ�����. 
��, �Լ��� �̿��Ͽ� ������ �ذ����ּ���.*/
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



/*�Լ��� �̿��� �κй��ڿ��� ��ġ ���ϱ�
�־��� �Է� ���ڿ��� ���Ͽ� ���� ���ڿ��� �κ� ���ڿ��� �����ϴ� ���, 
�κ� ���ڿ��� ���� �ε����� ����ϴ� �ڵ带 �ۼ��غ�����. 
��, �Լ��� �̿��Ͽ� ������ �ذ����ּ���. �ε����� 0���� �����Ѵٰ� �����մϴ�.
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


/*��ü - Next Level
"���̵�", "����"�� ���� ������ �� �ִ� ����(c����� ��� ����ü��, �ٸ� ����� ��� class)�� �����ϰ�, 
2���� ��ü�� ������ ��, �ϳ��� ��ü�� ���̵� "codetree", ������ "10"���� ���� �ʱ�ȭ�ϰ� 
�ٸ� ��ü�� ���Ӱ� �Է¹��� ���� �־� ����� ������ ���� ����ϴ� ���α׷��� �ۼ��غ�����.*/
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


/*�ڵ����
5���� �ڵ���Ӱ� ������ �Է¹޾� ������ ���� ���� ����� ������ ����ϴ� ���α׷��� �ۼ��غ�����. 
��, c����� ��� ����ü��, �ٸ� ����� ��� class�� �̿��Ͽ� 
�� ����� ������ ���� ��ü�� 5�� ����� ������ �ذ����ּ���.*/

/*Ŭ���� ��� ����
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
/*Ʃ�� ��� ����
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




/*��ü���� - Ű�� �������� ����*/
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


/*������ ������
n�� �־�����, n���� �л����� �̸��� ����, ����, ���� �� ������ ������ �־����� 
����, ����, ���� ������� �켱������ �Ͽ� ���� ������ ���� �л����� ����ϴ� ���α׷��� �ۼ��غ�����.*/
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


/*��������
5���� �̸�, Ű, �����԰� �־����� �̸������� �����Ͽ� ����ϰ�, 
Ű�� ū ������ �����Ͽ� ����ϴ� ���α׷��� �ۼ��غ�����. 
��, ������ �̸��� Ű�� �־����� �ʴ´ٰ� �����ص� �����ϴ�*/
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




/*Ű, �����Ը� �������� ����
n���� �̸�, Ű, �����԰� �־����� Ű�� �������� ������������ �����Ͽ� ����ϴ� ���α׷��� �ۼ��غ�����. 
��, Ű�� ������ ��쿡�� �����԰� �� ū ����� ���� �������� �����ؾ� �մϴ�. 
Ű, �����԰� �� �� ������ ���� ���ٰ� �����ص� �����ϴ�.*/


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


/* �帥 �ð� ��� */
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
2011�� m1�� d1�Ϸκ��� 2011�� m2�� d2�ϱ����� �� �� ���� �ִ����� ����ϴ� ���α׷��� �ۼ��غ�����. 2011���� ������ �ƴ� ���̱� ������ 2���� 28�ϱ��� �ֽ��ϴ�.*/
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
/*�Լ� ��� ����
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



/*2������ ��ȯ�ϱ�
������ n�� �־����� 0�� 1�θ� �̷���� 2������ �� ���� ��ȯ�Ͽ� ����ϴ� ���α׷��� �ۼ��غ�����.*/
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


/*10������ ��ȯ�ϱ�
0�� 1�� �̷���� 2������ � ���� �־����� �� ���� �������� ��ȯ�Ͽ� ����ϴ� ���α׷��� �ۼ��غ�����.*/
/*#include<iostream>
#include<algorithm>
#include<string>
#include<cmath>

using namespace std;

int power(int n, int m){    //���� ������ �����Լ� (cmath�� pow��� �Ȱ��� ���� �ִ�.)
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



/*���״� ���2
1�� ĭ���� N��° ĭ���� �� N���� ĭ�� �ֽ��ϴ�. 
�� �� Ai���� Bi���� ���� ���� 1�� ������� ����� K�� �־����ϴ�. 
����� �� ������ ���� 1�� ĭ���� N�� ĭ���� ���� ���� �� �� �ִ��� ����ϴ� ���α׷��� �ۼ��غ�����.*/

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




/*�簢���� �� ���� 2
2�� ��� ���� N���� ���簢���� �־����ϴ�. �� ���簢������ ������ �� ���̸� ���ϴ� ���α׷��� �ۼ��غ�����.*/
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

/*��ġ�� �ʴ� �簢���� ����
��ǥ������� ���簢�� A, B�� ���� ���̰� �� ���� ���簢�� M�� �ٿ����ϴ�. 
���� �����ִ� (M���� ������ ����) ���簢�� A, B�� ������ ���� ���ϴ� ���α׷��� �ۼ��غ�����. 
��, ���簢�� A, B�� ��ġ�� �ʰ� �־����ٰ� �����ص� �����ϴ�.*/

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




/*���⿡ ���� �̵�
(0, 0)���� �����Ͽ� �� N�� ������������ �մϴ�. 
N���� ���� �����̷��� ����� ������ �Ÿ��� �־����� ��, ���� ��ġ�� ����ϴ� ���α׷��� �ۼ��غ�����.
��, dx, dy ��ũ���� Ȱ���Ͽ� ������ �ذ����ּ���.*/

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






/*�ǵ��ƿ���
(0, 0)���� �����Ͽ� �� N�� ������������ �մϴ�. 
N���� ���� �����̷��� ����� ������ �Ÿ��� �־�����, 1�ʿ� �� ĭ�� �����δٰ� ���� ��, 
�� �� �ڿ� ó������ �ٽ� (0, 0)�� ���ƿ��� �Ǵ����� �Ǵ��ϴ� ���α׷��� �ۼ��غ�����.
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
//                 break;              //�� �κп��� ��ø �ݺ����� �� ���� Ż���ϰ� �ͽ��ϴ�.
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


/*�ڵ�ķ�� - �ʱ޹� �⸻���*/
//1.û���� ������ ����
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



//2.���̷��� �˻翡 �ʿ��� �ּ� �˻��� ��
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
//     // �Է�
//     for(int i = 0; i < N; i++) {
//         cin >> x1[i] >> y1[i] >> x2[i] >> y2[i];
        
//         // OFFSET�� �����ݴϴ�.
//         x1[i] += OFFSET;
//         y1[i] += OFFSET;
//         x2[i] += OFFSET;
//         y2[i] += OFFSET;
//     }
    
//     // ���簢���� �־��� ������ 1, 2 ��ȣ�� �ٿ��ݴϴ�.
//     // ���� ������ �����ϴ� �����̹Ƿ�
//     // x2, y2�� ��ȣ�� ���� ������ �����մϴ�.
//     for(int i = 0; i < N; i++)
//         for(int x = x1[i]; x < x2[i]; x++)
//             for(int y = y1[i]; y < y2[i]; y++)
//                 checked[x][y] = i + 1;
    
//     // 1, 2 ������ �ٿ��µ���
//     // ���� ���� 1�� �����ִ� ���� �� �ִ� �ּ� x, y ���� ���� ����մϴ�.
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
    
//     // ���̸� ����մϴ�.
//     int area;
//     // Case 1. ù ��° ���簢���� ���� �������� �ʴٸ� ���̴� 0�Դϴ�.
//     if(!first_rect_exist)
//         area = 0;
//     // Case 2. ù ��° ���簢���� �����ִٸ�, ���̸� ����մϴ�.
//     else
//         area = (max_x - min_x + 1) * (max_y - min_y + 1);

//     cout << area;
//     return 0;
// }









