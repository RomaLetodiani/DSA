using Xunit;
using CSHARP.Classes;
using System.Diagnostics;

namespace CSHARP.Tests{
    public class MySetTests
    {
        [Fact]
        public void TestMySetAdd()
        {
            // Arrange
            MySet set = new();

            // Assert
            Assert.Equal(0, set.GetLength());
            
            // Act
            set.Add(1);
            set.Add(2);
            set.Add(3);

            // Assert
            Assert.Equal(3, set.GetLength());
        }

        [Fact]
        public void TestMySetLength()
        {
            // Arrange
            MySet set = new();

            // Act and Assert
            Assert.Equal(0, set.GetLength());

            set.Add(1);
            Assert.Equal(1, set.GetLength());
            
            set.Add(2);
            Assert.Equal(2, set.GetLength());

            set.Add(3);
            Assert.Equal(3, set.GetLength());
        }

        [Fact]
        public void TestMYSetRemove()
        {
            // Arrange
            MySet set = new();

            // Act
            set.Add(1);
            set.Add(2);
            set.Add(3);

            // Assert
            Assert.Equal(3, set.GetLength());

            // Act
            set.Remove(1);
            Assert.Equal(2, set.GetLength());
            Assert.False(set.Contains(1));
        }

        [Fact]
        public void TestMYSetContains()
        {
            // Arrange
            MySet set = new();

             // Act
            set.Add(1);
            set.Add(2);
            set.Add(3);

             // Assert
            Assert.True(set.Contains(1));
            Assert.True(set.Contains(2));
            Assert.True(set.Contains(3));
            Assert.False(set.Contains(4));
        }
    }
}