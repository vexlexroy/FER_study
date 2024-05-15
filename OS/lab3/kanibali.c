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

#define max 20

struct osoba{
	char tip;
	int index;
};

struct osoba Lo[max];
struct osoba Do[max];
struct osoba camac[7]; 
int strana; //0 ljevo, 1 desno
int sekunda;
pthread_cond_t ukrcajsLm;
pthread_cond_t ukrcajsDm;
pthread_cond_t ukrcajsLk;
pthread_cond_t ukrcajsDk;
pthread_cond_t ukrcajL;
pthread_cond_t ukrcajD;
pthread_mutex_t ulaz;




int count(){
	int n=0;
	for(int i=0;i<7;i++){
		if(camac[i].index!=0){
			n++;
		}
	}
	return n;
}

int countM(){
	int n=0;
	for(int i=0;i<7;i++){
		if(camac[i].tip=='M'){
			n++;
		}
	}
	return n;
}

int countK(){
	int n=0;
	for(int i=0;i<7;i++){
		if(camac[i].tip=='K'){
			n++;
		}
	}
	return n;
}
int contains(char tipOsobe){
	for(int i=0;i<max;i++){
		if(strana){
			if(Do[i].tip==tipOsobe) return 1;
		}
		else{
			if(Lo[i].tip==tipOsobe) return 1;
		}
	}
	return 0;
}

int addLo(int index, char tipOs){
	for(int i=0;i<max;i++){
			if(Lo[i].index==0){
				Lo[i].index=index;
				Lo[i].tip=tipOs;
				return 1;
			}
			
	}
	return 0;
}

int addDo(int index, char tipOs){
	for(int i=0;i<max;i++){
			if(Do[i].index==0){
				Do[i].index=index;
				Do[i].tip=tipOs;
				return 1;
			}
			
	}
	return 0;
}

int addC(struct osoba x){
	for(int i=0;i<max;i++){
			if(camac[i].index==0){
				camac[i]=x;
				return 1;
			}
			
	}
	return 0;
}

int removeEl(struct osoba x){
	if(strana){
		for(int i=0;i<max;i++){
			if(Do[i].index==x.index&&Do[i].tip==x.tip){
				Do[i].index=0;
				Do[i].tip='N';
				return 1;
			}		
		}
	}
	else{
		for(int i=0;i<max;i++){
			if(Lo[i].index==x.index&&Lo[i].tip==x.tip){
				Lo[i].index=0;
				Lo[i].tip='N';
				return 1;
			}		
		}	
	}
	return 0;
}

void prevezi(){
	printf("camac preveo: ");
	for(int i=0;i<7;i++){
		if(camac[i].index!=0)
		printf("%c%d ",camac[i].tip,camac[i].index);
		camac[i].index=0;
		camac[i].tip='N';
	}printf("\n\n");
}


void printAll(){
	char s;
	if(strana)s='D';
	else s='L';
	
	printf("C[%c]={",s);
	
	for(int i=0;i<7;i++)
		if(camac[i].index!=0)
			printf("%c%d ",camac[i].tip,camac[i].index);
		
	printf("} LO={");
	
	for(int i=0;i<max;i++)
		if(Lo[i].index!=0)
			printf("%c%d ",Lo[i].tip,Lo[i].index); 
		
	printf("} DO={");
	
	for(int i=0;i<max;i++)
		if(Do[i].index!=0)
			printf("%c%d ",Do[i].tip,Do[i].index);
	printf("}\n\n");
	  
}
//iteracija3
void *misionar(void *arg){
	int index=*(int*)arg;
	int ob=rand()%2;
	struct osoba x;
	x.index=index;
	x.tip='M';
	if(ob==0){
		addLo(index,'M');//dodaj na ljevu
		printf("Misionar M%d dosao na ljevu obalu\n",index);
		printAll();
	}else{ 
		addDo(index,'M');//dodaj na desnu
		printf("Misionar M%d dosao na desnu obalu\n",index);
		printAll();
	}
	
	pthread_mutex_lock(&ulaz);
		while(1){
			if(ob)
				pthread_cond_wait(&ukrcajD,&ulaz);
			else
				pthread_cond_wait(&ukrcajL,&ulaz);
			if(count()<7){
				if(countK()<3){
					break;
				}
			}

		}
		
		removeEl(x);
		addC(x);
		printf("Misionar M%d usao u camac\n",index);
		printAll();
	pthread_mutex_unlock(&ulaz);
	
}
void *kanibal(void *arg){
	int index=*(int*)arg;
	int ob=rand()%2;
	struct osoba x;
	x.index=index;
	x.tip='K';
	if(ob==0){
		addLo(index,'K');//dodaj na ljevu
		printf("Kanibal K%d dosao na ljevu obalu\n",index);
		printAll();
	}else{ 
		addDo(index,'K');//dodaj na desnu
		printf("Kanibal K%d dosao na desnu obalu\n",index);
		printAll();
	}
	
	pthread_mutex_lock(&ulaz);
		while(1){
			if(ob)
				pthread_cond_wait(&ukrcajD,&ulaz);
			else
				pthread_cond_wait(&ukrcajL,&ulaz);
			if(count()<7){
				if(countM()==0){
					break;
				}
				else if(countK()<countM()){
					break;
				}
				else;
			}
		}
		
		removeEl(x);
		addC(x);
		printf("Kanibal K%d usao u camac\n",index);
		printAll();
	pthread_mutex_unlock(&ulaz);
	
}
void *camacf(void *arg){
	if(strana){
		printf("Camac: Na desnoj obali\n");
		printAll();
	}
	else{
		printf("Camac: Na ljevoj obali\n");
		printAll();
	}
	
	while(1){
		if(count()>=3 && (countK()<=countM()||countM()==0)){
			if(strana)
				pthread_cond_broadcast(&ukrcajD);
			else
				pthread_cond_broadcast(&ukrcajL);
			
			printf("\nCamac: Cekam sekundu\n");
			sleep(1);
			pthread_mutex_lock(&ulaz);
				printf("\nCamac krece na drugu obalu.\n\n");
				sleep(2);
				prevezi();
				if(strana)strana=0;
				else strana=1;
			pthread_mutex_unlock(&ulaz);
			
		}
		else{
			if(strana)
				pthread_cond_broadcast(&ukrcajD);
			else
				pthread_cond_broadcast(&ukrcajL);
		}
	}
	
}



int main(void){
	srand(time(NULL));
	pthread_t dretve[100];
	pthread_mutex_init(&ulaz,NULL);
	/*pthread_cond_init(&ukrcajsDm,NULL);
	pthread_cond_init(&ukrcajsLm,NULL);
	pthread_cond_init(&ukrcajsDk,NULL);
	pthread_cond_init(&ukrcajsLk,NULL);*/
	pthread_cond_init(&ukrcajD,NULL);
	pthread_cond_init(&ukrcajL,NULL);
	sekunda=0;
	strana=0; 
	int m=0;
	int k=0;
	void *y;
	
	//inicijalizacija polja
	for(int i=0;i<max;i++){
		Lo[i].index=0;
		Lo[i].tip='N';
		Do[i].index=0;
		Do[i].tip='N';
	}
	for(int i=0;i<7;i++){
		camac[i].index=0;
		camac[i].tip='N';
	}
	//---------------------
	y=&strana;
	pthread_create(&dretve[0],NULL,camacf,y);//stvori brod  
	
	for(int i=1;i<100;i++){
		if(i==99){
			i=0;
		}
		sleep(1);
		if(i%2){
			k++;
			y=&k;
			pthread_create(&dretve[i],NULL,kanibal,y);
		}
		else{
			m++;
			y=&m;
			pthread_create(&dretve[i],NULL,misionar,y);
		}
	}
}


 