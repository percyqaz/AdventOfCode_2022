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
	
	private static Set FindItems(String line)
	{
		Set items = new HashSet();
		
		for (int i = 0; i < line.length(); i++)
		{
			items.add(line.charAt(i));
		}
		
		return items;
	}
	
	public static void main(String[] args) throws IOException
	{
		List<String> lines = Files.readAllLines(Paths.get("test_data.txt"));

		int sum_of_priorities = 0;

		for (int i = 0; i < lines.size(); i += 3) {
			
			Set elf1 = FindItems(lines.get(i));
			Set elf2 = FindItems(lines.get(i + 1));
			Set elf3 = FindItems(lines.get(i + 2));
			
			// Calculate intersection
			elf1.retainAll(elf2);
			elf1.retainAll(elf3);
			
			// Extract single element
			char common_item = (char)elf1.iterator().next();
			System.out.println(common_item);
			
			sum_of_priorities += Priority(common_item);
		}
		
		System.out.println(sum_of_priorities);
	}
}