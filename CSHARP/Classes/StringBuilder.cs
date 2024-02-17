using System;
using System.Collections.Generic;

namespace CSHARP.Classes
{
    public class StringBuilder
    {
        private List<string> parts;
        private int length = 0;

        public StringBuilder()
        {
            parts = new List<string>();
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
