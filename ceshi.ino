
char col;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(115200); 
}

void loop() {
  // put your main code here, to run repeatedly:
 while(Serial.available()>0) //不断循环检测串口缓存，发现改为=1 也可，改为=2 不行。则Serial.available()读取到的是电平
 {
  col = Serial.read();
  if(col == 'a')
  {
    Serial.print("Read:");
    Serial.println(int(col));
    delay(1000);
    }
  }
}
