using System;

namespace CSHARP.DataStructures
{
    class StringExamples
    {
        static void Strings()
        {
            // O(1)
            string name = "World";
            Console.WriteLine($"Hello, {name}!"); // N

            // O(min(M, K)) ~ O(N)
            string test = "abcdef"; // M - length of test
            Console.WriteLine(test.StartsWith("abc")); // K - length of substring

            // O(M * K) ~ O(N^2)
            string test2 = "abcdabcd"; // M - length of test2
            Console.WriteLine(test2.IndexOf("bc")); // K - length of substring

            // O(M * min(L, K)) ~ O(N^2)
            string test3 = "abcdabcd"; // M - length of test3
            int count = 0;
            int pos = 0;
            while ((pos = test3.IndexOf("bc", pos)) != -1)
            {
                count++;
                pos += 2;
            }
            Console.WriteLine(count); // K - length of substring

            // O(M * K) ~ O(N^2)
            string test4 = "abcdabcd"; // M - length of test4
            int start_pos = 0;
            while ((start_pos = test4.IndexOf("bc", start_pos)) != -1)
            {
                test4 = test4.Remove(start_pos, 2).Insert(start_pos, "TTT"); // K -
            }
        }

        static void Main(string[] args)
        {
            Strings();
        }
    }
}
