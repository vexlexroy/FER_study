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


int Id;
struct shared{
	int A;
	int ZASTAVICE[2];
	int PRAVO;
};
struct shared *VAR;
int M;


void brisi(int sig)
{
   //oslobađanje zajedničke memorije
   (void) shmdt((char *) VAR);
   (void) shmctl(Id, IPC_RMID, NULL);
   exit(0);
}

void uKriticni(int i,int j){
	VAR->ZASTAVICE[i]=1;
	while(VAR->ZASTAVICE[j]!=0){
		if(VAR->PRAVO==j){
		VAR->ZASTAVICE[i]=0;
		while(VAR->PRAVO==j){
			//nista
		}
		VAR->ZASTAVICE[i]=1;
		}
	}
	
}

void izKriticnog(int i,int j){
	VAR->PRAVO=j;
	VAR->ZASTAVICE[i]=0;
}
void proces(int i){
	for(int x=0;x<M;x++){
	int j=1-i;
	uKriticni(i,j);
	printf("\nKRiticni = %d\n",i);
	VAR->A++;
	izKriticnog(i,j);
	}	
}


int main (int argc, char *argv[]){
	M = atoi(argv[1]);
	Id = shmget(IPC_PRIVATE, sizeof(int), 0600);
	
	VAR = (struct shared *) shmat(Id, NULL, 0);
    VAR->A = 0;
	VAR->ZASTAVICE[0] = 0;VAR->ZASTAVICE[1] = 0;
	VAR->PRAVO = 0;
	
	if (Id == -1)
      exit(1);  // greška - nema zajedničke memorije 
 
  
   
  // sigset(SIGINT, brisi);//u slučaju prekida briši memoriju
 
   // pokretanje paralelnih procesa
   
   if (fork() == 0) {
      proces(1);
	  //printf("\nFork 1\n");
      exit(0);
   }
   proces(0);
   
   
   
   
   
   (void) wait(NULL);
   (void) wait(NULL);
   printf("\nA: = %d\n",VAR->A);
   brisi(0);
	
	
}