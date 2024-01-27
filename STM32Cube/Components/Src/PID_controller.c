/*
 * PID_controller.c
 *
 *  Created on: Jan 22, 2024
 *      Author: yazed almazroua
 */
#include "PID_controller.h"
#include "time.h"
#include <stdio.h>
clock_t start_t, end_t;
 double kp = 2;
 double ki = 2;
 double kd = 9000;

void PID(SERVO_Handle_TypeDef* servo, int average_value , int setP)
{

    double setPP = setP;
	static double priError = 0;
	static double toError = 0;
	float dis = average_value;
	float error = setPP - dis;
	//calculating PID values

	double Pvalue = error * kp;
	double Ivalue = ki * (error * ki);
	double Dvalue = (error - priError) * kd;
	double PIDvalue = Pvalue + Dvalue + Ivalue;
	//Ivalue = PIDvalue + ki*error;



	if (-2 < error && error < 2) {
	    start_t = clock();
	    Ivalue += ki * error;

	    // Limit the integral term to prevent windup

	} else {
	    Ivalue = 0;
	}
	priError = error;//previous error (DValue)
	toError += error;//total error{IValue}
	SERVO_WritePosition(servo, PIDvalue);
	end_t = clock();
}

