#include<vector>
#include <iostream>

std::vector<int> precomput(int N) 
{ 
    std::vector<int> series{1500000};
    series[0] = 0; 
    series[1] = 1; 
   
    for (auto i = 2; i <= N; i++)
    {
        series[i] = (series[i-1] + series[i-2]) % 1000000; 
        std::cout << series[i] << std::endl; 
    }
    return series;
} 


int solution(int N) {
    
    auto series = precomput(N);
    auto temp = N % 1500000;

    std::cout << "The soolution " <<  series[temp] << std::endl;
    return series[temp];
}

int main()
{
    std::cout << "The soolution " <<  solution(8) << std::endl;
}