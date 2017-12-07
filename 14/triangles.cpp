#include <iostream>
#include <string>
using std::cout;
using std::endl;
using std::string;

string line(int l, std::string c){
  string line;
  while(l>0){
    line+=c;
    l--;
  }
  return line;
}

string rect(int w, int h) {
  string rec;
  for(int i=1;i<=h;i++){
    rec+=string(w,'*');
    if(i<h) rec+="\n";
  }
  return rec;
}

/*
 *
 **
 ***
 ****
 */
string tri1(int h) {
  string tri;
  for(int i=1;i<=h;i++){
    tri+=(string(i,'*'));
    if(i<h) tri+="\n";
  }
  return tri;
}


/*
   *
  ***
 *****
 */
string tri2(int h) {
  string tri;
  for(int base=h;h>0;h--){
    tri.insert(0,string(base-h,' ')+string(2*h-1,'*'));
    if(h>1) tri.insert(0,"\n");
  }
  return tri;
}

/*
  *
 **
***
 */
string tri3(int h) {
  string tri;
  for(int i=1;i<=h;i++){
    tri+=string(h-i,' ')+string(i,'*');
    if(i<h) tri+="\n";
  }
  return tri;
}

int main(){
  string s="hello";
  cout<<line(5,"yes")<<endl<<endl<<
  rect(8,4)<<endl<<endl<<
  tri1(5)<<endl<<endl<<
  tri2(5)<<endl<<endl<<
  tri3(5)<<endl;
}

