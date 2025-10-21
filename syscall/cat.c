#include <stdio.h>
#include <stdlib.h>
#include <fcntl.h>
#include <unistd.h>

#define BUFFER_SIZE 256

int main(int argc, char *argv[]) {
    if(argc!=2){
        fprintf(stderr,"Usage: %s <filename>\n",argv[0]);
        exit(1);
    }
    int fd=open(argv[1],O_RDONLY);
    if(fd==-1){
        perror("Error opening file");
        exit(1);
    }
    char buffer[BUFFER_SIZE];
    ssize_t bytes_read;
    while((bytes_read=read(fd,buffer,BUFFER_SIZE))>0)
        if(write(STDOUT_FILENO,buffer,bytes_read)==-1){
            perror("Error writing to stdout");
            close(fd);
            exit(1);
        }
    if(bytes_read==-1){
        perror("Error reading file");
        close(fd);
        exit(1);
    }
    if(close(fd)==-1){
        perror("Error closing file");
        exit(1);
    }
    return 0;
}
