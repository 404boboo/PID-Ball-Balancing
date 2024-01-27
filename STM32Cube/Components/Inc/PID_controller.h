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

/*---------------------------------------------------------------*/

/*Defines and variables------------------------------------------*/

extern double kp;
extern double ki;
extern double kd;
extern int setP;

//void PID(hcsr04_data_t* Sensor ,SERVO_Handle_TypeDef* servo );


#endif /* INC_PID_CONTROLLER_H_ */
