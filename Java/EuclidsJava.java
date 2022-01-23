public class EuclidsJava
{
	public static void main(String args[]){
		int m=16;
		int n=12;
		int rem;
		
		while(rem!=0){
			rem=m%n;
			m=n;
			n=rem;
		}
		System.out.println(rem);		
	}
}