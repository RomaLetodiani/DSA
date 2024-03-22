using Xunit;
using CSHARP.Classes;
using System.Diagnostics;

namespace CSHARP.Tests
{
    public class OddEvenListTests
    {
        [Fact]
        public void AddNumbers()
        {
            // Arrange
            OddEvenList list = new();

            // Act
            list.Add(1);
            list.Add(2);
            list.Add(3);

            // Assert
            Assert.Equal(3, list.Length());

        }

        [Fact]
        public void TestGettingLength()
        {
            // Arrange
            OddEvenList list = new();

            // Act
            list.Add(11);
            list.Add(22);
            list.Add(33);
            list.Add(44);
            list.Add(55);
            list.Add(66);
            list.Add(77);
            list.Add(88);
            list.Add(99);

            // Assert
            Assert.Equal(9, list.Length());
            Assert.NotEqual(list.GetEvens().Count, list.GetOdds().Count);
        }

        [Fact]
        public void TestEfficiency()
        {
            // Arrange
            OddEvenList list = new();
            Stopwatch stopwatch = new();

            // Act
            stopwatch.Start();
            for (int i = 0; i < 100000; i++)
            {
                list.Add(i);
            }
            stopwatch.Stop();

            // Assert
            Assert.True(100000 == list.Length(), "Appending large string should not fail and length should be 99999");
            Assert.True(stopwatch.ElapsedMilliseconds < 100, "Adding 100000 numbers should not take too long");
            Assert.Equal(list.GetEvens().Count, list.GetOdds().Count);

        }
    }
}
