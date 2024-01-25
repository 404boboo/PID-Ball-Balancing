/*
 * PID_controller.h
 *
 *  Created on: Jan 22, 2024
 *      Author: yazed almazroua
 */

#ifndef INC_PID_CONTROLLER_H_
#define INC_PID_CONTROLLER_H_
#include "hcsr04_sensor.h"
#include "stm32f7xx_hal.h"
#include "Servo.h"

extern double kp;
extern double ki;
extern double kd;

//void PID(hcsr04_data_t* Sensor ,SERVO_Handle_TypeDef* servo );


#endif /* INC_PID_CONTROLLER_H_ */
