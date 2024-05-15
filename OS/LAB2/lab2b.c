#include <stdio.h>
#include <signal.h>
#include <sys/types.h>
#include <sys/ipc.h>
#include <sys/shm.h>
#include <sys/wait.h>
#include <sys/stat.h>
#include <unistd.h>
#include <stdlib.h>
#include <stdatomic.h>
#include <pthread.h>



int Id;

atomic_int *ULAZ;
atomic_int *BROJ;
int M,N;


atomic_int A=0;
	
//pthread_mutex_t lock;

int max(atomic_int *p,int n){
	int pom= p[0];
	for(int k=1;k<N;k++){
		if(pom<p[k]){
			pom=p[k];
		}
	}
	return pom;
	
}

void uKriticni(int i){
	ULAZ[i]=1;
	BROJ[i] = max(BROJ,N);
	ULAZ[i]=0;
	for(int j=0;j<N;j++){
		while(ULAZ[j]!=0 || (BROJ[j] != 0 && (BROJ[j] < BROJ[i] || (BROJ[j] == BROJ[i] && j < i)))){
			// nista;
		}
	}
	
}
void izKriticnog(int i){
	BROJ[i]=0;
}

void *proces(void *in){
	//pthread_mutex_lock(&lock);
	int c;
	int i=*(int*)in;
	for(c=0;c<M;c++){
		
		uKriticni(i);
		
		A++;
		printf("\nIZVRSAVA DRETVU: %d\n", i);
		
		izKriticnog(i);
	}
	//pthread_mutex_unlock(&lock);
	
}




int main (int argc, char *argv[]){
	

	M = atoi(argv[1]);
	N = atoi(argv[2]);
	pthread_t dretve[N];
	atomic_int pBROJ[N];
	atomic_int pULAZ[N];
	BROJ=&pBROJ[0];
	ULAZ=&pULAZ[0];
	printf("\nM,N: %d %d\n", M,N);
	
	void *y;
	
	for(int x=0;x<N;x++){
		y=&x;
		pthread_create(&dretve[x],NULL,proces,y);
		usleep(1000);
   }

	for(int x=0;x<N;x++){
		(void) wait(NULL);
	}
	//pthread_mutex_destroy(&lock);
	printf("\nA:= %d\n",A);
	
}