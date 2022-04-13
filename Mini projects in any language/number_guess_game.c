#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main()
{
    system("CLS");
    int number, guess, nguesses = 1;
    srand(time(0));
    number = rand() % 100 + 1; // Generates Random number btw. 1 & 100
    // printf("%d", number);
    do
    {
        printf("Guess a number btw. 1 - 100\n");
        scanf("%d", &guess);
        if (guess > number)
        {
            printf("Lower Number Please\n");
        }
        else if (guess < number)
        {
            printf("Higher Number Please\n");
        }
        else
        {
            printf("You Guessed it in %d attempts\n", nguesses);
        }
        nguesses++;
    } while (guess != number);

    getchar();
    return 0;
}