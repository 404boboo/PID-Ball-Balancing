/**
  ******************************************************************************
  * @file		: servo.h
  * @author  	: AW		Adrian.Wojcik@put.poznan.pl
  * @version 	: 1.3.0
  * @date    	: Oct 24, 2023
  * @brief   	: MG90S micro servo motor
  *
  ******************************************************************************
  */

#ifndef INC_SERVO_H_
#define INC_SERVO_H_

/* Public includes -----------------------------------------------------------*/
#include "pwm.h"

/* Public typedef ------------------------------------------------------------*/

// Structure to handle a servo motor.
typedef struct {
	PWM_Handle_TypeDef PwmOut;
	float Position;
} SERVO_Handle_TypeDef;

/* Public define -------------------------------------------------------------*/

/* Public macro --------------------------------------------------------------*/

/* Public variables ----------------------------------------------------------*/

/* Public function prototypes ------------------------------------------------*/
/**
  * @brief Initializes a servo motor.
  * @param[in/out] hservo : Servo motor handler.
  * @retval None
  */

void SERVO_Init(SERVO_Handle_TypeDef* hservo);

/**
  * @brief Writes a new position to the servo motor.
  * @param[in/out] hservo : Servo motor handler.
  * @param[in] pos        : Desired position for the servo motor.
  * @retval None
  */

void SERVO_WritePosition(SERVO_Handle_TypeDef* hservo, float pos);

/**
  * @brief Reads and returns the current position of the servo motor.
  * @param[in] hservo : Servo motor handler.
  * @retval float      : Current position of the servo motor.
  */
float SERVO_ReadPosition(SERVO_Handle_TypeDef* hservo);

#endif /* INC_SERVO_H_ */
