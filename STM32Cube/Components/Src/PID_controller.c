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

/* Public includes -----------------------------------------------------------*/
#include "PID_controller.h"
#include "hcsr04_sensor.h"

/* Public typedef ------------------------------------------------------------*/

/* Public define -------------------------------------------------------------*/

/* Public macro --------------------------------------------------------------*/

/* Public variables ----------------------------------------------------------*/
double kp = 3;   // Proportional gain parameter in the PID controller. Scales the error to determine the proportional contribution.
double ki = 0.03;  // Integral gain parameter in the PID controller. Scales the accumulated error over time to determine the integral contribution.
double kd = 18000;  // Derivative gain parameter in the PID controller. Scales the rate of change of the error to determine the derivative contribution.
/* Private variables ---------------------------------------------------------*/

/* Public function prototypes ------------------------------------------------*/

/* Private functions ---------------------------------------------------------*/

/* Public function prototypes ------------------------------------------------*/

/**
*@brief: Calculate the PID control output based on the Proportional, Integral, and Derivative components
*@param:
*@retval: None
*/
void PID(SERVO_Handle_TypeDef* servo, int Position, int SetP)
{

    static double priError = 0;
    static double toError = 0;
    float dis = Position;
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


