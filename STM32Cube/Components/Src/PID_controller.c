/**
  ******************************************************************************
  * @file    PID_controller.c
  * @author  Yazid Almazroua
  * @author  Konrad Marchewka
  * @version V1.0
  * @date    23-Jan-2024
  * @brief   Simple PID controller set up
  *
  ******************************************************************************
  */
#include "PID_controller.h"
#include "hcsr04_sensor.h"

double kp = 10;
double ki = 0.038;
double kd = 500;

void PID(struct us_sensor_str* Sensor, SERVO_Handle_TypeDef* servo)
{
    int setP = 30;
    static double priError = 0;
    static double toError = 0;
    float dis = Sensor->distance_cm;
    float error = setP - dis;

    // calculating PID values
    double Pvalue = error * kp;
    double Ivalue = toError * ki;
    double Dvalue = (error - priError) * kd;
    double PIDvalue = Pvalue + Ivalue + Dvalue;

    priError = error;     // previous error (DValue)
    toError += error;      // total error {IValue}

    SERVO_WritePosition(servo, PIDvalue);
}


