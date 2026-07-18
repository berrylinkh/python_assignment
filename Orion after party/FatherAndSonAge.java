/* PSUEDOCODE
1. START
2. CREATE A REQUEST FOR TWO AGE INPUT FOR THE FATHER AND THE SON
3. TO GET KNOW IF THE FATHER AGE IS TWICE THE SON OR NOT:
4.  MULTIPLY THE SON AGE BY TWO
5. USE THE SON AGE TO DIVIDE THE FATHER AGE 
6. USE THE RESULT TO PRINT OUT THE RESULT, THE  RESULT IS THE YEAR(S) THE FATHER AGE WILL BE TWICE THE SON.
7. END
*/

import java.util.Scanner;
public class FatherAndSonAge{
public static void main(String [] args) {
Scanner input = new Scanner(System.in);
	
	System.out.print("Enter father's age: ");
	int fatherAge = input.nextInt();

	System.out.print("Enter son age: ");
	int sonAge = input.nextInt();
	
	int years = (2 * sonAge) - fatherAge;
	if (fatherAge % sonAge !=0) {

	System.out. printf("Father age will be twice the son in %d year", years);
		}
	
	}
}