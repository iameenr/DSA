import java.io.*;

public class files
{
	public static void main(String args[]) throws IOException
	{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		System.out.println("Enter a file name: ");
		String fname=br.readLine();
		
		File f =new File(fname);
		String result=f.exists()? "yeh bro":"nope";
		System.out.println(result);
	}
}
