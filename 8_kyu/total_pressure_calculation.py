#https://www.codewars.com/kata/5b7ea71db90cc0f17c000a5a

def solution(molar_mass1, molar_mass2, given_mass1, given_mass2, volume, temp) :
    return (given_mass1/molar_mass1 + given_mass2/molar_mass2)*0.082*(temp+273.15)/volume