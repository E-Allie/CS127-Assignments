#include <iostream>
#include <string>

using namespace std;


string cigar_party(int cigars, bool weekend){
	if(cigars>=40&&(cigars<=60||weekend==true))
		return "True";
	return "False";
}

int main(){
	cout<<"30 cigars, not weekend: "<<
	cigar_party(30,false)<<endl<<
	"70 cigars, weekend: "<<
	cigar_party(70, true)<<endl;
	return 0;
}