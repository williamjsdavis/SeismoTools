#include <stdio.h>
#include <string.h>

#define HEADER1_WORDS 70
#define HEADER2_WORDS 40
#define HEADER3_WORDS 24

char parse_input( int argc, char *argv[] ){
    
    if( argc == 2 ) {
        printf("The argument supplied is %s\n", argv[1]);
        printf("length is %lu\n", strlen(argv[1]));
    }
    else if( argc > 2 ) {
        printf("Too many arguments supplied.\n");
    }
    else {
        printf("One argument expected.\n");
    }

    return *argv[1];
}

int main( int argc, char *argv[] ){
    int header1_nwords;
    int header2_nwords;
    int header3_nwords;
    char in_string;

    header1_nwords = HEADER1_WORDS;
    header2_nwords = HEADER2_WORDS;
    header3_nwords = HEADER3_WORDS;
    
    printf("Words in header 1: %d\n", header1_nwords);
    printf("Words in header 2: %d\n", header2_nwords);
    printf("Words in header 3: %d\n", header3_nwords);

    in_string = parse_input(argc, argv);
    
    /*printf("In string is: %s\n", in_string);*/

    return 0;
}
