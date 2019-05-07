
#include <iostream>
#include <iomanip>
#include <fstream>
#include <sstream>
using namespace std;

int main(){
  ifstream inFile;
  ofstream ofile;
  bool txid = 0;
  ofile.open("txid2.csv");
  inFile.open("blockdata.txt");
  ofstream out;
  //std::cout << "/* message */" << '\n';
  if(!inFile || !ofile)
  {
    cout << "unable to open file";
    return 0;
  }

  string descript;

  while(getline(inFile,descript))
  {
    //  \"tx\": [
    //cout << descript << '\n';
    if(descript.compare("  \"tx\": [") == 0)
    {
      txid = 1;
    //  cout<<"hello5"<<endl;
    ///  cout<<descript<<endl;
      //break;
    }

    string temp,w;
//int i = 0;
    while(txid )
    {
      //i++;
      getline(inFile,descript);
      stringstream ss(descript);
      ss>>w;
      stringstream ss1(w);
      getline(ss1,temp,',');
      if(temp.compare("]") == 0)
      {
        //std::cout << "/* message */" << '\n';
        //cout << temp << '\n';
        txid = 0;
      }
      else
      { //cout << "/* hello1 */" << '\n';
        ofile << temp << endl;
      }

    }
  }


  cout << "done" << '\n';
  return 0;
}
