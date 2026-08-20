#include <fcntl.h>
#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>

int main(void) {
    const char *path="/tmp/os_syscall_demo.txt";
    const char *msg="system call laboratory\n";
    char buffer[128]={0};
    int fd=open(path,O_CREAT|O_TRUNC|O_RDWR,0600);
    if(fd<0){perror("open");return EXIT_FAILURE;}
    if(write(fd,msg,23)<0){perror("write");return EXIT_FAILURE;}
    if(lseek(fd,0,SEEK_SET)<0){perror("lseek");return EXIT_FAILURE;}
    ssize_t n=read(fd,buffer,sizeof(buffer)-1);
    if(n<0){perror("read");return EXIT_FAILURE;}
    printf("%s",buffer);
    close(fd); unlink(path); return EXIT_SUCCESS;
}
