import java.io.File;  // Import the File class
import java.io.FileNotFoundException;  // Import
import java.util.Scanner;

public class Solution {
    public static void main(String[] args) {
        try {
            File myObj = new File("input.txt");
            Scanner myReader = new Scanner(myObj);
            while (myReader.hasNextLine()) {
                String data = myReader.nextLine();
                System.out.println(data.substring(1,data.length()-1));
            }
            myReader.close();
        } catch (FileNotFoundException e) {
            System.out.println("An error occurred.");
            e.printStackTrace();
        }
    }
}
