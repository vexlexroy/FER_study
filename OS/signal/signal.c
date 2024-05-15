#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <signal.h>
#include <time.h>
#include <errno.h>
#include <stdbool.h>

// /-kod za vrijeme -------------------------------------------------------------------------\




struct timespec t0;
void postavi_pocetno_vrijeme()
{
	clock_gettime(CLOCK_REALTIME, &t0);
}
 
// dohvaca vrijeme proteklo od pokretanja programa
void vrijeme(void)
{
	struct timespec t;

	clock_gettime(CLOCK_REALTIME, &t);

	t.tv_sec -= t0.tv_sec;
	t.tv_nsec -= t0.tv_nsec;
	if (t.tv_nsec < 0) {
		t.tv_nsec += 1000000000;
		t.tv_sec--;
	}

	printf("%03ld.%03ld:\t", t.tv_sec, t.tv_nsec/1000000);
}

// ispis kao i printf uz dodatak trenutnog vremena na pocetku
#define printft(format, ...)       \
do {                              \
  vrijeme();                      \
  printf(format, ##__VA_ARGS__);  \
}while(0);								  \

// \_kod za vrijeme ___________________________________________________________________________/;






void printIntAr(int x[],int n){
	int i;
	for(i=0;i<n;++i){
		printf("%d",x[i]);
	}
}



struct stog{
	int prioritet;
	int registar;
	bool zauzet;
};

int prioritet=0;
int kzastavica[3]={0};
struct stog r[3]={{0,0,false},{0,0,false},{0,0,false}};

void printStog(struct stog x[],int n){
	for(int i=0;i<n;i++){
		if(x[i].zauzet){
			printf("%d, reg[%d];",x[i].prioritet, x[i].registar);
		}else{
			printf("-;");
		}
	}
	
}
bool checkPrio(struct stog x[],int prio,int n){
	for(int i=0;i<n;i++){
		if(x[i].zauzet&&prio<i+1){
		return false;
		}
	}
	return true;
}

void printStanje(int kz[],int n,int tp, struct stog stanje[]){
	printft(" K_Z=");
	printIntAr(kz,n);
	printf(", T_P=%d, stog: ",tp);
	printStog(stanje,3);
	
}

int nije_kraj = 1;
int k1=0,k2=0,k3=0;

// izvodenje signala--------------------------------------------------------------------------------------------
void sljedeci(int n);

void izvodenje_p1(int n){
	kzastavica[2]=0;
	if(k1==0){printft("zapocinje obradu prekida razine 1\n");}
	else {printft("nastavlja obradu prekida razine 1\n");}
	printStanje(kzastavica,3,prioritet,r);
	printf("\n");
	printf("\n");
	for(k1;k1<8;k1++){
	sleep(1);	
	}
	printf("\n");
	printft("kraj obrade prekida razine 1\n");
	k1=0;
	sljedeci(n);
}

void izvodenje_p2(int n){
	kzastavica[1]=0;
	if(k2==0){printft("zapocinje obradu prekida razine 2\n");}
	else {printft("nastavlja obradu prekida razine 2\n");}
	printStanje(kzastavica,3,prioritet,r);
	printf("\n");
	printf("\n");
	for(k2;k2<8;k2++){
	sleep(1);	
	}
	printf("\n");
	printft("kraj obrade prekida razine 2\n");
	k2=0;
	sljedeci(n);
}

void izvodenje_p3(int n){
	kzastavica[0]=0;
	if(k3==0){printft("zapocinje obradu prekida razine 3\n");}
	else {printft("nastavlja obradu prekida razine 3\n");}
	printStanje(kzastavica,3,prioritet,r);
	printf("\n");
	printf("\n");
	for(k3;k3<8;k3++){
	sleep(1);	
	}
	printf("\n");
	printft("kraj obrade prekida razine 3\n");
	k3=0;
	sljedeci(n);
}
void glavni(){
	printft("Povratak u glavni program\n");
	printStanje(kzastavica,3,prioritet,r);
	printf("\n");
	printf("\n");
}

void sljedeci(int n){
	int j;
	for(j=n;j>=0;j--){
		if(r[j].zauzet){
		prioritet=r[j].prioritet;
		r[j].prioritet=0;r[j].registar=0;r[j].zauzet=false;
		break;
		}
    }
	printStanje(kzastavica,3,prioritet,r);
	printf("\n");
	printf("\n");
	switch(prioritet){
	case 0: glavni();break;
	case 1: izvodenje_p1(n);break;
	case 2: izvodenje_p2(n);break;
	}
}
// izvodenje signala___________________________________________________________________________________________________________________

//  Obrada Signala---------------------------------------------------------------------------------------------------------------------
void obradi_pr1(int sig){// SIGTERM p1
printf("\n");
	if(prioritet<1){  // ako je prioritet manji od 1
		r[0].prioritet=0; r[0].registar=0; r[0].zauzet=true; // pamti prekinuti prioritet
		prioritet=1;
		kzastavica[2]=1;
		
		printft("SKLOP: prekid razine 1, prosljeduje procesoru\n");
		printStanje(kzastavica,3,prioritet,r);
		printf("\n");
		printf("\n");
		
		printf("\n");
		izvodenje_p1(3);//izvodenje prkida 1
		
	}
	else if(prioritet>1){ // ako je prioritet veci od 1
	printf("\n");
	printft("SKLOP: prekid razine 1, zapamti na stogu");
	r[1].prioritet=1; r[1].registar=1; r[1].zauzet=true; // pamti prioritet 1
	kzastavica[2]=1;
	printf("\n");
	printStanje(kzastavica,3,prioritet,r);
	printf("\n");
	printf("\n");
	}
}

void obradi_pr2(int sig){// SIGUSR1 p2
printf("\n");
	if(prioritet<2){  // ako je prioritet manji od 2
		r[prioritet].prioritet=prioritet; r[prioritet].registar=prioritet; r[prioritet].zauzet=true; // pamti prekinuti prioritet.
		kzastavica[1]=1;
		prioritet=2;
		
		printft("SKLOP: prekid razine 2, prosljeduje procesoru\n");
		printStanje(kzastavica,3,prioritet,r);
		printf("\n");
		
		printf("\n");
		izvodenje_p2(3);//izvodenje prkida 2
		
		
	}
	else if(prioritet>2){ // ako je prioritet veci od 2
	printf("\n");
	printft("SKLOP: prekid razine 2, zapamti na stogu");
	r[2].prioritet=2; r[2].registar=2; r[2].zauzet=true;
	kzastavica[1]=1;
	printf("\n");
	printStanje(kzastavica,3,prioritet,r);
	printf("\n");
	printf("\n");
	}
}

void obradi_pr3(int sig){// SIGILL p3
printf("\n");
	if(prioritet<3){  // ako je prioritet manji od 3
		r[prioritet].prioritet=prioritet; r[prioritet].registar=prioritet; r[prioritet].zauzet=true;//pamti trenutni prioritet
		kzastavica[2]=1;
		prioritet=3;
		
		printft("SKLOP: prekid razine 3, prosljeduje procesoru\n");
		printStanje(kzastavica,3,prioritet,r);
		printf("\n");
		
		printf("\n");
		izvodenje_p3(3);//izvodenje prkida 3

		
	}
	
}
// obrada signala__________________________________________________________________________________________________________________________






int main (void){
	postavi_pocetno_vrijeme();
	
	
	
	
struct sigaction act;
 // maskiranje signala SIGTERM 
 act.sa_handler = obradi_pr1;
 sigemptyset(&act.sa_mask);
 sigaction(SIGTERM, &act, NULL); // maskiranje signala preko sučelja OS-a
 
 // maskiranje signala SIGUSR1 
 act.sa_handler = obradi_pr2; // kojom se funkcijom signal obrađuje
 sigemptyset(&act.sa_mask);
 sigaction(SIGUSR1, &act, NULL); // maskiranje signala preko sučelja OS-a
 

 // maskiranje signala SIGILL 
 act.sa_handler = obradi_pr3;
 sigemptyset(&act.sa_mask);
 sigaction(SIGILL, &act, NULL); // maskiranje signala preko sučelja OS-a
	

 printft("Program s PID=%ld krenuo s radom\n", (long) getpid());
 int k=0;
 while(nije_kraj) {
 //printf("\n");
 //printft("Program: iteracija %d", k++);
 sleep(2);
 }

	
	return 0;
}