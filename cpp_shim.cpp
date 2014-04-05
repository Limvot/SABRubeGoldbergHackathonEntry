#include <iostream>
#include <string>
#include <cstdlib>

int main(int argc, char** argv) {
	std::string callString;
	for (int i = 1; i < argc; i++) {
		callString += argv[i];
		callString += " ";
	}
	std::cout << "Hello from C++! Executing: " << callString << std::endl;
	std::system(callString.c_str());
	return 0;
}