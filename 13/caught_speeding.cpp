#include <iostream>

using namespace std;

int speeding(int speed, bool day){
	if(day==true) speed-=5;
	if(speed>=61&&speed<=80) return 1;
	else if(speed>81) return 2;
	return 0;
	
}


int main(){
	cout<<"60 mph, not birthday: "<<
	speeding(60, false)<<endl<<
	"65 mph, not birthday: "<<
	speeding(65,false)<<endl<<
	"65 mph, birthday: "<<
	speeding(65,true)<<endl<<
	"85 mph, not birthday: "<<
	speeding(85,false)<<endl;
	return 0;
}