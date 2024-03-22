using System;
using System.Collections.Generic;

namespace CSHARP.Classes
{
    public class OddEvenList
    {
        private readonly List<int> odds = [];
        private readonly List<int> evens = [];

        public int Length()
        {
            return odds.Count + evens.Count;
        }

        public void Add(int num)
        {
            if (num % 2 == 0)
            {
                evens.Add(num);
            } 
            else
            {
                odds.Add(num);
            }
        }

        public List<int> GetOdds()
        {
            return odds;
        }

        public List<int> GetEvens()
        {
            return evens;
        }
    }
}