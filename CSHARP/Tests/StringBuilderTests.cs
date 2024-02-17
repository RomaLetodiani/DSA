using Xunit;
using CSHARP.Classes;
using System.Diagnostics;

namespace CSHARP.Tests
{
    public class StringBuilderTests
    {
        [Fact]
        public void TestStringBuilderAppend()
        {
            // Arrange
            StringBuilder sb = new();

            // Act
            sb.Append("Hello, ");
            sb.Append("World!");

            // Assert
            Assert.Equal("Hello, World!", sb.GetString());
        }
        
        [Fact]
        public void TestStringBuilderGetLength()
        {
            // Arrange
            StringBuilder sb = new();
            string first = "Hello";
            string second = "World!";

            // Act
            sb.Append(first);
            sb.Append(second);

            // Assert
            Assert.True(first.Length + second.Length == sb.GetLength(), "Length should be the sum of the lengths of appended strings");
        }

        [Fact]
        public void TestAppendingLargeString()
        {
            // Arrange
            StringBuilder sb = new();

            // Act
            for (int i = 1; i < 100000; i++)
            {
                sb.Append("a");
            }

            // Assert
            Assert.True(99999 == sb.GetLength(), "Appending large string should not fail and length should be 99999");
        }

        [Fact]
        public void TestEfficiency()
        {
            // Arrange
            StringBuilder sb = new();
            Stopwatch stopwatch = new Stopwatch();

            // Act
            stopwatch.Start();
            for (int i = 0; i < 100000; i++)
            {
                sb.Append("a");
            }
            stopwatch.Stop();

            // Assert
            Assert.Equal(100000, sb.GetLength());
            Assert.True(stopwatch.ElapsedMilliseconds < 100, "Appending 100,000 characters should take less than 100 milliseconds.");
        }
    }
}
