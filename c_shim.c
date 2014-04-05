#include <stdio.h>
#include <stdlib.h>

int main(int argc, char** argv) {
	printf("Hello from C!");
	printf("Executing:");
	printf(argv[1]);

	//system(argv[1]);
	system("g++ cpp_shim.cpp -o cpp_shim");
	system("./cpp_shim python ~/RubeGoldbergHackathon/SRGH.py");
	return 0;
}