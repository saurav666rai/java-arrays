import java.util.Arrays;
import java.util.Scanner;

public class transpose {
    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        System.out.println("Enter the rows");
        int rows=sc.nextInt();
        System.out.println("Enter the column");
        int col=sc.nextInt();
        int matrix1[][]=new int[rows][col];
        int transpose[][]=new int[rows][col];
        for (int i=0; i<rows; i++){
            for (int j=0; j<col; j++){
                System.out.println("Enter the matrix data");
                matrix1[i][j]=sc.nextInt();
            }
        }
        System.out.println("original matrix");
        for (int i=0; i<rows; i++){
            System.out.println(Arrays.toString(matrix1[i]));
        }// transpose
        for (int i=0; i<rows; i++){
            for (int j=0; j<col; j++){
                transpose[i][j]=matrix1[j][i];
            }
        }
        System.out.println("After Transpose ");
        for (int i=0; i<rows; i++){
            System.out.println(Arrays.toString(transpose[i]));
        }
    }
}
