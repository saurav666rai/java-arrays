import java.util.Arrays;
import java.util.PropertyResourceBundle;
import java.util.Scanner;
public class multiplacation {
    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        System.out.println("ENTER THE rows");
        int rows=sc.nextInt();
        System.out.println("Enter the column");
        int col=sc.nextInt();
        int matrix1[][]=new int[rows][col];
        int matrix2[][]=new int[rows][col];
        int matrix3[][]=new int[rows][col];
        //first matrix input
        for (int i=0; i<rows; i++){
            for (int j=0; j<col; j++){
                System.out.println("Enter the first matrix data");
                matrix1[i][j]=sc.nextInt();
            }
        }//second matrix input
        for (int i=0; i<rows; i++){
            for (int j =0; j<col; j++){
                System.out.println("Enter the second matrix data");
                matrix2[i][j]=sc.nextInt();
            }
        }// print first matrix
        for (int i=0; i<rows; i++){
            System.out.println(Arrays.toString(matrix1[i]));
        }// print second matrix
        System.out.println("second matrix");
        for (int i=0; i<rows; i++){
            System.out.println(Arrays.toString(matrix2[i]));
        }// multiplication of matrix
        for (int i=0; i<rows; i++){
            for (int j=0; j<col; j++){
                for (int k=0; k<col; k++){
                    matrix3[i][j]=matrix1[i][k]*matrix2[j][k];
                }
            }
        }
        System.out.println("multiplication of matrix");
        for (int i=0; i<rows; i++){
            System.out.println(Arrays.toString(matrix3[i]));
        }
    }
}
