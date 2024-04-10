using System;
using System.Collections.Generic;

namespace CSHARP.Classes
{
    public class MySet {
        private readonly List<List<int>> buckets = [[], [], [], []];
        private int length = 0;

        public int GetLength (){
            return length;
        }

        public bool Contains(int number) {
            int index = GetBucketIndex(number);
            return buckets[index].Contains(number);
        }

        public void Add(int number) {
            if (Contains(number)) {
                return;
            }
            int index = GetBucketIndex(number);
            buckets[index].Add(number);
            length++;
        }

        public void Remove(int number) {
            if (!Contains(number)) {
                return;
            }
            int index = GetBucketIndex(number);
            buckets[index].Remove(number);
            length--;
        }

        private int GetBucketIndex(int number) {
            return Math.Abs(number.ToString().GetHashCode() % buckets.Count);
        }
    }
}