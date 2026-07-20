public class MethodTasks{
	public static void main ( String [] args){
	String greetingResult = printWelcomeMessage();
	int doubleItResult = doubleIt(3);
	int multiple = 5;
	int averageResult = average(8, 5, 3);
	

	System.out.println(greetingResult);
	System.out.println(doubleItResult);

	//System.out.println(multipleResult);
	System.out.println(averageResult);
	
}
public static String printWelcomeMessage (){
	return "Welcome to java"; 
	}
public static int doubleIt (int n){
int doubleIt = n * 2;
return doubleIt; 
	}
public static int average(int a, int b, int c){
int average = (4 + 5 + 6) / 3;
return average; 
		
	}
}

