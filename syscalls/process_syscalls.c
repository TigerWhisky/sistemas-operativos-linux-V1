#include <stdio.h>
#include <unistd.h>
#include <sys/wait.h>
#include <stdlib.h>

int main(void){
    printf("parent PID=%ld\n",(long)getpid());
    pid_t pid=fork();
    if(pid<0){perror("fork");return EXIT_FAILURE;}
    if(pid==0){
        printf("child PID=%ld PPID=%ld\n",(long)getpid(),(long)getppid());
        execlp("sh","sh","-c","printf 'exec completed\\n'",(char*)NULL);
        perror("execlp"); _exit(127);
    }
    waitpid(pid,NULL,0); return EXIT_SUCCESS;
}
