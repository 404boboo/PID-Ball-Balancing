/**
  ******************************************************************************
  * @file     : PID_controller.h
  * @author   : Yazid Almazrua
  * @author   : Konrad Marchewka
  * @author   : AW    Adrian.Wojcik@put.poznan.pl
  * @version  : 1.3.0
  * @date     : Nov 27, 2022
  * @brief    : Pulse Width Modulation outputs components driver.
  *
  ******************************************************************************
  */

#ifndef INC_PID_CONTROLLER_H_
#define INC_PID_CONTROLLER_H_

/*Includes-------------------------------------------------------*/
#include "hcsr04_sensor.h"
#include "stm32f7xx_hal.h"
#include "Servo.h"

/* Public typedef ------------------------------------------------------------*/

/* Public define -------------------------------------------------------------*/

/* Public macro --------------------------------------------------------------*/

/* Public variables ----------------------------------------------------------*/
extern double kp;
extern double ki;
extern double kd;
extern int setP;

/* Public function prototypes ------------------------------------------------*/

void PID(SERVO_Handle_TypeDef* servo, int Position, int SetP);


#endif /* INC_PID_CONTROLLER_H_ */
