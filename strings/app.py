# coding=UTF-8
from text_formatter import formatter

string = input("\nInsira o texto a ser formatado: ")

char = input("\nInsira o número máximo de carácteres por linha: ")

print(formatter(string, char))