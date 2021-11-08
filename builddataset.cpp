#include <iostream>
#include <vector>
#include <cstdlib> // Header file needed to use srand and rand
#include <ctime> // Header file needed to use time
#include <fstream>
#include <iomanip>
using namespace std;

int main()
{
	
	int usernum = 250;
	
	ofstream file;
	file.open("d:\\dataset.txt");
	
	int cul = 40;
	
	int seed = time(0);
	for (int i=1;i <= 100;i++) {
		for (int j=1;j <= cul;j++) {
			int dice = rand() % 172 + 1;
			int score = rand() % 5 + 1;
			file << i << "," << dice << "," << score << endl; 
		}
	}
	
	return 0;
 } 
