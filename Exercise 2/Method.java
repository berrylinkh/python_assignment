public class Method{
	public static void main ( String [] args){
	int sumResult = add(10,5);
	int subtractResult = subtract(12, 7);
	System.out.println(sumResult);
	System.out.println(subtractResult);	
}

public static int add (int a, int b){
int sum = a + b;
return sum; 
	
	}
 public static int subtract (int a, int b){
int sub = a - b;
return sub; 
	}
}