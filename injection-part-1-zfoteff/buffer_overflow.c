#include <stdio.h>
#include <string.h>

int check_password(char *password) {
    int flag = 0;
    char buffer[20];    
    strcpy(buffer, password);
    
    if (strcmp(buffer, "mypass") == 0){
        flag = 1;
    }
    if (strcmp(buffer, "yourpass") == 0){
        flag = 1;
    }
    return flag;
}

void print_message(int is_access_granted) {
    if (is_access_granted) {
        printf("%s", "Access granted\n");
    } else {
        printf("%s", "Access denied\n");
    }
}

int main(int argc, char *argv[]) {
    printf("checking %s...\n", "mypass");
    print_message(check_password("mypass"));
    
    printf("checking %s...\n", "yourpass");
    print_message(check_password("yourpass"));
    
    printf("checking %s...\n", "wepass");
    print_message(check_password("wepass"));

    int i = 0;
    while (1)
    {
        char format_string[15];
        sprintf(format_string, "wepass%%%ds", i);
        char input[i];
        sprintf(input, format_string, "!");
        if (check_password(input)) {
            printf("The following password smashed the stack! \"%s\"\n", input);
            print_message(1);
            break;
        }
        
        if (i >= 1000) {
            printf("Could not smash the stack!");
            break;
        }
        
        i++;
    }
}
