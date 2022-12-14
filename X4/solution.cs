using System;
using System.IO;
using System.Collections.Generic;
using System.Linq;

public class Solution 
{

   static int AbyssPosition = 0;
   static List<double> Positions = new();

   static double HashPosition(int x, int y)
   {
      return (double)x + (1.0 / (double)y);
   }

   static void Mark(int x, int y)
   {
        Positions.Add(HashPosition(x, y));
   }

   static bool Test(int x, int y)
   {
        return !Positions.Contains(HashPosition(x, y));
   }

   static IEnumerable<(int, int)> ParseLine(string line)
   {
      var split = line.Split(new[] { " -> " }, StringSplitOptions.None);
      foreach (var pos in split)
      {
         var split2 = pos.Split(new[] { "," }, StringSplitOptions.None);
         yield return (Int32.Parse(split2[0]), Int32.Parse(split2[1]));
      }
   }

    static void Setup(string line)
    {
        var items = ParseLine(line).ToList();

        var x = items[0].Item1;
        var y = items[0].Item2;

        items.RemoveAt(0);
        
        foreach (var p in items)
        {
            if (p.Item2 != y)
            {
                while (y < p.Item2)
                {
                    Positions.Add(HashPosition(x, y));
                    y++;
                }
                while (y > p.Item2)
                {
                    Positions.Add(HashPosition(x, y));
                    y--;
                }
                AbyssPosition = Math.Max(AbyssPosition, y);
            }
            if (p.Item1 != x)
            {
                while (x < p.Item1)
                {
                    Positions.Add(HashPosition(x, y));
                    x++;
                }
                while (x > p.Item1)
                {
                    Positions.Add(HashPosition(x, y));
                    x--;
                }
            }
        }

        Positions.Add(HashPosition(x, y));
    }

    static bool Sand()
    {
        var x = 500;
        var y = 0;

        while (y <= AbyssPosition)
        {
            if (Test(x, y + 1))
            {
                y++;
            }
            else if (Test(x - 1, y + 1))
            {
                x--; y++;
            }
            else if (Test(x + 1, y + 1))
            {
                x++; y++;
            }
            else
            {
                Mark(x, y);
                return true;
            }
        }

        return false;
    }

   public static void Main(string[] argv)
   {
        var lines = File.ReadAllLines("test_data.txt");
        foreach (var line in lines)
        {
            Setup(line);
        }

        var sands = 0;
        while (Sand()) { sands++; }
        Console.WriteLine(sands);
   }
}