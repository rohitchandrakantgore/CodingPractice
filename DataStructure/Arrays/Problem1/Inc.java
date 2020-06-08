package Inc;

import java.util.*;

public class Inc {
	// Scanner sc=new Scanner(System.in);

	public static void main(String[] args) {
		// take array
		int[] input = { 3, 5, 0, 2, 1, 2, 0, 3, 0, 1, 0, 6, 1, 2, 0, 0, 0, 1 };
		// identiy total case
		int totalcases = input[0];
		int starter = 2, arraysize = input[1];
		int arraylimit;
		for (int i = 0; i < totalcases; i++) {
			arraylimit = starter + arraysize;
			int[] array = new int[arraysize];
			int array2 = 0;
			for (int j = starter; j < arraylimit; j++, array2++) {
				array[array2] = input[j];
			}

			if (arraylimit < input.length - 1) {
				arraysize = input[arraylimit];
				starter = arraylimit + 1;
			}
			// printarray(array);
			// System.out.println("\n--Before sort---");
			// printarray(array);
			int[] sorted = sortarray(array);
			// System.out.println("\n--after sort--- "+i);
			printarray(sorted);
		}

	}

	private static void printarray(int[] sorted) {
		for (int i = 0; i < sorted.length; i++) {
			System.out.print(sorted[i] + " ");
		}

	}

	private static int[] sortarray(int[] array) {
		for (int i = 0; i < array.length; i++) {
			for (int j = i + 1; j < array.length; j++) {
				if (array[i] > array[j]) {
					int temp = array[i];
					array[i] = array[j];
					array[j] = temp;
				}
			}
		}
		return array;
	}
}
