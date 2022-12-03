import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.List;
import java.io.IOException;
import java.util.HashSet;
import java.util.Set;

class AOC3 {
	
	private static int Priority(char c)
	{
		return "_abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ".indexOf(c);
	}
	
	private static int FindCommonPriority(String line)
	{
		Set first_compartment = new HashSet();
		
		for (int i = 0; i < line.length() / 2; i++)
		{
			first_compartment.add(line.charAt(i));
		}
		
		for (int i = 0; i < line.length() / 2; i++)
		{
			char c = line.charAt(line.length() - 1 - i);
			if (first_compartment.contains(c))
			{
				System.out.println(c);
				return Priority(c);
			}
		}
		
		return -1000000;
	}
	
	public static void main(String[] args) throws IOException
	{
		List<String> lines = Files.readAllLines(Paths.get("test_data.txt"));

		int sum_of_priorities = 0;

		for (String line : lines) {
			sum_of_priorities += FindCommonPriority(line);
		}
		
		System.out.println(sum_of_priorities);
	}
}