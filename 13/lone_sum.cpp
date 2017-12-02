#include <iostream>

using namespace std;


int lone_sum(int a, int b, int c){
	if(a==b&&b==c) return 0;
	else if(a==b) return c;
	else if(a==c) return b;
	else if(b==c) return a;
	else return a+b+c;
}


int main(){
	cout<<"Lone Summation"<<endl<<
	"1+2+3="<<lone_sum(1,2,3)<<endl<<
	"3+2+3="<<lone_sum(3,2,3)<<endl<<
	"3+3+3="<<lone_sum(3,3,3)<<endl;
	return 0;
}