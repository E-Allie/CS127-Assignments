#include <iostream>
#include <string>
#include <sstream>
#include <cctype>

using namespace std;

string piglatin(string in){

	istringstream eng(in);
	string word, out;
	string hold="";

	while(eng>>word){
		if(isalpha(word.back())==false){
			hold=word.back();
			word.pop_back();
		};

		if(tolower(word[0],locale())=='a'||tolower(word[0],locale())=='e'||
			tolower(word[0],locale())=='i'||tolower(word[0],locale())=='o'||
			tolower(word[0],locale())=='u'){
			word+="yay";
		}
		else{
			word+=tolower(word[0],locale());
			word+="ay";
			word.erase(0,1);
		};

		if(hold!=""){
			word+=hold;
			hold="";
		};

		out+=word+' ';
	}

	out[0]=toupper(out[0],locale());
	if(isalpha(out.back())==true) out[out.size()-1]='.';
	return out;
}

int main(){
	string in="Test input.";
	cout<<piglatin(in)<<endl<<
	piglatin("Wow this works, now with most punctuation!")<<endl;
	return 0;
}