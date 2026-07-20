public class MethodTask{
	public static void main ( String [] args){
	String greetingResult = printWelcomeMessage();
	int doubleItResult = doubleIt(3);
	boolean isNegativeResult = isNegative(-1);
	int multipleResult = printTmetable(3);
	int averageResult = average(2,3,4);
	boolean rangeResult = isRange(3, 5, 7);

	System.out.println(greetingResult);
	System.out.println(doubleItResult);
	System.out.println(isNegativeResult);
	System.out.println(multipleResult);
	System.out.println(averageResult);
	System.out.println(rangeResult);	
}

public static String printWelcomeMessage (){
String greeting = "Welcome to java";
return greeting; 
	
	}
public static int doubleIt (int n){
int doubleIt = n * 2;
return doubleIt; 
	}
public static boolean isNegative (int n){
 if (n < 0) {
return true;
	}

public static int printTmetable (int n){
int multiple = n;
return multiple; 
	
	}
public static int average (int a, int b, int c){
int average = a + b + c / 3;
return average; 
	
	}
public static boolean isRange (int a, int low, int high){
if (a < low && a < high) {
return true; 
			}
		}
	
	}

