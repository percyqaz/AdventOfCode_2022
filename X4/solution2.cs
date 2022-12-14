using System;
using System.IO;
using System.Collections.Generic;
using System.Linq;

public class Solution 
{
   static int AbyssPosition = 0;
   static int Left = 500;
   static int Right = 500;
   static HashSet<double> Positions = new();

   static double HashPosition(int x, int y)
   {
      return (double)x + (1.0 / (double)(y + 1));
   }

   static void Mark(int x, int y)
   {
        Positions.Add(HashPosition(x, y));
        Left = Math.Min(Left, x);
        Right = Math.Max(Right, x);
   }

   static bool Test(int x, int y)
   {
	   if (y == AbyssPosition) { return false; }
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
                    Mark(x, y);
                    y++;
                }
                while (y > p.Item2)
                {
                    Mark(x, y);
                    y--;
                }
            }
            else if (p.Item1 != x)
            {
                while (x < p.Item1)
                {
                    Mark(x, y);
                    x++;
                }
                while (x > p.Item1)
                {
                    Mark(x, y);
                    x--;
                }
            }
            AbyssPosition = Math.Max(AbyssPosition, p.Item2 + 2);
        }

        Mark(x, y);
    }

    static bool Sand()
    {
        var x = 500;
        var y = 0;
		
		if (!Test(500, 0)) { return false; }

        while (true)
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

		// impossible
        return false;
    }
	
	static void Render(string file)
	{
		var text = new List<string>();
		
		for (int y = 0; y < AbyssPosition; y++)
		{
			var line = "";
			for (int x = Left; x <= Right; x++)
			{
				if (Test(x, y))
				{
					line += ".";
				}
				else
				{
					line += "#";
				}
			}
			text.Add(line);
		}
		
		File.WriteAllLines(file, text);
	}

   public static void Main(string[] argv)
   {
        var lines = File.ReadAllLines("test_data.txt");
        foreach (var line in lines)
        {
            Setup(line);
        }
		Render("before.txt");

        var sands = 0;
        while (Sand()) { sands++; }
        Console.WriteLine(sands);
		Render("after.txt");
   }
}