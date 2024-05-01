#include <stdio.h>
#include <string.h>

int main() {
    // O(1)
    char name[] = "World";
    printf("Hello, %s!\n", name); // N

    // O(min(M, K)) ~ O(N)
    char test[] = "abcdef"; // M - length of test
    printf("%d\n", strncmp(test, "abc", 3)); // K - length of substring

    // O(M * K) ~ O(N^2)
    char test2[] = "abcdabcd"; // M - length of test2
    printf("%ld\n", strstr(test2, "bc") - test2); // K - length of substring

    // O(M * K) ~ O(N^2)
    char test3[] = "abcdabcd"; // M - length of test3
    int count = 0;
    char *pos = test3;
    while ((pos = strstr(pos, "bc")) != NULL) {
        count++;
        pos += 2;
    }
    printf("%d\n", count); // K - length of substring

    // O(N)
    char test4[] = "abcdabcd"; // M - length of test4
    char *pos2 = test4;
    while ((pos2 = strstr(pos2, "bc")) != NULL) {
        strncpy(pos2, "TTT", 3); // K - length of replacement
    }
    printf("%s\n", test4); // K - length of substring

    // O(N)
    char test5[] = "abcdabcd"; // M - length of test5
    char *token = strtok(test5, "bc");
    while (token != NULL) {
        printf("%s\n", token);
        token = strtok(NULL, "bc");
    }

    // O(N)
    char arr[] = {'1', '1', '2', '2', '3', '3', '\0'};
    char separator[] = "++";
    int arr_len = sizeof(arr) / sizeof(arr[0]);
    for (int i = 0; i < arr_len - 1; i++) {
        printf("%c%c", arr[i], separator[0]);
    }
    printf("%c\n", arr[arr_len - 1]);

    // O(N)
    char text2[] = "abcdabcd"; // M - length of text2
    for (int i = 0; i < strlen(text2); i++) {
        text2[i] = toupper(text2[i]);
    }
    printf("%s\n", text2);

    return 0;
}
