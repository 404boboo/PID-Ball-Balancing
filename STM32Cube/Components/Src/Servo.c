/**
  ******************************************************************************
  * @file		  : __template.c
  * @author  	: AW		Adrian.Wojcik@put.poznan.pl
  * @version 	: 1.3.0
  * @date    	: Oct 19, 2022
  * @brief   	: COMPONENT SOURCE FILE TEMPLATE
  *
  ******************************************************************************
  */

/* Private includes ----------------------------------------------------------*/
#include "Servo.h"
#include "common.h"

/* Private typedef -----------------------------------------------------------*/

/* Private define ------------------------------------------------------------*/
#define SERVO_MIN_DUTY 	2.5f
#define SERVO_MAX_DUTY 12.5f

/* Private macro -------------------------------------------------------------*/

/* Private variables ---------------------------------------------------------*/

/* Public variables ----------------------------------------------------------*/

/* Private function prototypes -----------------------------------------------*/

/* Public function prototypes ------------------------------------------------*/

/* Private functions ---------------------------------------------------------*/

/* Public functions ----------------------------------------------------------*/
/**
  * @brief Initializes a servo motor.
  * @param[in/out] hservo : Servo motor handler.
  * @retval None
  */

void SERVO_Init(SERVO_Handle_TypeDef* hservo)
{
	SERVO_WritePosition(hservo, 90.0f);
	PWM_Init(&(hservo->PwmOut));
}
/**
  * @brief Writes a new position to the servo motor.
  * @param[in/out] hservo : Servo motor handler.
  * @param[in] pos        : Desired position for the servo motor.
  * @retval None
  */

void SERVO_WritePosition(SERVO_Handle_TypeDef* hservo, float pos)
{
	hservo->Position = __SATURATION(pos, 120.0f, 160.0f);
	float duty = __LINEAR_TRANSFORM(hservo->Position, 120.0f, 160.0f, SERVO_MIN_DUTY, SERVO_MAX_DUTY);
	PWM_WriteDuty(&(hservo->PwmOut), duty);
}

/**
  * @brief Reads and returns the current position of the servo motor.
  * @param[in] hservo : Servo motor handler.
  * @retval float      : Current position of the servo motor.
  */

float SERVO_ReadPosition(SERVO_Handle_TypeDef* hservo)
{
	return hservo->Position;
}
