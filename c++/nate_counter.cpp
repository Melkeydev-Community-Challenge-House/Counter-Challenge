#include <iostream>
#include <string.h>
#include <stdio.h>

using namespace std;

int 
main(void)
{
	int count = 0; int age = 0; 
	float times_around_num; string times_around_str;
	string tmpin = "";
	string countin;
	
	std::cout << "\nWould you like to start[y/n]? "; 
	std::getline(std::cin, tmpin);
	std::cout << "\nwhat";
	while(tmpin.length() == 0)
	{
		std::cout << "Try Again [y/n]? ";
		std::getline(std::cin, tmpin);
		if(tmpin == "y")
		{ break; }
		if(tmpin == "n")
		{ return 0; }
	}	

	std::cout << "\nHow many times would you like to go around?[int] ";
	std::getline(std::cin, times_around_str);
	
	try
	{
		times_around_num = std::stoi(times_around_str);
	}
	catch(std::invalid_argument const &e)
	{
		std::cerr << "Not a number!" << '\n';
	}
	catch(const std::exception &e)
	{
		std::cerr << "Problems, bigger problems than just NaN" << "\n"; 
	}

	std::cout << times_around_num << "\n";
	std::cout << count << "\n";

	while(count < times_around_num + 1)
	{
		std::getline(std::cin, countin);
		std::cout << count;
		if(count == times_around_num)
		{
			count = 0;
			age += 1;
			std::cout << "\n	" << age << " times around";
		}
		count++;
	}
	return 0;
}
