// IO libraries
#include <stdlib.h>
#include <stdio.h>
#include <stdint.h>
#include <string.h>

// UART libraries
#include <unistd.h>
#include <fcntl.h>
#include <termios.h>
#include <errno.h>

int main(int argc, char **argv)
{
    int fd;
    //int flags;
    printf("Pi Zero W <-> RP-2040 Serial Interface\nCTRL+C to end\n");

    // open Gadget Serial port (read/write, non-blocking)
    //fd = open("/dev/ttyGS0", O_RDWR | O_NOCTTY | O_NDELAY);
    // Open Gadget Serial port 0 (read/write, not controlled by calling process' terminal, blocking)
    fd = open("/dev/ttyAMA0", O_RDWR | O_NOCTTY);

    if (fd == -1) {
        printf("Unable to open serial port.\n\n");
        return EXIT_FAILURE;
    }
    else {
        printf("Opened serial port.\n");
    }

    struct termios options;
    tcgetattr(fd, &options);

    // Output Options
    options.c_cflag = B115200 | CLOCAL | CREAD; // Set baud rate
    // "8N1"
    options.c_cflag &= ~PARENB;     // Disable parity bit
    options.c_cflag &= ~CSTOPB;     // Disable 2nd stop bit
    options.c_cflag &= ~CSIZE;      // Clear bit mask
    options.c_cflag |= CS8;         // Set bit mask for 8 data bits
    options.c_cflag &= ~CRTSCTS;    // Disable hardware flow ctrl

    options.c_iflag = IGNPAR;
    options.c_oflag &= ~OPOST;      // Select raw output
    options.c_cc[VMIN] = 1;         // Byte by byte
    options.c_cc[VTIME] = 0;        // Do not wait
    tcflush(fd, TCIFLUSH);

    // Input options
    options.c_lflag &= ~(ICANON | ECHO | ECHOE | ISIG); // Select raw input
    options.c_iflag &= ~(IXON | IXOFF | IXANY);         // Disable SW flow control

    // Apply options
    tcsetattr(fd, TCSANOW, &options);
    printf("Set options attribute.\n");
    //tcgetattr(fd, &options_out);
    //printf("Serial status: %s", flags);

    // Turn off blocking on reads
    //fcntl(fd, F_SETFL, 0);

    // Read for input
    unsigned char Buffer[1] = {0};
    Buffer[0] = "A";
    for ( ;; ) {
        int cntr = read(fd, (void *)Buffer, 1);
        // Data received, print
        if (cntr < -1) {
            printf("! Error '%s' (%d) received on read attempt.\n", strerror(errno), cntr);
            //flags = fcntl(fd, F_GETFL);      // Get flags
            //printf("Serial status: %s", flags);
            //return EXIT_FAILURE;
        }
        if (cntr > 0) {
            printf("%s", Buffer);
        }
    }

    close(fd);

    return EXIT_SUCCESS;
}
