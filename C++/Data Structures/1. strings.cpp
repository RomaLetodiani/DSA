#include <iostream>
#include <string>
#include <algorithm>

int main() {
    // O(1)
    std::string name = "World";
    std::cout << "Hello, " << name << "!" << std::endl; // N

    // O(min(M, K)) ~ O(N)
    std::string test = "abcdef"; // M - length of test
    std::cout << test.compare(0, 3, "abc") << std::endl; // K - length of substring

    // O(M * K) ~ O(N^2)
    std::string test2 = "abcdabcd"; // M - length of test2
    std::cout << test2.find("bc") << std::endl; // K - length of substring

    // O(M * K) ~ O(N^2)
    std::string test3 = "abcdabcd"; // M - length of test3
    size_t count = 0;
    size_t pos = 0;
    while ((pos = test3.find("bc", pos)) != std::string::npos) {
        count++;
        pos += 2;
    }
    std::cout << count << std::endl; // K - length of substring

    // O(M * K) ~ O(N^2)
    std::string test4 = "abcdabcd"; // M - length of test4
    size_t start_pos = 0;
    while ((start_pos = test4.find("bc", start_pos)) != std::string::npos) {
        test4.replace(start_pos, 2, "TTT"); // K - length of replacement
        start_pos += 3;
    }
    std::cout << test4 << std::endl; // K - length of substring

    // O(N)
    std::string test5 = "abcdabcd"; // M - length of test5
    size_t prev_pos = 0, pos2 = 0;
    while ((pos2 = test5.find("bc", prev_pos)) != std::string::npos) {
        std::cout << test5.substr(prev_pos, pos2 - prev_pos) << std::endl;
        prev_pos = pos2 + 2;
    }
    std::cout << test5.substr(prev_pos) << std::endl;

    // O(N)
    std::string arr[] = {"11", "22", "33"};
    std::string separator = "++";
    for (int i = 0; i < sizeof(arr) / sizeof(arr[0]) - 1; i++) {
        std::cout << arr[i] << separator;
    }
    std::cout << arr[sizeof(arr) / sizeof(arr[0]) - 1] << std::endl;

    // O(N)
    std::string text2 = "abcdabcd"; // M - length of text2
    std::transform(text2.begin(), text2.end(), text2.begin(), ::toupper);
    std::cout << text2 << std::endl;

    return 0;
}
