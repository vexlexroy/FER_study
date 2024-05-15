
#include <stdio.h>
#include <signal.h>
#include <unistd.h>
#include <stdlib.h>
#include <pthread.h>
#include <stdatomic.h>
#include <semaphore.h>
#include<sys/shm.h>
#include<sys/stat.h>
#include<sys/wait.h>
#include<sys/ipc.h>
#include<sys/types.h>
#include<time.h>

int ID;
int const max=5;
int const vrjeme=10;

struct share{
int otvoreno;
int br_mjesta;
sem_t bsemslobodan;
sem_t osemklient;
sem_t bsemklient;
sem_t osisan;
} *var;

void spavanje(){
	
}
void brisi(int sig){
	(void) shmdt((char *)var);
	(void) shmctl(ID,IPC_RMID,NULL);
	exit(0);
}

void frizerka(){
	int ispisano=0;
	int c=0;
	printf("Frizerka: Otvaram salon\n");
	printf("        : Postavljam znak OTVORENO\n");
	var->otvoreno=1;
    while(var->otvoreno){
    	if(var->br_mjesta==max){
			if(!ispisano){
        	printf("Frizerka: spavam dok nema klijeneata\n");
			ispisano=1;
			}
        	sleep(1);
        	c++;
    	}
    	else{
			ispisano=0;
            sem_wait(&(var->osemklient));
        	sem_post(&(var->bsemslobodan));
        	sem_wait(&(var->osisan));
			printf("Frizerka: Zavrsial sam frizuru, Sljedeci!\n");
        	c++;
    	}
    	if(c>=vrjeme+max){
        	var->otvoreno=0;
			if(max-var->br_mjesta)
			printf("Frizerka: Nemam vise vremena vas %d  moze doci sutra\n",max-var->br_mjesta);
    	}
    }
	printf("Frizerka: zatvaram salon\n");
	printf("        : Postavljam znak ZATVORENO\n");

}

void klijent(int index){
	int i= index;
	if(var->otvoreno){
	printf("Klijent(%d): Zelim na frizuru\n",i);
	
	if(var->br_mjesta>=1&&var->otvoreno==1){
	printf("Klijent(%d): Ulazim u cekaonicu\n",i);
	sem_wait(&(var->bsemklient));//bsem
	var->br_mjesta--;
	sem_post(&(var->bsemklient));//bsem
	sem_post(&(var->osemklient));
	}
	else{
	printf("Klient(%d): Nema mjesta vracam se sutra\n",i);
	exit(0);
	}
	
	sem_wait(&(var->bsemslobodan));
	printf("Klient(%d): Pocinjem raditi frizuru\n",i);
	var->br_mjesta++;
	sleep(2);
	printf("Klient(%d): Frizura mi je gotova\n",i);
	
	sem_post(&(var->osisan));
	}
	else{
		printf("Klient(%d): Dosao nakon Zatvaranja\n",i);
	}
	
	
}

int main (void){
	
	srand(time(NULL));
	ID=shmget(IPC_PRIVATE,sizeof(int),0600);
	var=(struct share *) shmat(ID,NULL,0);
	//sigset(SIGINT,brisi);
	sem_init(&(var->bsemklient),1,1);
	sem_init(&(var->bsemslobodan),1,0);
	sem_init(&(var->osemklient),1,0);
	sem_init(&(var->osisan),1,0);
	var->br_mjesta=max;
	int n=5;
	int c=0;
	
	
	if(fork()!=0){
	    frizerka();
	    //exit(0);
	}	
	else{
		for(int i=0;i<n;i++){
			if(fork()==0){
				klijent(i+1);
				break;
			}
			else{
				int z=rand()%3000000;
				usleep(z);
				//nista
			}
		}
	}
	
	
	//for(int i=0;i<n+1;i++)
	(void) wait(NULL);
	
	brisi(0);
}