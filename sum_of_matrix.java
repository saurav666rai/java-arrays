import java.util.Arrays;
import java.util.Scanner;
public class sum_of_matrix {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter the rows");
        int rows = sc.nextInt();
        System.out.println("Enter the column");
        int col = sc.nextInt();
        if (rows==col){
            int matrix1[][] = new int[rows][col];
            int matrix2[][] = new int[rows][col];
            int total[][] = new int[rows][col];
            // first matrix input
            for (int i = 0; i < rows; i++) {
                for (int j = 0; j < col; j++) {
                    System.out.println("Enter the first matrix data");
                    matrix1[i][j] = sc.nextInt();
                }
            }// second matrix data input
            for (int i=0; i<rows; i++){
                for (int j=0; j<col; j++){
                    System.out.println("Enter the second matrix data");
                    matrix2[i][j]=sc.nextInt();
                }
            }// print first matrix
            System.out.println("second matrix");
            for(int i=0; i<rows; i++){
                System.out.println(Arrays.toString(matrix1[i]));
            }
            System.out.println("second matrix");
            for (int i=0; i<rows; i++){
                System.out.println(Arrays.toString(matrix2[i]));
            }// sum of matrix
            for (int i=0; i<rows; i++){
                for (int j=0; j<col; j++){
                    total[i][j]=matrix1[i][j]+matrix2[i][j];
                }
            }
            System.out.println("sum of two matrix");
            for (int i=0; i<rows; i++){
                System.out.println(Arrays.toString(total[i]));
            }
        }else {
            System.out.println("------XXXXXXXXXXXXX---------");
            System.out.println("Rows and Column Should be Same");
        }
    }
}
