/* PSUEDOCODE
1. START
2. CREATE A REQUEST FOR THREE SCORE FROM THE USER
3. ADD THE SUM OF THE SCORES TOGETHER
4. CALCULATE THE AVERAGE (TOTAL SUM / THREE) 
5. USE THE RESULT TO PRINT OUT THE GRADE OF THE SCORE USING THE IF STATEMENT.
6. END 
*/

import java.util.Scanner;
public class ThreeScore{
public static void main(String [] args) {
Scanner input = new Scanner(System.in);
	
	int average = 0;
	int sum = 0;

	for(int reader = 1; reader <=3; reader++) {
	System.out.print("Enter score: ");
	int score = input.nextInt();

	sum = sum + score;
	average = sum / 3;
		}
	
	if(average >=90 && average <= 100){
	System.out.print("The grade is A");
}
	if(average>= 80 && average < 90){
	System.out.print("The grade is B");
}
	if(average>= 70 && average <80){
	System.out.print("The grade is C");
}
	if(average >= 60 && average < 70){
	System.out.print("The grade is D");
}
	if(average>= 0 && average < 60){
	System.out.print("The grade is F");
}

	
		}

	}	
	