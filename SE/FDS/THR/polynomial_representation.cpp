#include <bits/stdc++.h>
#include <iostream>
using namespace std;

typedef struct Polynomial {
    int coeff;
    int exponent;
} Poly;

void populate(Poly POLY[], int TERMS){
    cout << "Enter the Coefficents and Exponents for the Polynomial Expression:\n";
    for (int i = 0; i < TERMS; i++){
        int COEFF = 0; int EXPO = 0;
        cout << "Enter the Coefficient: "; cin >> COEFF;
        cout << "Enter the Exponent: "; cin >> EXPO;
        POLY[i].coeff = COEFF;
        POLY[i].exponent = EXPO; 
    }
}

void display(Poly POLY[], int TERMS){
    cout << "\nThe Polynomial Expression is: \n";
    for (int i = 0; i < TERMS; i++){
        if (POLY[i].coeff == 0) continue;
        else if (i == (TERMS-1)) {
            if (POLY[i].exponent == 0) {
                cout << POLY[i].coeff << endl;
            } else {
                cout << POLY[i].coeff <<  "x^" << POLY[i].exponent << endl;             
            }
        } else {
            cout << POLY[i].coeff << "x^" << POLY[i].exponent << " + ";
        }
    }
}

void add(Poly *POLY1, Poly *POLY2, int TERMS1, int TERMS2) {
    for (int i = 0; i < TERMS1; i++){
        for (int j = 0; j < TERMS2; j++){
            if (POLY1[i].exponent == POLY2[j].exponent){
                POLY1[i].coeff = POLY1[i].coeff + POLY2[j].coeff;
            } 
        }
    } 
    cout << "Required Sum is: \n";
    for (int i = 0; i < TERMS1; i++){
        if (POLY1[i].coeff == 0) continue;
        else if (i == (TERMS1-1)) {
            if (POLY1[i].exponent == 0) {
                cout << POLY1[i].coeff << endl;
            } else {
                cout << POLY1[i].coeff <<  "x^" << POLY1[i].exponent << endl;             
            }
        } else {
            cout << POLY1[i].coeff << "x^" << POLY1[i].exponent << " + ";
        }
    }
}

int main(){
    Poly P1[3];
    Poly P2[3];
    populate(P1, 3);            
    populate(P2, 3);
    add(P1, P2, 3, 3);
    return 0;
}


/* PROGRAM OUTPUT *

Enter the Coefficents and Exponents for the Polynomial Expression:
Enter the Coefficient: 1
Enter the Exponent: 2
Enter the Coefficient: 2
Enter the Exponent: 1
Enter the Coefficient: 3
Enter the Exponent: 0
Enter the Coefficents and Exponents for the Polynomial Expression:
Enter the Coefficient: 7
Enter the Exponent: 2
Enter the Coefficient: 8
Enter the Exponent: 1
Enter the Coefficient: 9
Enter the Exponent: 0

The Polynomial Expression is:
1x^2 + 2x^1 + 3

The Polynomial Expression is:
7x^2 + 8x^1 + 9

Required Sum is:
8x^2 + 10x^1 + 12

* END OUTPUT */

