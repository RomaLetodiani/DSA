using System;
using System.Collections.Generic;

namespace CSHARP.Classes
{
    public class StringBuilder
    {
        private readonly List<string> parts;
        private int length;

        public StringBuilder()
        {
            parts = [];
            length = 0;
        }

        public void Append(string str)
        {
            parts.Add(str);
            length += str.Length;
        }

        public int GetLength()
        {
            return length;
        }

        public string GetString()
        {
            return string.Concat(parts);
        }
    }
}
