package z1;

import java.util.Random;
import java.util.Scanner;
import java.util.*;

public class Main {

	public static void main(String[] args) {
		int[] polj=new int[10];
		
		decreasing(polj);
		
		for(int x:polj) {
			System.out.println(x);
		}

	}
	
	static void decreasing(int[] arr) {
		Random r= new Random();
		int num = arr.length;
		if(num!=0) {
			arr[0]=r.nextInt(50000, 100001);
			for(int i=1;i<num;i++) {
				if(arr[i-1]!=1&&arr[i-1]!=0)
					arr[i]=r.nextInt((int)arr[i-1]/2, arr[i-1]+1);
				else
					arr[i]=0;
			}
		}
	}

}
