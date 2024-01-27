/*
 * PID_controller.c
 *
 *  Created on: Jan 22, 2024
 *      Author: yazed almazroua
 */
#include "PID_controller.h"
 double kp = 10;
 double ki = 0.038;
 double kd = 500;
void PID(SERVO_Handle_TypeDef* servo,float average_distance , int setP)
{

	static double priError = 0;
	static double toError = 0;
	float dis = average_distance;
	float error = setP - dis;
	//calculating PID values
	double Pvalue = error * kp;
	double Ivalue = toError * ki;
	double Dvalue = (error - priError) * kd;
	double PIDvalue = Pvalue + Ivalue + Dvalue;
	priError = error;//previous error (DValue)
	toError += error;//total error{IValue}
	SERVO_WritePosition(servo, PIDvalue);
}

