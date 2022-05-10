#include <SoftwareSerial.h>
SoftwareSerial Bluetooth(2,4); // D2 = TX - D4 = RX
String Trame = "";
#define CartDebut  "#";
#define  CartFin "$";
int CapTemp = 0 ;
int CapTension = 1;
int ValeurSortiTemp ;
int R1 = 10000;
int ValeurTempFinal;
float Tension ; 
int ValeurtensionFinal ;
void setup(){
  Serial.begin(9600);
  Bluetooth.begin(9600);

  
}


void loop(){
  ValeurSortiTemp = analogRead(CapTemp);
  ValeurTempFinal= ((R1+ValeurSortiTemp*5) / ValeurSortiTemp) ;

  Tension = analogRead(CapTension)/41.00 ;

  ValeurtensionFinal = Tension*100;

  Trame =  Trame + CartDebut ;
  Trame = Trame + "/";
  Trame = Trame + ValeurTempFinal;
  Trame = Trame + "/";
  Trame = Trame + ValeurtensionFinal;
  Trame = Trame + "/";
  Trame = Trame + CartFin;
  Bluetooth.println(Trame);
  Serial.println(Trame);
  delay(500);
  Trame = "";
}
